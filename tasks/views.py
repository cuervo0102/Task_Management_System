import logging 
import pika 
from django.shortcuts import render, redirect
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from .tasks import sleepy, send_email_task
from django.http import HttpResponse

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task_writer = form.save(commit=False)
            task_writer.user = request.user
            task_writer.save()
            return redirect('/tasks/')
        
    else :
        form = TaskForm()

    return render(request, 'task_templates/task.html', context={'form':form})



def index(request):
    connection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    channel.queue_declare(queue='test')
    message = 'Django test done'
    channel.basic_publish(exchange='', routing_key='test', body=message)
    print(f'sent message: {message}')
    connection.close()
    return HttpResponse('The email has been sent!')


