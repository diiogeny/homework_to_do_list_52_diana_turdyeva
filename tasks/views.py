from django.shortcuts import render, redirect
from .models import Task
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')

        Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            status='new',
        )

        return redirect('task_list')

    return render(request, 'tasks/add_task.html')
