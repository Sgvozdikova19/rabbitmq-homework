import pika

# Подключение к RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Объявляем очередь, с durable=True
channel.queue_declare(queue='my_queue', durable=True)

# Callback-функция для обработки сообщений
def callback(ch, method, properties, body):
    print(f"Received: {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)  # Подтверждаем обработку

# Начинаем слушать очередь
channel.basic_consume(queue='my_queue', on_message_callback=callback)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()