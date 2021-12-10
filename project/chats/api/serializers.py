from rest_framework import serializers
from django.contrib.auth.models import User

from chats.models import Chat, Message
from account.models import Profile


class MessageSerializers(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    recipient = serializers.StringRelatedField()
    created_at = serializers.DateTimeField('%Y:%m:%d %H:%M')

    class Meta:
        model = Message
        fields = ('author', 'recipient', 'chat', 'body', 'created_at')


class CreateMessageSerializers(serializers.ModelSerializer):
    recipient = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = "__all__"

    def create(self, validated_data):
        recipient = self.context['request'].data['recipient']
        profile = Profile.objects.filter(user__username=recipient)[0]
        validated_data['recipient'] = profile
        return super().create(validated_data)
