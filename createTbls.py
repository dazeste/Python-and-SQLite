from connect import *

cursor.execute(
    """
CREATE TABLE"songs"(
  "SongID" INTEGER NOT NULL UNIQUE,
  "Title" TEXT,
  "Artist" TEXT,
  "Genre" TEXT,
  PRIMARY KEY("SongID" AUTOINCREMENT)
)
"""
)
conn.commit()
