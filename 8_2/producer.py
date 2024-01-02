import pika
from mongoengine import connect, Document, StringField, BooleanField
from faker import Faker

connect('contacts_db', host='mongodb://localhost:27017/contacts_db')

class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    is_message_sent = BooleanField(default=False)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue')

fake = Faker()
for _ in range(5):
    contact = Contact(
        full_name=fake.name(),
        email=fake.email()
    )
    contact.save()


    channel.basic_publish(
        exchange='',
        routing_key='email_queue',
        body=str(contact.id)
    )

    print(f"Message sent to the queue for contact: {contact.full_name}")

connection.close()