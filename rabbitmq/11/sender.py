import pika

credentials = pika.PlainCredentials('guest' , 'guest')
connection = pika.BaseConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))
ch = connection.channel()

ch.exchange_declare('he' , exchange_type='headers')
message = 'hello world'
ch.basic_publish(exchange='he' ,routing_key='' , body=message , properties=pika.BasicProperties(
    headers={'name' : 'mongard'}))

print('sent')

connection.close()

# no need for queue -> we are definding specefic roles like headers , so we dont need to specify queue here (reciever needs)
