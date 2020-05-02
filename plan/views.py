from django.shortcuts import render
from . import models
from rest_framework import generics
from .serializers import ToDoSerializer, ProfileSerializer, UserSerializer, ThemeSerializer
from django.contrib.auth.models import User

from django.http import HttpResponse


# Visual side

def home(request):
    # return render(request, 'index.html', {})
    return HttpResponse('This is homepage')

# API side


class ToDoAPIView(generics.ListCreateAPIView):
    queryset = models.ToDo.objects.all()
    serializer_class = ToDoSerializer


class ProfileAPIView(generics.ListCreateAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = ProfileSerializer


class ThemeAPIView(generics.ListCreateAPIView):
    queryset = models.Theme.objects.all()
    serializer_class = ThemeSerializer


class UserAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
