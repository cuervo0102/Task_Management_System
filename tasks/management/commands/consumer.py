# from django.core.management.base import BaseCommand
# import pika

# class Command(BaseCommand):
#     help = 'Consume messages from RabbitMQ queue'

#     def handle(self, *args, **options):
#         def on_message_received(ch, method, properties, body):
#             try:
#                 self.stdout.write(self.style.SUCCESS(f'Received new message: {body}'))
#             except Exception as e:
#                 self.stderr.write(self.style.ERROR(f'Error processing message: {e}'))

#         connection_parameters = pika.ConnectionParameters('localhost')
#         connection = pika.BlockingConnection(connection_parameters)

#         # channel = connection.channel()

#         channel.queue_declare(queue='test')

#         channel.basic_consume(queue='test', auto_ack=True, on_message_callback=on_message_received)

#         self.stdout.write(self.style.SUCCESS('Start Consuming'))

#         try:
#             channel.start_consuming()
#         except KeyboardInterrupt:
#             self.stdout.write(self.style.SUCCESS('Stopping the consumer'))

#         connection.close()
