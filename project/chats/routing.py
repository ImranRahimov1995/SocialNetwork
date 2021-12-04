from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('chat/<pk>/', consumers.ChatsConsumer.as_asgi())
]