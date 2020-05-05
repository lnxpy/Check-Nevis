from django.shortcuts import render
from . import models
from rest_framework import generics
from .serializers import ToDoSerializer, ProfileSerializer, UserSerializer, ThemeSerializer
from django.contrib.auth.models import User
from .permissions import AnybodyIsAble

from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse


# Visual side

def home(request):
    # return render(request, 'index.html', {})
    return HttpResponse('This is homepage')

# API side


class UserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = models.User.objects.all()
    permission_classes = (AnybodyIsAble,)


class ToDoAPIView(generics.RetrieveUpdateAPIView):
    pass


class ToDoDetailAPIView(generics.RetrieveUpdateAPIView):
    pass


class ProfileAPIView(generics.RetrieveUpdateAPIView):
    pass


class ThemeAPIView(generics.RetrieveUpdateAPIView):
    pass
