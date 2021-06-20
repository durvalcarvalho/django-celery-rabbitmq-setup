import pika, sys, os

def callback(ch, method, properties, body):
    print(f"Received a new message: {body}")

def main():

    credentials = pika.PlainCredentials('admin', 'admin')

    connection_parameters = pika.ConnectionParameters(
        host="rabbitmq-service",
        port=5672,
        credentials=credentials,
    )

    connection = pika.BlockingConnection(connection_parameters)

    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_consume(
        queue='hello',
        on_message_callback=callback,
        auto_ack=True,
    )

    print("Waiting for messages. To exit press CTRL+C")

    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")

        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
