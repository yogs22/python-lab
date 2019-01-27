"""
# Object Oriented Programming
"""

class Player(object):
	name = 'Maradona'

	def getPlayer(self, arg = name):
		self.name = arg
		return self.name

player = Player()
print(player.getPlayer('Wow'))
