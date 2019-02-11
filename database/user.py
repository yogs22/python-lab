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

users = User.select().order_by(User.point.desc())

for user in users:
	print(user.name + ' Memiliki ' + str(user.point) + ' Point \nbergabung pada', user.join_at)

# def get_rand():
# 	return random.randint(1,20)

# data = [
# 	{'name': 'hilman', 'point': get_rand()},
# 	{'name': 'yogi', 'point': get_rand()},
# 	{'name': 'novi', 'point': get_rand()},
# 	{'name': 'aldy', 'point': get_rand()},
# ]

# User.insert_many(data).execute()