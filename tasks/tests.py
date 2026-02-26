from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Task
from django.utils import timezone
from datetime import timedelta


class TaskAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.token = Token.objects.create(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )

        self.task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='Test Description',
            deadline=timezone.now() + timedelta(days=2),
            priority='medium'
        )

    def test_create_task(self):
        url = reverse('task-list')
        data = {
            'title': 'New Task',
            'description': 'New Description',
            'deadline': timezone.now() + timedelta(days=3),
            'priority': 'high'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_get_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_update_task(self):
        url = reverse('task-detail', args=[self.task.id])
        data = {
            'title': 'Updated Task',
            'description': 'Updated Description',
            'deadline': timezone.now() + timedelta(days=5),
            'priority': 'low',
            'status': 'completed'
        }

        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')

    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

class UserRegistrationTest(APITestCase):

    def test_user_registration(self):
        url = reverse('register')
        data = {
            'username': 'newuser',
            'email': 'newuser@test.com',
            'password': 'newpassword123'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)