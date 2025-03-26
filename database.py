import sqlite3

connection = sqlite3.connect("books.db")

cursor = connection.cursor()

#bruges til at lave en connection til databasen og hente data. ligesom en mellemmand. cursor objekt
cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, titel string, author string, release_year INTEGER, isbn TEXT)") #sql query



sql = "INSERT INTO books (titel, author, release_year) VALUES (?, ?, ?)"
#vi laver en prepared statement. for ikke at få sql injection.
for book in books:              # for loop der ittere over vores tabels indhold 
    cursor.execute(sql, book) #udføre kommandoen 
    connection.commit() #gemmer ændringerne




connection.close()