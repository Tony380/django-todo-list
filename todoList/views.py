from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from .models import TodoList


class Index(ListView):

    model = TodoList
    template_name = 'todoList/index.html'


class CreateTask(CreateView):

    model = TodoList
    fields = ['content']
    success_url = '/'


class DeleteTask(DeleteView):

    model = TodoList
    success_url = reverse_lazy('todoList:index')


class UpdateTask(UpdateView):

    model = TodoList
    template_name = 'todoList/update.html'
    fields = ['content']
    success_url = reverse_lazy('todoList:index')