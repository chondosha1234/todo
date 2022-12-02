from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('complete/<id>', views.complete, name='complete'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_task/', views.delete_task, name='delete_task'),
    path('edit_task/', views.edit_task, name='edit_task'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
]
