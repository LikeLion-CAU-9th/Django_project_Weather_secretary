from django.contrib import admin
from django.urls import path
import outfit.views

urlpatterns = [
    path('', outfit.views.outfit, name="outfit"),
]