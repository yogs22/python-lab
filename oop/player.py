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

	def getSkill(self):
		return 'normal'

class ArgentinaPlayer(Player):
	def getSkill(self):
		return 'cepat'

class BrazilPlayer(Player):
	def getSkill(self):
		return 'samba'

class MalaysiaPlayer(Player):
	pass
		
		
player = ArgentinaPlayer('Maradona', '200')
print('Nama : ' + player.getName() + ', Skill : ' + player.getSkill())

player2 = MalaysiaPlayer('Sultan', '200')
print('Nama : ' + str(player2.getName()) + ', Skill : ' + str(player2.getSkill()))