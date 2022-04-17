from django.urls import path
from .views import index, task_list, task_update, task_create

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', task_list, name='task-list'),
    path('tasks/<int:month>/', task_list, name='task-list'),
    path('task/<int:pk>/', task_update, name='task-update'),
    path('task/create/', task_create, name='task-create'),

]