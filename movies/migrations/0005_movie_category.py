# Generated by Django 4.1.7 on 2023-04-19 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_defter_movie_kisilik_movie_vakit'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='movies.category'),
        ),
    ]
