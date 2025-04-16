import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


def init_db():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor() #bruges til at lave en connection til databasen og hente data. ligesom en mellemmand. cursor objekt
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, cover_id INTEGER, reading_status TEXT)")
    
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE,password TEXT)")

    connection.commit()
    connection.close()

def add_db(title, author, year, cover_id, reading_status): #parameter 
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    sql = "INSERT OR IGNORE INTO  books (title, author, year, cover_id, reading_status) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(sql, (title, author, year, cover_id, reading_status))  #https://tinyurl.com/5fhjnp3j
    connection.commit()


def update_reading_list(reading_status, cover_id):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    sql = "UPDATE books SET reading_status = ? WHERE cover_id = ?  "
    cursor.execute(sql, (reading_status, cover_id))
    connection.commit()

        
def create_user(username, password):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    hash_pw = generate_password_hash(password)
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hash_pw))

    connection.commit()
    connection.close()




def get_books_by_status(status=None):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    
    if status:
        sql = "SELECT * FROM books WHERE reading_status = ?"
        cursor.execute(sql, (status,))
    else:
        sql = "SELECT * FROM books"
        cursor.execute(sql)
    
    books = cursor.fetchall()
    connection.close()
    return books

    

     #gemmer ændringerne
      #except sqlite3.Error as error:
     # print(f"Error {error}")  
   # finally:

   