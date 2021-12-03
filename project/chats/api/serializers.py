from rest_framework import serializers

from chats.models import Chat,Message
from account.models import Profile
from django.contrib.auth.models import User


class MessageSerializers(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    recipient = serializers.StringRelatedField()
    created_at = serializers.DateTimeField('%Y:%m:%d %H:%M')

    class Meta:
        model = Message
        fields = ('author','recipient','chat','body','created_at')

class RecipientField(serializers.RelatedField):
    def to_representation(self,value):
        user = User.objects.get(name=value)
        value = Profile.objects.get(user=user)
        return value

class CreateMessageSerializers(serializers.ModelSerializer):
    recipient = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields ="__all__"

    def create(self,validated_data):
        recipient = self.context['request'].data['recipient']
        validated_data['recipient']=Profile.objects.filter(user__username=recipient)[0]
        return super().create(validated_data)
