from connect import *
from readSongs import read
from time import sleep

def insertSongs():		# Take input and add songs.
	mySong = []
	title = input("Enter a Song Title: ")
	artist = input("Enter the Artist's Name: ")
	genre = input("Enter the Genre of the song: ")

	mySong.append(title)
	mySong.append(artist)
	mySong.append(genre)

	print(mySong)
	cursor.execute(
	f"""
	INSERT INTO songs VALUES(NULL, "{mySong[0]}", "{mySong[1]}", "{mySong[2]}")
	"""
	)
	conn.commit()
	print(f"{title}, has been added successfully to the database.")
	sleep(3)
	read()

if __name__ == "__main__":
	insertSongs()