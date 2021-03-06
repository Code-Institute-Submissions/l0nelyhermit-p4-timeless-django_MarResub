# Generated by Django 3.1.7 on 2021-03-18 13:24

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch_brand', models.CharField(choices=[('Rolex', 'Rolex'), ('Omega', 'Omega'), ('Patek Philippe', 'Patek Philippe')], default='Rolex', max_length=20)),
                ('watch_model', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=255)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Sold', 'Sold')], default='Available', max_length=10)),
                ('cover', cloudinary.models.CloudinaryField(max_length=255)),
            ],
        ),
    ]
