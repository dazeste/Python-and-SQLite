from connect import *

def read():
	cursor.execute("SELECT * FROM songs")
	rows = cursor.fetchall()

	# print("\n",rows)
	# print(type(rows))

	print("\nSong List:")
	for record in rows:
		# print(type(record))
		print(record)

if __name__ == "__main__":
	read()
