import sqlite3


def init_db():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor() #bruges til at lave en connection til databasen og hente data. ligesom en mellemmand. cursor objekt



    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn TEXT)") #sql query

    connection.commit()
  
def add_db(title, author, year, isbn): #parameter 
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    sql = "INSERT OR IGNORE INTO  books (title, author, year, isbn) VALUES (?, ?, ?, ?)"

      
    cursor.execute(sql, (title, author, year, isbn))  #https://tinyurl.com/5fhjnp3j



  def reading_list():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor() #bruges til at lave en connection til databasen og hente data. ligesom en mellemmand. cursor objekt

    cursor.execute("CREATE TABLE IF NOT EXISTS Reading_list (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn TEXT)") #sql query

    connection.commit()

  def add_to_reading():
    sql = "INSERT INTO books (title, author, year, isbn, status) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(sql, (title, author, year, isbn, status))



   

    connection.commit() #gemmer ændringerne
      #except sqlite3.Error as error:
     # print(f"Error {error}")  
   # finally:
    connection.close() 