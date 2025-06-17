import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


def init_db():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,cover_id INTEGER,reading_status TEXT,user_id INTEGER)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT UNIQUE,password TEXT)""")
    connection.commit()
    connection.close()

def add_db(title, author, year, cover_id, reading_status, user_id):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    sql = "INSERT OR IGNORE INTO books (title, author, year, cover_id, reading_status, user_id) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(sql, (title, author, year, cover_id, reading_status, user_id))
    connection.commit()



def update_reading_list(reading_status, cover_id, user_id, title, author, year):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()


    cursor.execute("SELECT * FROM books WHERE cover_id = ? AND user_id = ?", (cover_id, user_id))
    book = cursor.fetchone()
    

    if book:
         sql = "UPDATE books SET reading_status = ? WHERE cover_id = ? AND user_id = ?"
         cursor.execute(sql, (reading_status, cover_id, user_id))
    
    else: 
        sql = "INSERT INTO books (title, author, year, cover_id, reading_status, user_id) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, (title, author, year, cover_id, reading_status, user_id))
    
    

    connection.commit()
    connection.close()

        
def create_user(username, password):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    hash_pw = generate_password_hash(password)
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hash_pw))

    connection.commit()
    connection.close()




def get_books_by_status(status, user_id):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM books WHERE reading_status = ? AND user_id = ?"
    cursor.execute(sql, (status, user_id))
    books = cursor.fetchall()
    connection.close()
    return books

def get_all_books_for_user(user_id):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM books WHERE user_id = ?"
    cursor.execute(sql, (user_id,))
    books = cursor.fetchall()
    connection.close()
    return books

def delete_book(cover_id, user_id):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    try:
        sql = "DELETE FROM books WHERE cover_id = ? AND user_id = ?"
        cursor.execute(sql, (cover_id, user_id))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()
    

     #gemmer ændringerne
      #except sqlite3.Error as error:
     # print(f"Error {error}")  
   # finally:

   class User:
    def __init__(self, user_id, username)
        

        def add_book(self, book)