from django.contrib import admin
from django.urls import path
from django import views
from pwned.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name=home),
]