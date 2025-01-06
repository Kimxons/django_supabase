from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from .services.supabase_service import SupabaseService

supabase_service = SupabaseService()

def todo_list(request):
    try:
        todos = supabase_service.fetch_todos()
        return render(request, 'myapp/todo_list.html', {'todos': todos})
    except ConnectionError as e:
        messages.error(request, str(e))
        return render(request, 'myapp/todo_list.html', {'todos': []})

def add_todo(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        try:
            supabase_service.create_todo(task)
            messages.success(request, 'Todo created successfully!')
        except ValidationError as e:
            messages.error(request, str(e))
        except ConnectionError as e:
            messages.error(request, str(e))
    return redirect('todo_list')

def update_todo(request, todo_id):
    if request.method == 'POST':
        try:
            task = request.POST.get('task')
            if not task:
                raise ValidationError("Task cannot be empty")
            completed = 'completed' in request.POST
            data = {
                'task': task,
                'completed': completed
            }
            supabase_service.update_todo(todo_id, data)
            messages.success(request, 'Todo updated successfully!')
        except (ValidationError, ConnectionError) as e:
            messages.error(request, str(e))
    return redirect('todo_list')

def delete_todo(request, todo_id):
    if request.method == 'POST':
        try:
            supabase_service.delete_todo(todo_id)
            messages.success(request, 'Todo deleted successfully!')
        except ConnectionError as e:
            messages.error(request, str(e))
    return redirect('todo_list')