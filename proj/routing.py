from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from myapp.consumers import EchoConsumer
application=ProtocolTypeRouter({
    'websocket':URLRouter([
        path('ws/socket/',EchoConsumer())
    ])
})