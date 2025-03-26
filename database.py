import sqlite3


def init_db():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor() #bruges til at lave en connection til databasen og hente data. ligesom en mellemmand. cursor objekt
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title string, author string, year INTEGER, isbn TEXT)") #sql query



def add_to_db(title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    
    cursor = connection.cursor()

    sql = "INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?)" #vi laver en prepared statement. for ikke at få sql injection.


    cursor.execute(sql,(title, author, year, isbn))


  



    connection.commit() #gemmer ændringerne
    connection.close()