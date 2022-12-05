from datetime import datetime

from mongoengine import Document, connect, StringField, ListField, EmailField, DateField, DateTimeField, BooleanField

DB = 'mongo_db_assist'
HOST = 'localhost'
PORT = 27017

connect(DB, host=HOST, port=PORT)


class Contact(Document):
    first_name = StringField(max_length=50, required=True)
    last_name = StringField(max_length=50, required=True)
    phone = ListField(StringField(unique=True, required=True))
    email = ListField(EmailField(unique=True, default=None))
    address = StringField(max_length=100, default=None)
    birthday = DateField(default=None)
    favorite = BooleanField(default=False)
    created_at = DateField(default=datetime.now())

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


