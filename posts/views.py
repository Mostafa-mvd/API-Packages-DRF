from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets
from . import models, serializers, permissions as posts_permissions


#---------------------------------------------APIViews---------------------------------------------

class PostList(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        posts_permissions.IsAuthorOrReadOnly,
        )
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer


#---------------------------------------------ViewSets---------------------------------------------


class PostViewSets(viewsets.ModelViewSet):
    permission_classes = (
        posts_permissions.IsAuthorOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly,
    )
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class UserViewSets(viewsets.ModelViewSet):
    permission_classes = (
        posts_permissions.IsRealUser,
    )
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
