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

#delete_instance
user = User.get(User.id == 4)
user.delete_instance()