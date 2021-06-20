import pika

credentials = pika.PlainCredentials('admin', 'admin')

connection_parameters = pika.ConnectionParameters(
    host="0.0.0.0",
    port=5672,
    credentials=credentials,
)

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='hello')

for i in range(100):

    channel.basic_publish(
        exchange='',
        routing_key='hello',
        body=f'Hello World N {i}!'
    )

    from time import sleep
    sleep(1)

connection.close()