# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, permissions
from .models import BlogPost, Profile
from .serializers import BlogPostSerializer, ProfileSerializer, UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class RegisterUser(APIView):
    '''write code here'''

class LoginView(ObtainAuthToken):
    '''write code here'''


class UserProfile(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

class BlogPostList(generics.ListCreateAPIView):
    '''write code here'''

class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    '''write code here'''

