import pika 

def producer():
    connection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    channel.queue_declare(queue='test')
    message = 'Django test done'
    channel.basic_publish(exchange='', routing_key='test', body=message)
    print(f'sent message: {message}')
    connection.close()
    return None