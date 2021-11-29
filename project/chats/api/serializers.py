from rest_framework import serializers

from chats.models import Chat,Message
from account.models import Profile



class MessageSerializers(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    recipient = serializers.StringRelatedField()
    created_at = serializers.DateTimeField('%Y:%m:%d %H:%M')

    class Meta:
        model = Message
        fields = ('author','recipient','chat','body','created_at')