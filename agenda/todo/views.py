from django.shortcuts import render, redirect
from django.contrib import messages

from todo.forms import TodoForm
from .models import Todo

def index(request):
    todos = Todo.objects.filter(title__contains=request.GET.get('search',''))
    context = {
        'todos' : todos
    }
    return render(request, 'todo/index.html', {})
    
def create(request):
    if request.method == 'GET':
        form = TodoForm()
        context = {
            'form': form
        }
        return render(request, 'todo/create.html', context)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('todo')
    
def view(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'todo/detail.html', context)

def edit(request, id):
    todo = Todo.objects.get(id = id)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        context = {
            'form': form,
            'id' : id
        }
        return render(request, 'todo/edit.html', context)
    
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'id' : id
        }
        messages.success(request, "Tarea actualizada")
        return render(request, 'todo/edit.html', context)
    

def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    redirect('todo')
