

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Song
import librosa
import numpy as np

def analyze_song(song_id):
#get song from database
    song = get_object_or_404(Song, id=song_id)

    y, sr = librosa.load(song.audio_file.path)

# demo analysis, calculating tempo
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    song.tempo = tempo