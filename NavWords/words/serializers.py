from rest_framework import serializers
from .models import WordList


class WordListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordList
        fields = ('name', 'user')
