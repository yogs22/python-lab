"""
File python
"""

file = open('data.txt', 'a+')

""" 
	Return the choice 
"""

def choiceAction():
	choice = input('Pilih Menu \n 1. Buat List \n 2. Lihat List \n 3. Exit \n >> ')
	if choice == '1':
		askData()
	elif choice == '2':
		checkData()
	elif choice == '3':
		exitAction()
	else:
		print('Pilihan tidak ada ! \n')
		choiceAction()

"""
	Chocie 1
"""

def addData(text):
	file.write('\n' + text)
	askData()

def askData():
	askInput = input("(exit) untuk keluar \n Mau Makan Apa ? ")
	if askInput == 'exit':
		choiceAction()
	else:
		addData(askInput)

"""
	Choice 2
"""

def checkData():
	global file

	file.seek(0)
	print(file.read())
	print('\n')

	choiceAction()

"""
	Choice 3
"""

def exitAction():
	print('Selamat tinggal ^_^')

choiceAction()
