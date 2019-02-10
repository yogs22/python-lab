"""
# Object Oriented Programming
"""

class Player(object):
	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

	def getSkill(self):
		return 'normal'

class ArgentinaPlayer(Player):
	def __init__(self, name):
		super().__init__(name)
		print('Hellow argentina!')

	def getSkill(self):
		return 'cepat'

player = ArgentinaPlayer('Maradona')
print('Nama : ' + player.getName() + ', Skill : ' + player.getSkill())