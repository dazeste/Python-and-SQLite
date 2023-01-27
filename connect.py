import sqlite3 as sql

# connect(filePathToDatabase)
conn = sql.connect(r"C:\Files\Desktop\softwarebootcamp\Lessons\GLA4\Python Week10\databaseoperations\bootcamp.db")

cursor = conn.cursor()
