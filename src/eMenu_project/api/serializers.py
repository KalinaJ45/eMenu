from django.contrib.auth.models import User
from .models import Dish, Card
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer of User"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user


class DishSerializer(serializers.ModelSerializer):
    """Serializer of dish"""
    class Meta:
        model = Dish
        fields = ['id', 'user', 'name', 'description', 'price',
                  'preparation_time', 'created', 'updated', 'vegetarian', 'photo']


class CardSerializer(serializers.ModelSerializer):
    """Serializer of card menu"""
    dishes = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Card
        fields = ['id', 'user', 'name', 'description', 'dishes',
                  'created', 'updated']
