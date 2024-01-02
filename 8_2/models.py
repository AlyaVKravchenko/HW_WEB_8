from mongoengine import Document, StringField, BooleanField
from mongoengine import connect

connect('myhw8', host='mongodb+srv://alyavkravchenko:TryNewPass@cluster0.rxysigp.mongodb.net/myhw8?retryWrites=true&w=majority')

class Contact(Document):
    fullname = StringField(required=True, max_length=255)
    email = StringField(required=True, max_length=255)
    message_sent = BooleanField(default=False)

    meta = {
        'collection': 'contacts'
    }