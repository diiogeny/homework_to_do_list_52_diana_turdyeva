from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_task, name='add_task'),  # Новый маршрут
    path('', views.task_list, name='task_list'),   # Главная страница (список задач)
]

