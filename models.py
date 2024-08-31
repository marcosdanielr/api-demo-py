from peewee import *

db = SqliteDatabase('animals.db')

class Animals(Model):
    name = CharField()
    age = IntegerField()

    class Meta:
        database = db