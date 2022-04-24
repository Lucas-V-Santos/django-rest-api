from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from core.views import MovieViewSet, InterpreterViewSet

router = routers.DefaultRouter()
router.register(r'movies',MovieViewSet)
router.register(r'interpreters', InterpreterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]