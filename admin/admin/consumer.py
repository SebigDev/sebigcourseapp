import pika, json

params = pika.URLParameters('amqps://jwglapwm:PErkym2axsuCUZRfC6ziBvH0YBdlEtoM@roedeer.rmq.cloudamqp.com/jwglapwm')

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body=None):
    if body is not None:
        print('Message received')
        #data = json.loads(body)
        if properties.content_type == 'user_created':
            print('user ', body)
        elif properties.content_type == 'product_created':
            print('product created ', body)
        elif properties.content_type == 'product_updated':
            print('product updated ', body)
    else:
        print('Listening for message...')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consuming...')

channel.start_consuming()

channel.close()