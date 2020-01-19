from datetime import datetime

from mongoengine import EmbeddedDocument
from mongoengine.fields import *


class Price(EmbeddedDocument):

    modified = DateTimeField(default=datetime.utcnow)
