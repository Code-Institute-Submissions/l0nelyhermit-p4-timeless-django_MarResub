# Generated by Django 3.1.7 on 2021-03-18 16:02

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watches', '0002_watch_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch',
            name='cover',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='watch_brand',
            field=models.CharField(choices=[('Rolex', 'Rolex'), ('Omega', 'Omega'), ('Patek Philippe', 'Patek Philippe')], default='Rolex', max_length=30),
        ),
        migrations.AlterField(
            model_name='watch',
            name='watch_model',
            field=models.CharField(max_length=50),
        ),
    ]
