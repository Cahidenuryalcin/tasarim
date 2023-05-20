# Generated by Django 4.1.7 on 2023-05-09 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_alter_movie_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Malzeme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malzeme_adi', models.CharField(max_length=200)),
                ('malzeme_resim', models.CharField(max_length=100)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.kategori')),
            ],
        ),
    ]
