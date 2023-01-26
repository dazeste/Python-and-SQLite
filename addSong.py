from connect import *
from readSongs import read
from time import sleep

# Add songs
mySong = []

title = input("Enter a Song Title: ")
artist = input("Enter an Artist: ")
genre = input("Enter the Genre of the song: ")

mySong.append(title)
mySong.append(artist)
mySong.append(genre)


print(mySong)
cursor.execute(
    f"""
INSERT INTO songs VALUES(NULL, 
"{mySong[0]}", "{mySong[1]}", "{mySong[2]}")

"""
)

# commit our changes
conn.commit()

print(f"The song {title}, has been added successfully to the database.")

sleep(3)

read()
