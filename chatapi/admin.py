from django.contrib import admin
from chatapi.models import ChatHistory, ChatUser


# Register your models here.
@admin.register(ChatUser)
class ChatUsers(admin.ModelAdmin):
    list_display = ["id", "sender_user", "receiver_user"]


@admin.register(ChatHistory)
class ChatHistorys(admin.ModelAdmin):
    list_display = ["id", "chat_user", "chat"]
