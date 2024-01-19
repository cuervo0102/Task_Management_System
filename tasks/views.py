import logging
from django.shortcuts import render, redirect
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from .rabbitmq_configuration import producer
from .models import Task
from django.http import HttpResponse
from django.core.management import call_command
from .utils import generate_tracking_token
from .tasks import process_messages

logger = logging.getLogger(__name__)

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        try:
            if form.is_valid():
                task_writer = form.save(commit=False)
                task_writer.user = request.user
                task_writer.save()

                priority = task_writer.priority
                content = task_writer.title  
                producer(priority, content)

                return redirect('/tasks/')
        except Exception as e:
            logger.error(f"An error occurred: {e}")
        
    else:
        form = TaskForm()

    return render(request, 'task_templates/task.html', context={'form': form})




def index(request):
    processor_tasks = Task.objects.filter(processors=request.user)

    

    context = {
        'precessor': processor_tasks,
    }

    return render(request, 'task_templates/index.html', context)


def task_details(request, pk):
    task = Task.objects.get(id=pk)
    token = generate_tracking_token()
    url_with_tracking = f'/detail/{pk}/?token={token}'

   

    context = {
        'details': task,
        'url': url_with_tracking,
        'status': task.status,
    }

    if request.method == 'POST':
        status_ = request.POST.get('status')
        task.status = status_
        task.save()  
        context['status'] = status_  


    process_messages.delay(task.id, task.status)

    return render(request, 'task_templates/task_details.html', context)