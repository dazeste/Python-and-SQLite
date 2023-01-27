from time import sleep
from readSongs import read
from addSongs import insertSongs
from updateSongs import update
from deleteSongs import delete

def menuOptions(): # Function? Subroutine?
	menuUI = \
	"""
	Welcome to Music Database v1.00

	Please Select an Option Below:
		1. Display songs in the Database
		2. Add a new song to the Database
		3. Update an existing song
		4. Delete an existing song
		5. Exit Application

	"""
	options = ["1", "2", "3", "4", "5"]
	choice = 0
	while choice not in options:
		print(menuUI)
		choice = input("Enter Select an option from the menu: ")
		if choice not in options:
			print(choice, "is not a valid option, try again.")
			sleep(1)
	return choice
	

mainProgram = True
while mainProgram:
	userChoice = menuOptions() # Choice is stored in userChoice
	if userChoice == "1":
		read()
	elif userChoice == "2":
		insertSongs()
	elif userChoice == "3":
		update()
	elif userChoice == "4":
		delete()
	else:
		mainProgram = False

input("Press Enter to Exit the Application.")
# Finished