from rest_framework import serializers
from core.models import Movie, Interpreter


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'translated_title', 'released_year', 'director', 'category']


class InterpreterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interpreter
        fields = ['name', 'nationality', 'birth_year']