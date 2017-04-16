from mongoengine import *
import datetime

# Create your models here.
class Artist(Document):
    name = StringField(max_length=50, required=True)
    location = StringField(max_length=50)

class Performance(Document):
    title = StringField(max_length=50, required=True)
    artists = ListField(ReferenceField(Artist))
    desc = StringField(max_length=500)
    date = DateTimeField(help_text='schedule date', default=datetime.datetime(2017,7,14))