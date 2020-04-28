from django.contrib import admin
from .models import Profile, ToDo, Theme
from django.contrib.admin import AdminSite
from django.http import HttpResponse


admin.site.register(Profile)
admin.site.register(ToDo)
admin.site.register(Theme)
