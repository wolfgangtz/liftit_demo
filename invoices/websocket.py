from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync
import json

class FrontendConsumer(JsonWebsocketConsumer):


    def connect(self):
        self.ws_session_name = self.scope['url_route']['kwargs']['session_name']
        self.room_custom_name = 'ws_%s' % self.ws_session_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_custom_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        print("Closed websocket with code: ", close_code)
        async_to_sync(self.channel_layer.group_discard)(
            self.room_custom_name,
            self.channel_name
        )
        self.close()


    def send_response(self, event):
        self.send_json(
            {
                'type': 'send.response',
                'content': event['content']
            }
        )