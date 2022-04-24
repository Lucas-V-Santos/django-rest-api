from django.contrib import admin
from core.models import Movie, Interpreter


class Movies(admin.ModelAdmin):
    list_display = ('title', 'translated_title', 'released_year', 'director', 'category')


class Interpreters(admin.ModelAdmin):
    list_display = ('name', 'nationality', 'birth_year')


admin.site.register(Movie, Movies)
admin.site.register(Interpreter, Interpreters)