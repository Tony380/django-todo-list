from django.urls import path
from .views import index, delete, update


urlpatterns = [
    path('', index, name='index'),
    path('delete/<int:id>', delete, name='delete'),
    path('update/<int:id>', update, name='update'),
]

app_name = 'todoList'