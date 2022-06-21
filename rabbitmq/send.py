import pika

# создаем соединение к брокеру
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#создаем очередь
channel.queue_declare(queue='hello')

# задаем обмен, указываем очередь, задаем сообщение
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

# закрываем соединение
connection.close()