from django.test import TestCase
from django.urls import reverse
from .models import TodoList
from .views import index, update, delete


class Tests(TestCase):

    def setUp(self):
        TodoList.objects.create(content='Do the dishes')
    
    def test_model(self):
        obj = TodoList.objects.get(id=1)
        self.assertEqual(str(obj), 'Do the dishes')
    
    def test_index_post_view(self):
        obj = TodoList.objects.create(content='Cook')
        response = self.client.post(reverse('todoList:index'), data={'content':{obj.content:'Cook'}})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_index_get_view(self):
        response = self.client.get(reverse('todoList:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todoList/index.html')

    def test_update_view(self):
        id = TodoList.objects.first().id
        response = self.client.get(reverse('todoList:update', args=[id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todoList/update.html')

    def test_update_post_view(self):
        obj = TodoList.objects.get(id=1)
        obj.content = 'Test'
        obj.save()
        response = self.client.post(reverse('todoList:update', args=[obj.id]), data={'content':{obj.content:'Test'}})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
    
    def test_delete_view(self):
        id = TodoList.objects.first().id
        response = self.client.get(reverse('todoList:delete', args=[id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
