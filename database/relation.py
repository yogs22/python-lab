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

# query = Tweet.select().join(User).where(User.username == 'yogi')
# for tweet in query:
# 	print(tweet.message)

noviTweet = User.get(User.username == 'novi')
for tweet in noviTweet.tweets:
	print(noviTweet.username + ' - ' + tweet.message + '\n' + str(tweet.created_at))