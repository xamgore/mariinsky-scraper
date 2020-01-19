from mongoengine import Document
from mongoengine.fields import *


class User(Document):
    _id = StringField(required=True)
    first_name = StringField()
    last_name = StringField()
    username = StringField()
    photo_url = URLField()
    auth_date = DateTimeField(required=True)
    hash = StringField()
