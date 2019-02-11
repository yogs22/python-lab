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

# users = User.select().where((User.name == 'yogi') | (User.name == 'novi'))

# for user in users:
# 	print(user.name + ' Memiliki ' + str(user.point) + ' Point \nbergabung pada', user.join_at)

users = User.select().where(User.name.contains('i'))
for user in users:
	print(user.name)