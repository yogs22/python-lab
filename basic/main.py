"""
Local Global Var
"""
name = input("Nama monster ?")
monster = {"name": name, "power": 100}

def startGame():
	choice = input("Pilih Menu: 1. Makan, 2. Lihat Status, 3. Keluar")
	if choice == "1":
		goEat()
	elif choice == "2":
		goStatus()
	else:
		print("Goodbye !")

def goEat():
	global monster
	print("Makan makan ..")
	monster['power'] += 100
	print("Power monster bertambah 100 : ", monster['power'])
	startGame()

def goStatus():
	print("Checking ...")
	print("Name : ", monster['name'])
	print("Power : ", monster['power'])
	startGame()

def goExit():
	print("Goodbye")

startGame()