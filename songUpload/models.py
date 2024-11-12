from django.db import models

class Song(models.Model):
    title=models.CharField(max_length=100)
    artist=models.CharField(max_length=100)
    audio_file=models.FileField(upload_to='songs/')
    upload_date=models.DateTimeField( auto_now_add=True)
    tempo=models.FloatField(null=True,blank=True)
    key=models.CharField(null=True,blank=True)
    spectrum=models.TextField(null=True,blank=True)
    is_analyzed=models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.title} by {self.artist}"
    
    