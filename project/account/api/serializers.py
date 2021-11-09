from django.db.models import fields
from rest_framework import serializers
from account.models import PublicStatus

class PublicStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicStatus
        fields = '__all__'


