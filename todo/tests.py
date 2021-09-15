from django.test import TestCase
from . import models


class TodoModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        models.Todo.objects.create(
            id=1,
            title="See Movie",
            body="Who am i?"
        )
    
    def test_title_obj(self):
        todo_obj = models.Todo.objects.get(id=1)
        self.assertEqual(todo_obj.title, "See Movie")
    
    def test_body_obj(self):
        todo_obj = models.Todo.objects.get(id=1)
        self.assertEqual(todo_obj.body, "Who am i?")

