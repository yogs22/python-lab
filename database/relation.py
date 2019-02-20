import datetime
from peewee import *

sqlite_db = SqliteDatabase('tweet.db')

class BaseModel(Model):
	class Meta():
		database = sqlite_db

class User(BaseModel):
	username = CharField(unique = True)

class Tweet(BaseModel):
	user = ForeignKeyField(User, backref = 'tweets')
	message = TextField()
	created_at = DateTimeField(default = datetime.datetime.now)

sqlite_db.create_tables([User, Tweet])

data = (
	('hilman', ('halo tweet', 'ini tweet pertama')),
	('yogi', ('halo bro', 'selamat makan')),
	('novi', ('halo kang', 'ini tweet pertama')),
)

for username, tweets in data:
	user = User.create(username = username)
	for tweet in tweets:
		Tweet.create(user = user, message = tweet)