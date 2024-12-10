from rest_framework.test import APITestCase
from rest_framework import status

from sections.models import Section, SectionContent
from users.tests.utils import get_admin_user

class ContentTestCase(APITestCase):
    def setUp(self) -> None:
        self.admin_user = get_admin_user()
        response = self.client.post('/user/token/', {"email": 'tester@test1.com', "password": 'qwerty'})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_section = Section.objects.create(
            title='test_section',
            description='test_description'
        )
        self.test_content = SectionContent.objects.create(
            section=self.test_section,
            title='test_content_title',
            content='test_content_content'
        )

    def test_content_create(self):
        data = {
            'section': 1,
            'title': 'test_content_create',
            'content': 'test_content_description_create',
        }
        response = self.client.post('/content/create/', data=data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SectionContent.objects.count(), 2)

    def test_content_delete(self):
        response = self.client.delete(f'/content/3/delete/')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_content_detail(self):
        response = self.client.get(f'/content/4/')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], 'test_content_title')
        self.assertEqual(response.json()['content'], 'test_content_content')
        self.assertEqual(self.test_content.__str__(), 'test_content_title')

    def test_content_list(self):
        response = self.client.get('/content/list/')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['title'], 'test_content_title')

    def test_content_update(self):
        data = {
            'section':5,
            'title': 'test_content_put',
            'content': 'test_content_description_put',
        }
        response = self.client.put( '/content/6/update/', data=data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['section'], 5)
        self.assertEqual(response.json()['title'], 'test_content_put')
        self.assertEqual(response.json()['content'], 'test_content_description_put')
