from django.contrib import admin
from django.urls import path
import place.views

urlpatterns = [
    path('', place.views.w_place , name='w_place'),
]
