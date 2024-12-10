from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/analysis/<str:song_id>', consumers.AnalysisConsumer.as_asgi()),
]
