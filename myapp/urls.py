from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_list, name='todo_list'),
    path('add-todo/', views.add_todo, name='add_todo'),
    path('update-todo/<str:todo_id>/', views.update_todo, name='update_todo'),
    path('delete-todo/<str:todo_id>/', views.delete_todo, name='delete_todo'),
]