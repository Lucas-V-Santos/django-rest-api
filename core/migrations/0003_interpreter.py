# Generated by Django 4.0.4 on 2022-04-22 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_year_movie_released_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interpreter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('nationality', models.CharField(max_length=60)),
                ('birth_year', models.IntegerField()),
            ],
        ),
    ]
