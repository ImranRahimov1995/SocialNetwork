from rest_framework import serializers
from friendship.models import FriendshipRequest



class FriendshipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendshipRequest
        fields = ('user_from',"user_to")

class FriendshipAcceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendshipRequest
        fields = '__all__'