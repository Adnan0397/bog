from flask import Flask, render_template, request
import requests
app = Flask(__name__) #initialiser vores flask

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search_book")
def search():
        bookquery = request.args.get("bookquery") #vores query data fra input er stored her. 
        url = f"https://openlibrary.org/search.json?q={bookquery}" #bruger f" da det gør det nemmer at indsætte variabler i tekststrenge. en f" er en række af karaktere/bogstaver. 
        #{} er placeholders
       
        response= requests.get(url) # bruger get til at hente data. 
    
 
        if response.status_code == 200:
            data = response.json() # variabel data der gemmer data.
        else:
            print(f"failed{response.status_code}")
        
        data = response.json() # variabel data der gemmer data.
        
        book = data["docs"][0] #første resultat i vores liste. 01234
        title = book.get("title")
        author = book.get("author_name")
        year = book.get("first_publish_year")
        value = book.get("ia")[0]

        print(value, title, author, year)

        return render_template("search_book.html", title=title, author=author, year=year, value=value)

       


        



#todoo indsæt data fra api og render det på html



if __name__ == "__main__":
    app.run()


