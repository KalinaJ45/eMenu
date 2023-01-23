from django.db import models
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Dish(models.Model):
    """Model of dish"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True)
    name = models.CharField(_('Nazwa'), max_length=32, unique=True)
    description = models.TextField(_('Opis'), max_length=256)
    price = models.DecimalField(_('Cena'), max_digits=5, decimal_places=2)
    preparation_time = models.PositiveIntegerField(_('Czas przygotowania'))
    created = models.DateField(_('Data dodania'), auto_now_add=True)
    updated = models.DateField(_('Data aktualizacji'), auto_now=True)
    vegetarian = models.BooleanField(_('Danie wegetariańskie'))
    photo = models.ImageField(_('Zdjęcie'), null=True,
                              blank=True, upload_to='photos/%Y/%m/%d')

    def __str__(self):
        return self.name


class Card(models.Model):
    """Model of card menu"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True)
    name = models.CharField(_('Nazwa'), max_length=32, unique=True)
    description = models.TextField(_('Opis'), max_length=256)
    dishes = models.ManyToManyField(Dish, null=True,
                                    blank=True)
    created = models.DateField(_('Data dodania'), auto_now_add=True)
    updated = models.DateField(_('Data aktualizacji'), auto_now=True)

    def __str__(self):
        return self.name
