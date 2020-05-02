from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('api/todo', views.ToDoAPIView.as_view(), name='todo'),
    path('api/profile', views.ProfileAPIView.as_view(), name='profile'),
    path('api/theme', views.ThemeAPIView.as_view(), name='theme'),
    path('api/user', views.UserAPIView.as_view(), name='user'),

    path('api/login', include('rest_framework.urls')),
    path('api/', include('rest_auth.urls')),
]
