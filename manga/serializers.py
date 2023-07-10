from rest_framework import serializers
from .models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = 'name'.split()


class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = 'image year title'.split()


class MangaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = 'image title type year genre synopsis'.split()

