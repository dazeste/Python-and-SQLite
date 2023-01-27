from connect import *
from readSongs import read
from time import sleep
# DELETE FROM songs WHERE SongID = "id"

def delete():
	read()
	sure = False
	# while loop validation
	while sure == False:
		givenID = input("\nEnter the ID of the Song you'd Like to delete:\n")
		print(f"You've selected song of ID {givenID}.")
		confirm = input(f"Are you sure you want to Delete song {givenID}?\n")
		if confirm == "yes" or confirm == "y" or confirm == "Y":
			sure = True

	cursor.execute(f"DELETE FROM songs WHERE SongID = {givenID}")
	conn.commit()

	print(f"The Song of ID {givenID} has been deleted.")
	sleep(2)
	read()

if __name__ == "__main__":
	delete()