from django.urls import path
from .views import BlogPostList, BlogPostDetail, UserProfile, RegisterUser, LoginView

urlpatterns = [
    path('posts/', BlogPostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', BlogPostDetail.as_view(), name='post-detail'),
    path('profile/', UserProfile.as_view(), name='user-profile'),
    path('register/',RegisterUser.as_view(), name = 'register-user'),
    path('login/',LoginView.as_view(), name = 'login-user')
]