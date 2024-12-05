from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        labels = {
            'title': 'Название задачи',
            'description': 'Описание задачи',
        }
