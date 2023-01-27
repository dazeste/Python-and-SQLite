from connect import *
from readSongs import read
from time import sleep

def update():
	# Taken the ID
	givenID = input("Enter the ID of the Song you'd like to update:\n")

	title = input("Enter new title ")
	artist = input("Enter new Artist: ")
	genre = input("Enter new Genre: ")

	# Update SQL Statement
	cursor.execute(
		f"""
		UPDATE songs
		SET Title = "{title}", Artist = "{artist}", Genre = "{genre}"
		WHERE SongID = {givenID}
		;
		"""
		
	)
	conn.commit()

	print(f"Song ID {givenID} has been successfully updated.")
	sleep(2)
	read()

if __name__ == "__main__":
	update()