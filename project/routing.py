from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.apps import apps
from a2wsgi import ASGIMiddleware
bokeh_app_config = apps.get_app_config('bokeh.server.django')

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(URLRouter(bokeh_app_config.routes.get_websocket_urlpatterns())),
    'http': AuthMiddlewareStack(URLRouter(bokeh_app_config.routes.get_http_urlpatterns())),
})

# app = ProtocolTypeRouter({
#     'websocket': AuthMiddlewareStack(URLRouter(bokeh_app_config.routes.get_websocket_urlpatterns())),
#     'http': AuthMiddlewareStack(URLRouter(bokeh_app_config.routes.get_http_urlpatterns())),
# })
# print('starting middlewhere')
# application = ASGIMiddleware(app)

