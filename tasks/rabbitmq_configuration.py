import pika

def producer(priority, content):
    connection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    
    channel.queue_declare(queue='test')
    
    channel.basic_publish(
        exchange='',
        routing_key=priority, 
        body=content,
        properties=pika.BasicProperties(
            headers={'priority': priority}
        )
    )
    
    print(f'Sent message: {content} with priority: {priority}')
    
    connection.close()
    return None
