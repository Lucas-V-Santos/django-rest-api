import requests
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from rest_framework import viewsets
from core.models import Movie, Interpreter
from core.serializer import MovieSerializer, InterpreterSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    # queryset = Movie.objects.filter(released_year=2016)
    serializer_class = MovieSerializer


class InterpreterViewSet(viewsets.ModelViewSet):
    queryset = Interpreter.objects.all()
    serializer_class = InterpreterSerializer
