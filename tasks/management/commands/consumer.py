import pika 
from tasks.tasks import process_messages


def on_message_received(ch, method, properties, body):
    try:
        task_id, new_status = map(int, body.split())
        
        process_messages.delay(task_id, new_status)

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