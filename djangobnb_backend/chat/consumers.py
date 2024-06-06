import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import ConversationMessage


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    # Leave room
    async def disconnect(self):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message
    async def receive(self, text_data):
        data = json.loads(text_data)

        conversation_id = data["data"]["conversation_id"]
        sent_to_id = data["data"]["sent_to_id"]
        name = data["data"]["name"]
        body = data["data"]["body"]

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "body": body, "name": name}
        )

        await self.save_message(conversation_id, body, sent_to_id)
