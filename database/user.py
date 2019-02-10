from peewee import *

sqlite_db = SqliteDatabase('user.db')

class User(Model):
	name = CharField()
	email = CharField()

	class Meta:
		database = sqlite_db

sqlite_db.connect()
sqlite_db.create_tables([User], safe = True)

# Insert data
# Insert one data

# user = User(name = 'Yogi Testing 2', email = 'yogi@example.com')
# user.save()

# print(user)

# Insert many data
fields = [User.name, User.email]
data   = [
			('Yogi Test 8', 'yogs@example1.com'),
			('Yogi Test 9', 'yogs@example2.com')
		]

User.insert_many(data, fields = fields).execute()