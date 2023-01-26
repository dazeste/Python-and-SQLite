import sqlite3 as sql


# connect(filePathDatabase)
conn = sql.connect(
    r"C:\JustIT\week_10_Python\day_4\database_operation\bootcamp.db")


# OR
# conn = sql.connect(     "C:\\JustIT\\week_10_Python\\day_4\\database_operation\\bootcamp.db")

cursor = conn.cursor()
cursor.execute("SELECT'hello world'")
rows = conn.cursor().fetchall()
print(type(rows))
