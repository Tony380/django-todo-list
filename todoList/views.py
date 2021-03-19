from django.shortcuts import render, redirect
from .models import TodoList


def index(request):
    return render(request, 'index')

