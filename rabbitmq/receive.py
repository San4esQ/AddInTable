import pika

# создаем соединение к брокеру
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# убеждаемся что очередь существует
channel.queue_declare(queue='hello')

# получаем сообщение из очереди
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# получение сообщения через callback из очереди
channel.basic_consume('hello',
                      callback,
                      no_ack=True)

# вводим цикл, который ожидает данные и запускает callback, когда это необходимо
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
