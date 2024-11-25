from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
def add_task(request):
    if request.method == 'POST':
        description = request.POST['description']
        status = request.POST['status']
        due_date = request.POST.get('due_date')

        Task.objects.create(description=description, status=status, due_date=due_date)
        return redirect('task_list')

    return render(request, 'tasks/add_task.html')
