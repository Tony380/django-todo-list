from django.urls import path
from .views import Index, CreateTask, DeleteTask, UpdateTask


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('add', CreateTask.as_view(), name='create'),
    path('delete/<int:pk>', DeleteTask.as_view(), name='delete'),
    path('update/<int:pk>', UpdateTask.as_view(), name='update'),
]

app_name = 'todoList'