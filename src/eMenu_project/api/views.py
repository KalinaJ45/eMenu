from django.contrib.auth.models import User
from .models import Dish, Card
from .serializers import UserSerializer, DishSerializer, CardSerializer
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import Count


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet of User"""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        if request.user == obj.user:
            return True


class DishViewSet(viewsets.ModelViewSet):
    """ViewSet of dish"""
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CardViewSet(viewsets.ModelViewSet):
    """ViewSet of card menu"""
    queryset = Card.objects.all()

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            queryset = Card.objects.all()

        else:
            queryset = Card.objects.filter(dishes__isnull=False).annotate(
                dishes_count=Count('dishes'))

        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    serializer_class = CardSerializer
    filterset_fields = ['name', 'created', 'updated']
    filter_backends = [filters.OrderingFilter]
    filter_backends = [DjangoFilterBackend]
    ordering_fields = ['name', 'dishes_count']
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post'])
    def join_dish(self, request, **kwargs):
        card = self.get_object()
        dish = Dish.objects.get(id=request.data['dish'])
        card.dishes.add(dish)

        serializer = CardSerializer(card, many=False)
        return Response(serializer.data)
