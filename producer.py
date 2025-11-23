import pika

# Подключение к RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Объявляем очередь (если не существует), с durable=True
channel.queue_declare(queue='my_queue', durable=True)

# Отправляем несколько сообщений
messages = ["Hello from Python! Message 1", "Message 2", "Message 3"]
for msg in messages:
    channel.basic_publish(exchange='', routing_key='my_queue', body=msg)
    print(f"Sent: {msg}")

# Закрываем соединение
connection.close()