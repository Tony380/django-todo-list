from django.test import TestCase
from .models import TodoList


class Tests(TestCase):

    def setUp(self):
        TodoList.objects.create(content='Do the dishes')
    
    def test_model(self):
        obj = TodoList.objects.get(id=1)
        self.assertEqual(str(obj), 'Do the dishes')
