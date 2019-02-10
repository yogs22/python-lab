"""
# Object Oriented Programming
"""

class Player(object):
	job = 'Pemain sepak bola'

	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

	@staticmethod
	def retiredIn(age):
		return str(40 - age)

	@classmethod
	def getInfo(cls, age):
		return cls.job + ' akan penisun pada ' + cls.retiredIn(20) + ' tahun'

print(Player.getInfo(30))