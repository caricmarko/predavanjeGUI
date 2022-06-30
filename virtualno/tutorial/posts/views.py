from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from posts.serializers import PostSerializer
from posts.models import Post
from django.contrib.auth.models import User # dodato
from posts.serializers import UserSerializer # dodato
from rest_framework import permissions # dodato
from posts.permissions import IsOwnerOrReadOnly # dodato
from rest_framework.decorators import api_view # dodato za navigaciju
from rest_framework.reverse import reverse # dodato za navigaciju

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format)
    })

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
