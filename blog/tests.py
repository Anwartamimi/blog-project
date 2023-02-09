from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@tester.com',
            password = 'password',
        )

        self.post = Post.objects.create(
            title = 'new test post',
            body = 'the post body ...',
            author = self.user,
        )