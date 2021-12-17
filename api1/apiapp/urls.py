from django.contrib import admin
from django.urls import path,include
from .views import HeroView

urlpatterns = [
    path('gethero/',HeroView.as_view())
]
