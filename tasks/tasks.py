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
    def on_message_received(ch, method, properties, body):
        try:
            task = Task.objects.get(id=task_id)
            
            task.status = new_status
            task.save()

            send_notification_to_owner(task_id, new_status)

        except Exception as e:
            print(f'Error processing message: {e}')

    connection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_parameters)

    channel = connection.channel()

    channel.queue_declare(queue='test')

    channel.basic_consume(queue='test', auto_ack=True, on_message_callback=on_message_received)

    print('Start Consuming')

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print('Stopping the consumer')
        channel.stop_consuming()

    connection.close()

if __name__ == '__main__':
    process_messages()