import sqlite3


def init_db():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor() #bruges til at lave en connection til databasen og hente data. ligesom en mellemmand. cursor objekt
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, titel string, author string, release_year INTEGER, isbn TEXT)") #sql query

  cursor.execute(sql, book) #udføre kommandoen 
  connection.commit() #gemmer ændringerne



def add_to_db():
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books (titel, author, release_year) VALUES (?, ?, ?)
    ,(title, author, year, isbn))")


#vi laver en prepared statement. for ikke at få sql injection.
           # for loop der ittere over vores tabels indhold 
  




connection.close()