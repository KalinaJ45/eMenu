from rest_framework.test import APITestCase, APIClient
import json
from rest_framework import status
from django.contrib.auth.models import User
from .models import Dish, Card
from django.contrib.auth import get_user_model
import pytest


class DishAPITestCase(APITestCase):

    def setUp(self) -> None:

        user = get_user_model().objects.create_superuser(username="admintest",
                                                         email="admintest@admintest.com", password="admintest")
        self.user = User.objects.get(username='admintest')
        self.client = APIClient()
        self. client.force_authenticate(user=self.user)
        self.dish = Dish.objects.create(
            user=self.user,
            name='testdish',
            description='testdishdescription',
            price=50,
            preparation_time=60,
            vegetarian=False
        )

    def test_create(self):
        initial_dishes_count = Dish.objects.count()
        dish_attrs = {
            'user': self.user.id,
            'name': 'testdish2',
            'description': 'testdishdescription2',
            'price': 100,
            'preparation_time': 120,
            'vegetarian': False
        }
        data = json.dumps(dish_attrs)
        response = self.client.post(
            "/api/dishes/",
            data=data, content_type="application/json"
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert Dish.objects.count() == initial_dishes_count + 1

    def test_list(self):
        response = self.client.get('/api/dishes/')
        assert response.status_code == status.HTTP_200_OK

    def test_detail(self):
        response = self.client.get(
            '/api/dishes/{}/'.format(self.dish.id))
        assert response.status_code == status.HTTP_200_OK

    def test_update(self):
        data = {'user': self.user.id,
                'name': 'testdish3',
                'description': 'testdishdescription3',
                'price': 200,
                'preparation_time': 180,
                'vegetarian': True}
        data = json.dumps(data)
        response = self.client.put(
            '/api/dishes/{}/'.format(self.dish.id),
            data=data, content_type="application/json"
        )
        assert response.status_code == status.HTTP_200_OK
        updated = Dish.objects.get(id=self.dish.id)
        assert updated.name == 'testdish3'

    def test_partial_update(self):
        response = self.client.patch(
            '/api/dishes/{}/'.format(self.dish.id),
            data={"name": "testdish4"}
        )
        assert response.status_code == status.HTTP_200_OK
        partial_updated = Dish.objects.get(id=self.dish.id)
        assert partial_updated.name == 'testdish4'

    def test_delete(self):
        initial_dishes_count = Dish.objects.count()
        response = self.client.delete(
            '/api/dishes/{}/'.format(self.dish.id))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Dish.objects.count() == initial_dishes_count - 1
        pytest.raises(Dish.DoesNotExist,
                      Dish.objects.get, id=self.dish.id)


class CardAPITestCase(APITestCase):

    def setUp(self) -> None:

        user = get_user_model().objects.create_superuser(username="admintest",
                                                         email="admintest@admintest.com", password="admintest")
        self.user = User.objects.get(username='admintest')
        self.client = APIClient()
        self. client.force_authenticate(user=self.user)
        self.card = Card.objects.create(
            user=self.user,
            name='testcard',
            description='testcardescription',

        )

    def test_create(self):
        initial_cards_count = Card.objects.count()
        card_attrs = {
            'user': self.user.id,
            'name': 'testcard2',
            'description': 'testcarddescription2',
        }
        data = json.dumps(card_attrs)
        response = self.client.post(
            "/api/cards/",
            data=data, content_type="application/json"
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert Card.objects.count() == initial_cards_count + 1

    def test_list(self):
        response = self.client.get('/api/cards/')
        assert response.status_code == status.HTTP_200_OK

    def test_detail(self):
        response = self.client.get(
            '/api/cards/{}/'.format(self.card.id))
        assert response.status_code == status.HTTP_200_OK

    def test_update(self):
        data = {'user': self.user.id,
                'name': 'testcard3',
                'description': 'testcarddescription3',
                }
        data = json.dumps(data)
        response = self.client.put(
            '/api/cards/{}/'.format(self.card.id),
            data=data, content_type="application/json"
        )
        assert response.status_code == status.HTTP_200_OK
        updated = Card.objects.get(id=self.card.id)
        assert updated.name == 'testcard3'

    def test_partial_update(self):
        response = self.client.patch(
            '/api/cards/{}/'.format(self.card.id),
            data={"name": "testcard4"}
        )
        assert response.status_code == status.HTTP_200_OK
        partial_updated = Card.objects.get(id=self.card.id)
        assert partial_updated.name == 'testcard4'

    def test_delete(self):
        initial_cards_count = Card.objects.count()
        response = self.client.delete(
            '/api/cards/{}/'.format(self.card.id))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Card.objects.count() == initial_cards_count - 1
        pytest.raises(Card.DoesNotExist,
                      Card.objects.get, id=self.card.id)


class UserAPITestCase(APITestCase):

    def setUp(self) -> None:

        user = get_user_model().objects.create_superuser(username="admintest",
                                                         email="admintest@admintest.com", password="admintest")
        self.user = User.objects.get(username='admintest')
        self.client = APIClient()
        self. client.force_authenticate(user=self.user)

    def test_create(self):
        initial_users_count = User.objects.count()
        card_attrs = {
            'username': 'usertest',
            'email': 'usertest@admintest.com',
            'password': 'usertest',
        }
        data = json.dumps(card_attrs)
        response = self.client.post(
            "/api/users/",
            data=data, content_type="application/json"
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.count() == initial_users_count + 1

    def test_list(self):
        response = self.client.get('/api/users/')
        assert response.status_code == status.HTTP_200_OK

    def test_detail(self):
        response = self.client.get(
            '/api/users/{}/'.format(self.user.id))
        assert response.status_code == status.HTTP_200_OK

    def test_update(self):
        data = {'username': 'usertest2',
                'email': 'usertest2@admintest.com',
                'password': 'usertest2',
                }
        data = json.dumps(data)
        response = self.client.put(
            '/api/users/{}/'.format(self.user.id),
            data=data, content_type="application/json"
        )
        assert response.status_code == status.HTTP_200_OK
        updated = User.objects.get(id=self.user.id)
        assert updated.username == 'usertest2'

    def test_partial_update(self):
        response = self.client.patch(
            '/api/users/{}/'.format(self.user.id),
            data={"username": "usertest3"}
        )
        assert response.status_code == status.HTTP_200_OK
        partial_updated = User.objects.get(id=self.user.id)
        assert partial_updated.username == 'usertest3'

    def test_delete(self):
        initial_users_count = User.objects.count()
        response = self.client.delete(
            '/api/users/{}/'.format(self.user.id))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert User.objects.count() == initial_users_count - 1
        pytest.raises(User.DoesNotExist,
                      User.objects.get, id=self.user.id)
