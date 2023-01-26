from time import sleep
from connect import *
from readSongs import read

# Delete from songs where SongID = "id"
read()


sure= False

# While loop validation
while sure:
  givenID = input("Enter the ID of the Song you'd Like to delete:\n")
  print(f"You selected song ID {givenID}. ")
  confirm = input("Are you sure you want delete song ID {givenID}?")
  if confirm == "y":
    sure = True


cursor.execute(f"DELETE FROM songs WHERE SongID = {givenID}")
conn.commit()

print(" The song of Id {givenID} has been deleted")
sleep(2)
read()