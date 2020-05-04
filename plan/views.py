from django.shortcuts import render
from . import models
from rest_framework import generics
from .serializers import ToDoSerializer, ProfileSerializer, UserSerializer, ThemeSerializer
from django.contrib.auth.models import User
from .permissions import AnybodyIsAble

from rest_framework.response import Response
from django.http import HttpResponse


# Visual side

def home(request):
    # return render(request, 'index.html', {})
    return HttpResponse('This is homepage')

# API side


class ToDoAPIView(generics.ListCreateAPIView):
    queryset = models.ToDo.objects.all()
    serializer_class = ToDoSerializer

    def get(self, request, format=None):
        ToDos = models.ToDo.objects.filter(author=request.user.id)
        serializer = ToDoSerializer(ToDos, many=True)
        return Response(serializer.data)


class ToDoDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.ToDo.objects.all()
    serializer_class = ToDoSerializer

    def get(self, request, pk, format=None):
        ToDos = models.ToDo.objects.filter(author=request.user.id)
        filtered = ToDos.filter(id=pk)
        serializer = ToDoSerializer(filtered, many=True)
        return Response(serializer.data)


class ProfileAPIView(generics.ListCreateAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request, format=None):
        Profile = models.Profile.objects.filter(username=request.user.id)
        serializer = ProfileSerializer(Profile, many=True)
        return Response(serializer.data)


class ProfileDetailAPIView(generics.ListCreateAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request, pk, format=None):
        Profile = models.Profile.objects.filter(username=request.user.id)
        filtered = Profile.filter(id=pk)
        serializer = ProfileSerializer(filtered, many=True)
        return Response(serializer.data)


class ThemeAPIView(generics.ListCreateAPIView):
    queryset = models.Theme.objects.all()
    serializer_class = ThemeSerializer

    def get(self, request, pk, format=None):
        Theme = models.Theme.objects.filter(username=request.user.id)
        serializer = ThemeSerializer(Theme, many=True)
        return Response(serializer.data)


class ThemeDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.Theme.objects.all()
    serializer_class = ThemeSerializer

    def get(self, request, format=None):
        Theme = models.Theme.objects.filter(username=request.user.id)
        serializer = ThemeSerializer(Theme, many=True)
        return Response(serializer.data)


class UserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AnybodyIsAble,)
