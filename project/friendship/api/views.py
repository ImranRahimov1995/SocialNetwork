from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from friendship.models import FriendshipRequest
from account.models import Profile
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


class FriendshipRequestCreateView(generics.CreateAPIView):
    serializer_class = FriendshipRequestSerializer
    queryset = FriendshipRequest.objects.all()
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        
        data = serializer.validated_data
        # print(serializer.validated_data)
        check_same_record = FriendshipRequest.objects.filter(
                                                    user_from=data['user_to'],
                                                    user_to=data['user_from'])

        if data['user_from'] == data['user_to']:
            raise ValidationError('You cannot send friendship  to myself')

        if check_same_record:
            raise ValidationError('You have already have friendship ')
        else:
            return super().perform_create(serializer)


class FriendshipRequestRetrieveView(
                    generics.RetrieveUpdateDestroyAPIView):

    serializer_class = FriendshipAcceptSerializer
    queryset = FriendshipRequest.objects.all()
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated,]