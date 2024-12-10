import logging
from channels.generic.websocket import AsyncWebsocketConsumer
import json

# Logger 
logger = logging.getLogger(__name__)

class AnalysisConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.song_id = self.scope["url_route"]["kwargs"]["song_id"]
        self.group_name = f"song_{self.song_id}"

        try:
            # add group and accept 
            await self.channel_layer.group_add(
                self.group_name,
                self.channel_name,
            )
            await self.accept()
            logger.info(f"WebSocket connected: {self.group_name}")
        except Exception as e:
            logger.error(f"WebSocket connection error: {e}")
            await self.close()

    async def disconnect(self, close_code):
        try:
            
            await self.channel_layer.group_discard(
                self.group_name,
                self.channel_name,
            )
            logger.info(f"WebSocket disconnected: {self.group_name}")
        except Exception as e:
            logger.error(f"WebSocket disconnection error: {e}")

    async def send_analysis_update(self, event):
        try:
            await self.send(text_data=json.dumps(event))
            logger.info(f"WebSocket message sent to {self.group_name}: {event}")
        except Exception as e:
            logger.error(f"Error sending WebSocket message: {e}")
