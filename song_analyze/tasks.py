from songUpload.models import Song
from celery import shared_task
import librosa
import numpy as np

@shared_task
def analyze_song_task(song_id):
    #get song from DB
    
    song=Song.objects.get(id=song_id)
    
    #Loading the audio file using librosa
    #Pathway control before librosa
    try:
        y,sr= librosa.load(song.audio_file.path)
    except Exception as e:
        print(f"Error loading audio file:{e}")
        return
    
    # Calculating tempo
    try:
        tempo,_=librosa.beat.beat_track(y=y,sr=sr)
        song.tempo= tempo
    except Exception as e:
        print(f"Tempo Error:{e}")
        return
    
    #Other Calculations...
    try:
        chroma = librosa.feature.chroma_cqt(y=y, sr=sr)  # Chroma specs
        key_index = np.argmax(chroma.mean(axis=1))  # find strongest note
        keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        song.key = keys[key_index]  # define tonality and save it
    except Exception as e:
        print(f"Error calculating key: {e}")
        return
    try:
        # Onset power and spectral changes
        onset_env = librosa.onset.onset_strength(y=y, sr=sr)
        spectral_flux = np.mean(np.diff(onset_env))  #  calculate spectral changes
        zcr = np.mean(librosa.feature.zero_crossing_rate(y))  # zero_crossing_rate
        
        # Danceability Score
        danceability = (tempo / 200) + (spectral_flux / 2) + (zcr * 2)
        song.danceability = min(danceability, 1.0)  # limit Danceability  value and save
    except Exception as e:
        print(f"Error calculating danceability: {e}")
        return
    #optimizing dancebiity score with(spotify API vs...)
    
    
    #mark the song analyze completed
    song.is_analyzed=True
    song.save()