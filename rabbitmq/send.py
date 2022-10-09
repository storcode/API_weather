import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='connection_db', durable=True)
channel.basic_publish(
    exchange='',
    routing_key='connection_db',
    body='conn_db_dwn_json',
    properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)   # очередь задач не потеряется при перезапуске кролика
    )
print("Sent message")
connection.close()