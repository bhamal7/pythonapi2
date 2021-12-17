from django.db import models
from django.db.models import fields
from .models import Hero
from rest_framework import serializers


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name','age','gender')