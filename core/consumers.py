# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import Conversation, Message
from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer


class ChatConsumer(JsonWebsocketConsumer):
    """
    This consumer is used to show user's online status,
    and send notifications.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None

    def connect(self):
        print("Connected!")
        self.room_name = "home"
        self.accept()
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name,
        )
        self.send_json(
            {
                "type": "welcome_message",
                "message": "Hey there! You've successfully connected!",
            }
        )

    def disconnect(self, code):
        print("Disconnected!")
        return super().disconnect(code)

    def receive_json(self, content, **kwargs):
        message_type = content["type"]
        if message_type == "chat_message":
            async_to_sync(self.channel_layer.group_send)(
                self.room_name,
                {
                    "type": "chat_message_echo",
                    "name": content["name"],
                    "message": content["message"],
                },
            )
        return super().receive_json(content, **kwargs)

    def chat_message_echo(self, event):
        print(event)
        self.send_json(event)


# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.user = self.scope["user"]
#         if self.user.is_anonymous:
#             await self.close()
#         else:
#             self.room_group_name = f"chat_{self.user.username}"
#             await self.channel_layer.group_add(
#                 self.room_group_name,
#                 self.channel_name
#             )
#             await self.accept()
#
#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )
#
#     async def receive(self, text_data):
#         message = json.loads(text_data)
#         content = message['content']
#         recipient_username = message['recipient']
#
#         recipient = await self.get_user(recipient_username)
#         if not recipient:
#             return
#
#         sender_username = self.user.username
#         sender = self.user
#
#         conversation = await self.get_conversation(sender, recipient)
#         if not conversation:
#             conversation = await self.create_conversation(sender, recipient)
#
#         message = await self.create_message(conversation, sender, content)
#         data = {
#             'type': 'new_message',
#             'id': message.id,
#             'sender': sender_username,
#             'recipient': recipient_username,
#             'content': content,
#             'timestamp': str(message.timestamp),
#         }
#
#         await self.channel_layer.group_send(
#             conversation.room_name,
#             {
#                 'type': 'chat_message',
#                 'data': data,
#             }
#         )
#
#     async def chat_message(self, event):
#         await self.send(text_data=json.dumps(event['data']))
#
#     @staticmethod
#     async def get_user(username):
#         try:
#             return User.objects.get(username=username)
#         except User.DoesNotExist:
#             return None
#
#     @staticmethod
#     async def get_conversation(user1, user2):
#         try:
#             return Conversation.objects.get(users=user1).filter(users=user2).first()
#         except Conversation.DoesNotExist:
#             return None
#
#     @staticmethod
#     async def create_conversation(user1, user2):
#         conversation = Conversation.objects.create()
#         conversation.users.add(user1, user2)
#         conversation.room_name = f"chat_{conversation.id}"
#         await conversation.save()
#         return conversation
#
#     @staticmethod
#     async def create_message(conversation, sender, content):
#         return Message.objects.create(conversation=conversation, sender=sender, content=content)
