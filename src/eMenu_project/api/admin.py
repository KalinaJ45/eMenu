from django.contrib import admin
from .models import Dish, Card


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):

    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    ordering = ['name']

    queryset = Dish.objects.all()


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):

    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    ordering = ['name']

    queryset = Card.objects.all()
