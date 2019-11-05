from channels.routing import ProtocolTypeRouter, URLRouter
import playlists.routing

application = ProtocolTypeRouter({
    'http': URLRouter(playlists.routing.urlpatterns),
})
