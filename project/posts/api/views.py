from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from posts.models import Post


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated,]



class PostRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated,]