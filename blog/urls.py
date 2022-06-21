from django.urls import path
from .views import index, addTodo, complete_todo, delete_complete, delete_all

urlpatterns = [
    path('', index, name='index'),
    path('add', addTodo, name='add'),
    path('complete/<todo_id>', complete_todo, name='complete'),
    path('delete_complete', delete_complete, name='delete_complete'),
    path('delete_all', delete_all, name='delete_all')
]
