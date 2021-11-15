from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from friendship.models import FriendshipRequest


class FriendshipRequestCreateView(generics.CreateAPIView):
    serializer_class = FriendshipRequestSerializer
    queryset = FriendshipRequest.objects.all()
    permission_classes = [IsAuthenticated,]
