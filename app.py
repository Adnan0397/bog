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
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("index.html")




@app.route("/search_book")
def search():
    bookquery = request.args.get("bookinput")  # vores query data fra input er stored her. 
    if not bookquery:
        return redirect(url_for("index"))

    url = f"https://openlibrary.org/search.json?q={bookquery}"  # bruger f" da det gør det nemmer at indsætte variabler i tekststrenge. en f" er en række af karaktere/bogstaver. 
    # {} er placeholders
    try:
        response = requests.get(url)  # bruger get til at hente data. 

        if response.status_code == 200:
            data = response.json()
            if not data["docs"]:
                return render_template("index.html", error="NO RESULT FOUND")
        else:
            return render_template("index.html", error="API ERROR")

        book = data["docs"][0]  # første resultat i vores liste. 01234
        title = book.get("title")
        author = book.get("author_name")

        if isinstance(author, list):
            author = ", ".join(author)

        year = book.get("first_publish_year")
        cover_id = book.get("cover_i")

        # pattern = re.compile(r"isbn_(\d+)")
        # isbn = "isbn"
        # for i in values:
        #     match = pattern.match(i)
        #     if match:
        #         isbn = match.group(1)
        #         break

       

        return render_template("search_book.html",title=title,author=author,year=year,cover=cover_id)

    except Exception as e:
        print(f"Error: {e}")
        return render_template("index.html", title=title, author=author, year=year, cover=cover_id)  # sender data videre til search side

    
            

           
         

 
@app.route("/status", methods=["POST"])               
def add_status(): 
        if "user_id" not in session:
            return redirect(url_for('login'))

        status = request.form.get("status")
        cover_id = request.form.get("cover_id")
        title = request.form.get("title")
        author = request.form.get("author")
        year = request.form.get("year")
             
        user_id = session.get("user_id")
        database.update_reading_list(status, cover_id, user_id, title, author, year)


        return redirect(url_for('show_list'))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return render_template("signup.html", error="Username or password required")

        try:
            database.create_user(username, password)
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            return render_template("signup.html", error="Username already exists")

    
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
            return render_template("login.html", error="Wrong Username or password")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))
        


@app.route("/list")
def show_list():
    if "user_id" not in session: 
        return redirect(url_for("login"))


    user_id = session.get("user_id")
    reading_books = database.get_books_by_status("Reading", user_id)
    completed_books = database.get_books_by_status("Completed", user_id)
    planned_books = database.get_books_by_status("Plan to Read", user_id)
    
    return render_template("list.html", reading_books=reading_books, completed_books=completed_books, planned_books=planned_books)




@app.route("/reading-list")
def get_reading_list():
    user_id = session.get("user_id")
    if not user_id:
        return {"error": "Not logged in"}, 401

    books = database.get_all_books_for_user(user_id)
    return {"books": books}

@app.route("/delete", methods=["POST"])
def delete_book():
    if "user_id" not in session: 
        return redirect(url_for("login"))

    
    cover_id = request.form.get("cover_id")
    user_id = session.get("user_id")


    if cover_id:
        database.delete_book(cover_id, user_id)


    return redirect(url_for("show_list"))



if __name__ == "__main__":
    app.run()


