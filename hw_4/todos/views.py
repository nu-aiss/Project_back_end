from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList, Todo


def redirect_to_todo_lists(request):
    return redirect('todo_lists')


def todo_list_view(request):
    lists = TodoList.objects.all()
    return render(request, 'todos/todo_list.html', {'lists': lists})

def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    return render(request, 'todos/todo_list_detail.html', {'todo_list': todo_list})



def todo_detail_view(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todos = Todo.objects.filter(todo_list=todo_list)
    return render(request, 'todos/todo_detail.html', {'todo_list': todo_list, 'todos': todos})


def todo_list_delete(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todo_list.delete()
    return redirect('todo_lists')


def todo_list_edit(request, id):
    pass

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo_list_id = todo.todo_list.id
    todo.delete()
    return redirect('todo_detail', id=todo_list_id)

def todo_edit(request, id):
    pass
