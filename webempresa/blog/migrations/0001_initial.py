# Generated by Django 4.1.6 on 2023-03-12 01:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'categoría',
                'verbose_name_plural': 'categorías',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('content', models.TextField(default='a completar', verbose_name='Contenido')),
                ('published', models.DateTimeField(default=datetime.datetime(2023, 3, 12, 1, 45, 27, 210208, tzinfo=datetime.timezone.utc), verbose_name='fecha publicacion')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('categories', models.ManyToManyField(to='blog.category', verbose_name='Categorías')),
            ],
            options={
                'verbose_name': 'Posteo',
                'verbose_name_plural': 'Posteos',
                'ordering': ['-created'],
            },
        ),
    ]
