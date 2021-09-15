from django.contrib.auth import get_user_model
from django.test import TestCase
from . import models


class PostModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        user_obj = get_user_model().objects.create(
            username="mostafa",
            password="12345"
        )

        models.Post.objects.create(
            title="Linux",
            body="Linus",
            author=user_obj
        )
    
    def test_title_post(self):
        post_obj = models.Post.objects.get(id=1)
        self.assertEqual(post_obj.title, "Linux")
    
    def test_body_post(self):
        post_obj = models.Post.objects.get(id=1)
        self.assertEqual(post_obj.body, "Linus")
    
    def test_author_post(self):
        post_obj = models.Post.objects.get(id=1)
        self.assertEqual(post_obj.author.username, "mostafa")



