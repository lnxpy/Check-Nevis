from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('api/todo/', views.ToDoAPIView.as_view(), name='todo'),
    path('api/todo/<int:pk>/', views.ToDoDetailAPIView.as_view(), name='todo_detail'),

    path('api/profile/', views.ProfileAPIView.as_view(), name='profile'),
    path('api/profile/<int:pk>/',
         views.ProfileDetailAPIView.as_view(), name='profile_detail'),

    path('api/theme/', views.ThemeAPIView.as_view(), name='theme'),
    path('api/theme/<int:pk>/',
         views.ThemeDetailAPIView.as_view(), name='theme_detail'),

    path('api/user/', views.UserAPIView.as_view(), name='user'),
    path('api/login/', include('rest_framework.urls')),
    path('api/', include('rest_auth.urls')),
]
