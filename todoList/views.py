from django.shortcuts import render, redirect
from .models import TodoList


def index(request):

    if request.method == 'POST':
        task = TodoList.objects.create(content=request.POST['content'])
        task.save()
        return redirect('todoList:index')
    else:
        context = TodoList.objects.all()
        return render(request, 'todoList/index.html', {'context': context})


def delete(request, id):

    task = TodoList.objects.get(id=id)
    task.delete()
    return redirect('todoList:index')


def update(request, id):
    task = TodoList.objects.get(id=id)

    if request.method == 'POST':
        task.content = request.POST['content']
        task.save()
        return redirect('todoList:index')

    else:
        return render(request, 'todoList/update.html', {'task': task})

