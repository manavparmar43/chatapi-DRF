from channels.generic.websocket import AsyncJsonWebsocketConsumer
from chatapi.models import ChatHistory, ChatUser
from chatapi.serializers import ChatHistorySerializer
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async


class AsyncConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        print("connect success")
        await self.accept()

    async def receive_json(self, content, **kwargs):
        sender_id = content.get("sender_id")
        receiver_id = content.get("receiver_id")
        message = content.get("message")

        if sender_id and receiver_id and message:
            await self.save_chat(sender_id, receiver_id, message)
            response = await self.serialize_chat(sender_id, receiver_id)
            await self.send_json(response)

    async def disconnect(self, code):
        await self.close()

    @sync_to_async
    def save_chat(self, sender_id, receiver_id, message):
        sender = User.objects.get(id=sender_id)
        receiver = User.objects.get(id=receiver_id)
        chat_user, _ = ChatUser.objects.get_or_create(
            sender_user=sender, receiver_user=receiver
        )
        ChatHistory.objects.create(chat_user=chat_user, chat=message)

    @sync_to_async
    def serialize_chat(self, sender_id, receiver_id):
        sender = User.objects.get(id=sender_id)
        receiver = User.objects.get(id=receiver_id)
        chat_user = ChatUser.objects.get(sender_user=sender, receiver_user=receiver)
        chat_history = ChatHistory.objects.filter(chat_user=chat_user).last()
        serializer = ChatHistorySerializer(chat_history)
        return serializer.data
