import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import realtime_analysis.routing  # Doğru modülü import edin

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catch_my_tune')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            realtime_analysis.routing.websocket_urlpatterns  
        )
    ),
})
