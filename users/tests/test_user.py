from http.client import responses

from rest_framework.test import APITestCase
from rest_framework import status

from users.tests.utils import get_admin_user


class UserTestCase(APITestCase):
    """(Тесты для модели Users, 2 опции:
    1) ОБЩИЙ для запуска тестов из терминала
    2) ЛОКАЛЬНЫЙ для запуска тестов только в этом файле)
    """
    def setUp(self) -> None:
        # Базовые настройки
        self.admin_user = get_admin_user()
        response = self.client.post('/user/token/', {"email":'tester@test1.com', "password":'qwerty'})
        self.access_token = response.json.get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
    """
    если вы хотите запустить ЛОКАЛЬНЫЙ тест только для этого файла
    """

    def test_user_create(self):
        data = {
            "email": "tester_create@test.com",
            "role": 'member',
            "password": 'drftestweb320',
        }
        response = self.client.post('/user/create/', data, format='json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['email'], 'tester_create@test.com')

    def test_users_delete(self):
        response = self.client.post('/users/3/delete')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_users_detail(self):
        response = self.client.get('/users/4/')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], 'tester@test_1.com')
        self.assertEqual(response.json()['is_active'],True)

    def test_users_list(self):
        response = self.client.get('/users/')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['email'], 'tester@test_1.com')

    def test_user_update(self):
        data = {
            "email": "tester_update@test.com",
            "password": 'qwerty',

        }
        response = self.client.patch('/users/5/update/', data=data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], "tester_update@test.com")

