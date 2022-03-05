
import pika, json

params = pika.URLParameters('amqps://jwglapwm:PErkym2axsuCUZRfC6ziBvH0YBdlEtoM@roedeer.rmq.cloudamqp.com/jwglapwm')

connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    json_body = json.dumps(body)
    channel.basic_publish(exchange='', routing_key='admin', body=json_body, properties=properties)
