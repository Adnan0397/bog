from flask import Flask, render_template, request, redirect, url_for
import requests
import database
import sqlite3
from flask import session, flash
from werkzeug.security import check_password_hash
import os

database.init_db()


app = Flask(__name__) #initialiser vores flask
app.secret_key = os.urandom(24)  

@app.route("/")
def index():
    return render_template("index.html")




@app.route("/search_book")
def search():
        bookquery = request.args.get("bookinput") #vores query data fra input er stored her. 
        url = f"https://openlibrary.org/search.json?q={bookquery}" #bruger f" da det gør det nemmer at indsætte variabler i tekststrenge. en f" er en række af karaktere/bogstaver. 
        #{} er placeholders
       
        response= requests.get(url) # bruger get til at hente data. 
    
 
        if response.status_code == 200: #tjekker status
            data = response.json() #response bliver lavet om til json format, og gemt i variablen data. 
        else:
            print(f"failed{response.status_code}")
        
        

        book = data["docs"][0] #første resultat i vores liste. 01234
        title = book.get("title")
        author = book.get("author_name")

        if isinstance(author, list):
            author = ", ".join(author)

        year = book.get("first_publish_year")
        cover_id = book.get("cover_i")

        print("cover id: ", cover_id)

        #pattern = re.compile(r"isbn_(\d+)")

        #isbn = "isbn"

        #for i in values:
            #match = pattern.match(i)
            #if match:
                 #isbn = match.group(1)
                # break
        
        if cover_id: 
            database.add_db(title, author, year, cover_id, "")

        print(f"{title}, {author}, {year}, {cover_id}")

    
        return render_template("search_book.html", title=title, author=author, year=year, cover=cover_id) #sender data videre til search side

    
            

           
         

 
@app.route("/status", methods=["POST"])               
def add_status(): 
        status = request.form.get("status")
        cover_id = request.form.get("cover_id")

        database.update_reading_list(status, cover_id)

        print(status, cover_id)

        return render_template("search_book.html", status=status, cover=cover_id)          
                  
@app.route("/signup", methods=["GET", "POST"])
def signup():
     if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return render_template("signup.html", error="Brugernavn og adgangskode kræves")
        
        try:
            # Create new user
            database.create_user(username, password)
            return redirect("/login")
        except sqlite3.IntegrityError:
            return render_template("signup.html", error="Brugernavnet findes allerede")
        
        return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return render_template("login.html", error="Brugernavn og adgangskode kræves")

        conn = sqlite3.connect("books.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[2], password):  # user[2] = password hash
            session["user_id"] = user[0]
            session["username"] = user[1]
            return redirect("/")
        else:
            return render_template("login.html", error="Forkert brugernavn eller adgangskode")

    return render_template("login.html")

def logout():
    session.clear()
    return redirect("/")
        


@app.route("/list")
def show_list():
    reading_books = database.get_books_by_status("Reading")
    completed_books = database.get_books_by_status("Completed")
    planned_books = database.get_books_by_status("Plan to Read")
    
    return render_template("list.html", reading_books=reading_books, completed_books=completed_books,planned_books=planned_books)
               
                          

#conn = sqlite3.connect(database)
#cur = conn.cursor()
#cur.execute("SELECT * from ")


        




        



#todoo indsæt data fra api og render det på html





if __name__ == "__main__":
    app.run()


