from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Post, User

class PostAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')
        self.post = Post.objects.create(author=self.user, title="Test Post", content="Test content")
        self.posts_url = reverse('post-list')

    def test_get_posts(self):
        response = self.client.get(self.posts_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_post_summary(self):
        summary_url = reverse('post-summary')
        response = self.client.get(summary_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        if response.data:
            self.assertIn('id', response.data[0])
            self.assertIn('title', response.data[0])
            self.assertIn('comment_count', response.data[0])
