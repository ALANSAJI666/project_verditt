
from django.urls import re_path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from .consumers import ChatConsumer


application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            re_path(r'ws/chat/$', ChatConsumer.as_asgi()),
        ])
    ),
})