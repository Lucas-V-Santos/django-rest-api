# Generated by Django 4.0.4 on 2022-04-18 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='year',
            new_name='released_year',
        ),
    ]