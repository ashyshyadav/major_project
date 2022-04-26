from channels.auth import AuthMidllewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing


application = ProtocolTypeRouter({
    'websocket':AuthMidllewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})