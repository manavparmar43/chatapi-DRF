from django.db import models
from django.contrib.auth.models import User


class ChatUser(models.Model):
    sender_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_chats"
    )
    receiver_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_chats"
    )
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.receiver_user.first_name


class ChatHistory(models.Model):
    chat_user = models.ForeignKey(
        ChatUser, on_delete=models.CASCADE, related_name="chat_user"
    )
    chat = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"{self.chat_user.sender_user.first_name}-"
            f"{self.chat_user.receiver_user.first_name}"
        )
