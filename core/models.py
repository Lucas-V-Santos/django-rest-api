from django.db import models


class Movie(models.Model):
    title = models.CharField(name='title', max_length=60)
    translated_title = models.CharField(name='translated_title', max_length=60)
    released_year = models.IntegerField(name='released_year')
    director = models.CharField(name='director', max_length=60)
    category = models.CharField(name='category', max_length=60)

    def __str__(self):
        return f'{self.title}, release in {self.released_year}, directed by {self.director}'


class Interpreter(models.Model):
    name = models.CharField(name='name', max_length=60)
    nationality = models.CharField(name='nationality', max_length=60)
    birth_year = models.IntegerField(name='birth_year')

    def __str__(self):
        return f'{self.name}, born in {self.nationality} in {self.birth_year}'
