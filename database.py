import sqlite3

connection = sqlite3.connect("books.db")

cursor = connection.cursor()

#bruges til at lave en connection til databasen og hente data. ligesom en mellemmand. cursor objekt
cursor.execute("CREATE TABLE IF NOT EXISTS books (titel string, author string, release_year integer)") #sql query
#todoo lav id til table, find ud hvordan man fetcher fra api. med request. 
books = [
    ("The Metamorphasis", "Franz Kafka", 1970),
    ("gurli gris", "James Gunn", 2010 ),
    ("Doppler", "arlend loe", 2020),
    ("Hunger games", "suzanne collins", 2008 )
]

sql = "INSERT INTO books (titel, author, release_year) VALUES (?, ?, ?)"
#vi laver en prepared statement. for ikke at få sql injection.
for book in books:
    cursor.execute(sql, book)
    connection.commit()

SELECT ROWID books

connection.commit()
connection.close()