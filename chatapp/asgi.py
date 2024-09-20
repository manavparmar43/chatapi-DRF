import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

# import chatapi.routing  # Import after setup to ensure apps are loaded
from chatapi import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatapp.settings")

# Ensure apps are loaded before continuing
django.setup()

django_asgi_app = get_asgi_application()
application = ProtocolTypeRouter(
    {"http": django_asgi_app, "websocket": URLRouter(routing.websocket_urlpatterns)}
)
