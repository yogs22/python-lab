"""
File python
"""

file = open('data.txt', 'a+')

def addData(text):
	file.write('\n' + text)
	askData()

def askData():
	addData(input("Mau makan apa ? "))

askData()