# Generated by Django 4.1.5 on 2023-01-23 08:18

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
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Nazwa')),
                ('description', models.TextField(max_length=256, verbose_name='Opis')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cena')),
                ('preparation_time', models.PositiveIntegerField(verbose_name='Czas przygotowania')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Data dodania')),
                ('updated', models.DateField(auto_now=True, verbose_name='Data aktualizacji')),
                ('vegetarian', models.BooleanField(verbose_name='Danie wegetariańskie')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Zdjęcie')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Nazwa')),
                ('description', models.TextField(max_length=256, verbose_name='Opis')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Data dodania')),
                ('updated', models.DateField(auto_now=True, verbose_name='Data aktualizacji')),
                ('dishes', models.ManyToManyField(blank=True, null=True, to='api.dish')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
