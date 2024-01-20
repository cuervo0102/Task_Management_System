import pika
from celery import shared_task, Celery
from time import sleep
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from .models import Task

app = Celery('main', broker='pyamqp://guest:guest@localhost//')

@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email_task():
    print('Starting send_email_task')
    sleep(10)
    print('After sleep')
    
    try:
        send_mail(
            'Celery mail worked',
            'this is proof the task works',
            'djangocelery2024@gmail.com',
            ['widey97189@regapts.com']
        )
        print('Email sent successfully')
    except Exception as e:
        print(f'Error sending email: {e}')

    return None


def send_notification_to_owner(task_id, status):
    task = Task.objects.get(id=task_id)

    task_owner = task.task_writer

    print(f'Sending notification to {task_owner.username}: Task status is now {new_status}')



@app.task
def process_messages(task_id, new_status):
    try:
        task = Task.objects.get(id=task_id)
        task.status = new_status
        task.save()

        send_notification_to_owner(task_id, new_status)

    except Exception as e:
        print(f'Error processing message: {e}')





        
if __name__ == '__main__':
    process_messages()