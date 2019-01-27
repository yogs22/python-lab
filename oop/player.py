"""
# Object Oriented Programming
"""

class Player(object):
	name = ''
	speed = ''

	def __init__(self, name, speed):
		self.name = name
		self.speed = speed

	def getName(self):
		return self.name

	def getSpeed(self):
		return self.speed 

player = Player('Maradona', '200')
print('Nama pemainku adalah ' + player.getName() + ' Kecepatanku ' + str(player.getSpeed()))