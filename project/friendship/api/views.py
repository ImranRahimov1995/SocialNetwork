from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from friendship.models import FriendshipRequest
from account.models import Profile
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from friendship.models import Friends

class FriendshipRequestCreateView(generics.CreateAPIView):
    serializer_class = FriendshipRequestSerializer
    queryset = FriendshipRequest.objects.all()
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):

        data = serializer.validated_data
        # print(serializer.validated_data)
        check_same_record = FriendshipRequest.objects.filter(
            user_from=data['user_to'],
            user_to=data['user_from'],
        )

        if data['user_from'] == data['user_to']:
            raise ValidationError(
                'You cannot send friendship  to myself'
            )

        if check_same_record:
            raise ValidationError(
                'You have already have friendship'
            )
        else:
            try:
                super().perform_create(serializer)
            except ValidationError:
                return ValidationError('check models settings')


class FriendshipRequestRetrieveView(
    generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FriendshipAcceptSerializer
    queryset = FriendshipRequest.objects.all()
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, ]

    def delete(self, request, pk):
        fr = FriendshipRequest.objects.get(pk=pk)

        check_one = Friends.objects.filter(
            user1=fr.user_from,
            user2=fr.user_to,
        )
        check_second = Friends.objects.filter(
            user1=fr.user_to,
            user2=fr.user_from,
        )
        print(check_one)
        print(check_second)
        if check_one:
            check_one[0].delete()
        if check_second:
            check_second[0].delete()

        super().delete(pk)
        return Response('ok')
