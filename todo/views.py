from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
from .forms import TodoForm


def inicio(request):
    todos = Todo.objects.filter(titulo__contains=request.GET.get('buscar', ''))

    return render(request, 'todo/inicio.html', {'todos': todos})


def vista(request, id):
    todo = Todo.objects.get(id=id)

    return render(request, 'todo/vista.html', {'todo': todo})


def editar(request, id):
    todo = Todo.objects.get(id=id)

    if request.method == 'GET':
        formulario = TodoForm(instance=todo)

        return render(request, 'todo/editar.html', {'formulario': formulario, 'id': id})

    if request.method == 'POST':
        formulario = TodoForm(request.POST, instance=todo)

        if formulario.is_valid():
            formulario.save()

        messages.success(request, '¡Tarea actualizada con exito!')

        return render(request, 'todo/editar.html', {'formulario': formulario, 'id': id})


def crear(request):
    if request.method == 'GET':
        formulario = TodoForm()

        return render(request, 'todo/crear.html', {'formulario': formulario})

    if request.method == 'POST':
        formulario = TodoForm(request.POST)

        if formulario.is_valid():
            formulario.save()

        return redirect('todo')


def borrar(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()

    return redirect('todo')
