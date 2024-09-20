from django.shortcuts import render
from chatapi.serializers import (
    ChatHistorySerializer,
    ChatUserSerializer,
    MyTokenObtainPairSerializer,
    UserRegisterSerializer,
)
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from django.contrib.admin.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from chatapi.models import ChatUser, ChatHistory


class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserReisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class ChatUserView(CreateAPIView):
    queryset = ChatUser.objects.all()
    serializer_class = ChatUserSerializer


class GetChatUseView(ListAPIView):
    serializer_class = ChatUserSerializer

    def get_queryset(self):
        return ChatUser.objects.filter(sender_user=self.request.user)
