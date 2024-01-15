from django.core.management.base import BaseCommand
import pika

class Command(BaseCommand):
    help = 'Consume messages from RabbitMQ queue'

    def handle(self, *args, **options):
        def on_message_recieved(ch, method, properties, body):
            print(f'Received new message: {body}')

        connection_parameters = pika.ConnectionParameters('localhost')
        connection = pika.BlockingConnection(connection_parameters)

        channel = connection.channel()

        channel.queue_declare(queue='test')
        

        channel.basic_consume(queue='test', auto_ack=True, 
                              on_message_callback=on_message_recieved)

        print('Start Consuming')

        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            print('Stopping the consumer')

        connection.close()
