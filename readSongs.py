from connect import *


def read():
    cursor.execute("SELECT * FROM songs")
    rows = cursor.fetchall()

    print("\n", rows)
    print(type(rows))

    for record in rows:
        print(record)

    conn.commit()

# If the same file was
if __name__ == "__main__":
    read()
