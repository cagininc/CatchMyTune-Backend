from django.db import models


class Song(models.Model):
    title=models.CharField(max_length=100)
    artist=models.CharField(max_length=100)
    audio_file=models.FileField(upload_to='songs/')
    
    def __str__(self):
        return f"{self.title} by {self.artist}"
    
    