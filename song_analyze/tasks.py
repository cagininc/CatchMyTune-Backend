import os
import django
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from songUpload.models import Song
from celery import shared_task
import librosa
import numpy as np
import logging
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catch_my_tune.settings')
django.setup()

# Logging settings
logging.basicConfig(
    level=logging.INFO,
    filename='celery_tasks.log',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@shared_task
def analyze_song_task(song_id):
    logging.info(f"Starting analysis for song ID: {song_id}")
    channel_layer = get_channel_layer()
    group_name = f"song_{song_id}"

    try:
        # song
        logging.info("Fetching song from database")
        song = Song.objects.get(id=song_id)
        logging.info(f"Song fetched: {song}")

        # Librosa song upload
        logging.info(f"Loading audio file from: {song.audio_file.path}")
        y, sr = librosa.load(song.audio_file.path)
        logging.info(f"Audio file loaded: y={type(y)}, sr={sr}")

        # Tempo (bpm)
        logging.info("Performing tempo analysis")
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        song.tempo = float(tempo)  # json 
        logging.info(f"Tempo analysis completed: {song.tempo}")

        # song duration for users
        logging.info("Calculating song duration")
        duration = librosa.get_duration(y=y, sr=sr)
        song.duration = f"{int(duration // 60)}:{int(duration % 60):02d}"
        logging.info(f"Duration calculated: {song.duration}")

        # Key analysis
        logging.info("Performing key analysis")
        chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
        key_index = np.argmax(chroma.mean(axis=1))
        keys = ['C/Amin', 'C#/A#min', 'D/Bmin', 'D#/Cmin', 'E/C#min', 'F/Dmin', 
               'F#/D#min', 'G/Emin', 'G#/Fmin', 'A/F#min', 'A#/Gmin', 'B/G#min']
        song.key = keys[key_index]
        logging.info(f"Key analysis completed: {song.key}")

        #analyze completed
        logging.info("Marking song as analyzed")
        song.is_analyzed = True
        song.save()
        logging.info(f"Song saved: {song}")

        # send to ws
        results = {
            'tempo': song.tempo,
            'key': song.key if hasattr(song, 'key') else None,
            'duration': song.duration,
        }
        logging.info(f"Prepared WebSocket message: {results}")

        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                'type': 'send_analysis_update',
                'status': 'completed',
                'results': results,
            }
        )
        logging.info(f"Analysis completed and results sent for song ID: {song_id}")

    except Exception as e:
        # error message to ws
        logging.error(f"Error during analysis for song ID {song_id}: {e}")
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                'type': 'send_analysis_update',
                'status': 'error',
                'error': str(e),
            }
        )
