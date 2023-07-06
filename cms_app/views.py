from rest_framework import generics, permissions
from .models import User, Post, Like
from .serializers import UserSerializer, PostSerializer, LikeSerializer

class CreateUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ReadUpdateDeleteUserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreatePostAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ReadUpdateDeletePostAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

class CreateLikeAPIView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class ReadUpdateDeleteLikeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer