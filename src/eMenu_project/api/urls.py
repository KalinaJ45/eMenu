from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'dishes', views.DishViewSet, basename='dishes')
router.register(r'cards', views.CardViewSet, basename='cards')

urlpatterns = [
    path('', include(router.urls))
]
