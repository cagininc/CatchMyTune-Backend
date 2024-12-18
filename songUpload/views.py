from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # for test only!!
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Song
from django.utils import timezone
from song_analyze.tasks import analyze_song_task

@csrf_exempt

def upload_song(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        
        # Add time stamp
        file_name = f"{int(timezone.now().timestamp())}_{file.name}"
        
        # Save locally if you want
        # saved_file_name = default_storage.save(file_name, ContentFile(file.read()))
        
        #save as a song model
        song_instance= Song(
            title=file.name,
            audio_file=file,
            upload_date=timezone.now(),
        )
        song_instance.save() #
            
            
          #song_ıd control
        print(f"Saved Song ID: {song_instance.id}")
  
            
        #Start analyze process after saving the song
        analyze_song_task.delay(song_instance.id)#celery 
            
       
        return JsonResponse({'message': "File uploaded successfully", "file_name": file.name,"song_id":song_instance.id})

    # error message 
    return JsonResponse({'error': "No file uploaded or incorrect request method"}, status=400)
