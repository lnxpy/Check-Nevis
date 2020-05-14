from django.shortcuts import render
from . import models
from rest_framework import generics
from .serializers import ToDoSerializer, ProfileSerializer, UserSerializer, ThemeSerializer
from django.contrib.auth.models import User
from .permissions import AnybodyIsAble

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Visual side

def home(request):
    return render(request, 'index.html', {})


# API side


class UserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = models.User.objects.all()
    permission_classes = (AnybodyIsAble,)


class ToDoAPIView(generics.ListCreateAPIView):
    serializer_class = (ToDoSerializer)
    queryset = models.ToDo.objects.all()

    def get(self, request, format=None):
        user_profile = models.Profile.objects.get(username=request.user.id)
        todo_items = models.ToDo.objects.filter(author=user_profile.id)
        serializer = ToDoSerializer(todo_items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data.copy()

        user_profile = models.Profile.objects.get(username=request.user.id)
        data['author'] = user_profile.id

        serializer = ToDoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = (ToDoSerializer)
    queryset = models.ToDo.objects.all()

    def get_object(self, pk, username):
        try:
            return models.ToDo.objects.get(pk=pk, author=username)
        except models.ToDo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_profile = models.Profile.objects.get(username=request.user.id)
        todo_item = models.ToDo.objects.filter(id=pk, author=user_profile.id)
        serializer = ToDoSerializer(todo_item, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user_profile = models.Profile.objects.get(username=request.user.id)
        todo_item = self.get_object(pk, user_profile.id)
        data = request.data.copy()
        data['author'] = user_profile.id
        serializer = ToDoSerializer(todo_item, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user_profile = models.Profile.objects.get(username=request.user.id)
        todo_item = self.get_object(pk, user_profile.id)
        todo_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = (ProfileSerializer)
    queryset = models.Profile.objects.all()

    def get_object(self, username):
        try:
            return models.Profile.objects.get(username=username)
        except models.Profile.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        profile = models.Profile.objects.filter(username=request.user.id)
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        profile = self.get_object(request.user.id)
        data = request.data.copy()
        data['username'] = request.user.id
        serializer = ProfileSerializer(profile, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ThemeAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = (ThemeSerializer)
    queryset = models.Theme.objects.all()

    def get_object(self, username):
        try:
            return models.Theme.objects.get(username=username)
        except models.Theme.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        user_profile = models.Profile.objects.get(username=request.user.id)
        theme = models.Theme.objects.filter(username=user_profile.id)
        serializer = ThemeSerializer(theme, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        user_profile = models.Profile.objects.get(username=request.user.id)
        theme = self.get_object(user_profile.id)
        data = request.data.copy()
        data['username'] = user_profile.id
        serializer = ThemeSerializer(theme, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
