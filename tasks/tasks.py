from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.core.mail import EmailMessage
 

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