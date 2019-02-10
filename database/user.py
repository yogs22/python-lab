from peewee import *

sqlite_db = SqliteDatabase('user.db')

class User(Model):
	name = CharField()
	email = CharField()

	class Meta:
		database = sqlite_db

sqlite_db.connect()
sqlite_db.create_tables([User])