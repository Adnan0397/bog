import sqlite3


def init_db():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor() #bruges til at lave en connection til databasen og hente data. ligesom en mellemmand. cursor objekt



    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, cover_id INTEGER, reading_status TEXT)") #sql query

    connection.commit()
  
def add_db(title, author, year, cover_id, reading_status): #parameter 
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    sql = "INSERT OR IGNORE INTO  books (title, author, year, cover_id, reading_status) VALUES (?, ?, ?, ?, ?)"


    
    cursor.execute(sql, (title, author, year, cover_id, reading_status))  #https://tinyurl.com/5fhjnp3j

def status():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    

   

    connection.commit() #gemmer ændringerne
      #except sqlite3.Error as error:
     # print(f"Error {error}")  
   # finally:
    connection.close() 