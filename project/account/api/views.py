from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from account.models import Profile,PublicStatus


class PublicStatusRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PublicStatusSerializer
    queryset = PublicStatus.objects.all()
    lookup_field = 'owner'
    permission_classes = [IsAuthenticated,]
