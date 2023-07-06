from django.urls import path
from .views import CreateUserAPIView, ReadUpdateDeleteUserAPIView, CreatePostAPIView, ReadUpdateDeletePostAPIView, CreateLikeAPIView, ReadUpdateDeleteLikeAPIView

urlpatterns = [
    path('users/', CreateUserAPIView.as_view(), name='create_user'),
    path('users/<int:pk>/', ReadUpdateDeleteUserAPIView.as_view(), name='read_update_delete_user'),
    path('posts/', CreatePostAPIView.as_view(), name='create_post'),
    path('posts/<int:pk>/', ReadUpdateDeletePostAPIView.as_view(), name='read_update_delete_post'),
    path('likes/', CreateLikeAPIView.as_view(), name='create_like'),
    path('likes/<int:pk>/', ReadUpdateDeleteLikeAPIView.as_view(), name='read_update_delete_like'),
]