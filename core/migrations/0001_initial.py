# Generated by Django 4.0.4 on 2022-04-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('translated_title', models.CharField(max_length=60)),
                ('year', models.IntegerField()),
                ('director', models.CharField(max_length=60)),
                ('category', models.CharField(max_length=60)),
            ],
        ),
    ]
