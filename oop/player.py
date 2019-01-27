"""
# Object Oriented Programming
"""

class Player(object):
	def __init__(self, name, speed):
		self.name = name
		self.speed = speed

	def getName(self):
		return self.name

	def getSpeed(self):
		return self.speed 

class ArgentinaPlayer(Player):
	def setAge(self, age):
		self.age = age 
		return self.age
		
player = ArgentinaPlayer('Maradona', '200')
print('Nama : ' + player.getName() + ' \nKecepatan ' + player.getSpeed() + ' \nUsia : ' + player.setAge('12'))