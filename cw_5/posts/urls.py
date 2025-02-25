from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('authenticate/', views.authenticate_user, name='authenticate'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.posts_view, name='posts'),
    path('my/', views.my_posts_view, name='my_posts'),
    path('<int:id>/', views.post_detail_view, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('<int:id>/delete/', views.delete_post, name='delete_post'),
]
