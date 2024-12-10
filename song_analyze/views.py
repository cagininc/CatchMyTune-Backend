# from django.shortcuts import get_object_or_404
# from django.http import JsonResponse
# from .models import Song
# import numpy as np


# def check_analysis(request, song_id):

#     song = get_object_or_404(Song, id=song_id)

#     if song.is_analyzed:
#         # return analyze data planned
#         return JsonResponse(
#             {
#                 "message": "Song analyzed succesfuly",
#                 "song_id": song.id,
#                 "title": song.title,
#                 "tempo": song.tempo,
#                 "key": song.key,
#                 "spectrum": song.spectrum,
#                 "danceability":song.danceability
#             }
#         )

#     else:
#         #if analyze is still in progress or not started yet
#         return JsonResponse({'message':'Song analyze in progress','song_id':song.id},status=202)