# Generated by Django 4.1.7 on 2023-05-09 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_kategori_malzeme'),
    ]

    operations = [
        migrations.AddField(
            model_name='malzeme',
            name='malzeme_adet',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
