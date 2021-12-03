from rest_framework import generics
from .serializers import *

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,BasicAuthentication


from chats.models import Chat,Message

class ChatApiView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    serializer_class = MessageSerializers


    def get_queryset(self):
        chat= Chat.objects.get(pk=self.kwargs['pk'])
        return Message.objects.filter(chat=chat).order_by('-created_at')


class CreateMessageView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    serializer_class = CreateMessageSerializers
    queryset = Message.objects.all()



