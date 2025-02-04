from django.urls import path
from .views import post_list, post_detail, create_post, delete_post

urlpatterns = [
    path('posts/', post_list, name='post_list'),
    path('posts/<int:id>', post_detail, name='post_detail'),
    path('posts/create/', create_post, name='create_post'),
    path('posts/<int:id>/delete/', delete_post, name='delete_post')
]
