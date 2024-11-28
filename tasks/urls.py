from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),               # Список задач
    path('<int:pk>/', views.task_detail, name='task_detail'),  # Детальная информация о задаче
]
