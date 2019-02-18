from peewee import *
import random, datetime

sqlite_db = SqliteDatabase('user.db')

class User(Model):
	name    = CharField()
	point   = IntegerField()
	join_at = DateTimeField(default=datetime.datetime.now) 

	class Meta:
		database = sqlite_db

sqlite_db.connect()
sqlite_db.create_tables([User], safe = True)

user = User.select().where(User.name == 'yogi prasetyawan').get()
user.name = 'yogi'

User.update(point = 100).where(User.name == 'novi').execute()