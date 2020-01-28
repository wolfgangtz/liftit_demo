from django.urls import re_path

from invoices import websocket

websocket_urlpatterns = [
    re_path(r'ws/(?P<session_name>\w+)/$', websocket.FrontendConsumer),
]