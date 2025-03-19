from flask import Flask, render_template, request
import requests
app = Flask(__name__) #initialiser vores flask

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search_book")
def search():
        bookquery = request.args.get("bookquery") #vores query data er fra input er stored her. 
        url = f"https://openlibrary.org/search.json?q={bookquery}" #bruger f" da det gør det nemmer at indsætte variabler i tekststrenge. en f" er en række af karaktere/bogstaver. 
        #{} er placeholders
        response= requests.get(url) # bruger get til at hente data. 
        data = response.json() # variabel data der gemmer data.
        print(data["docs"][0])
        return render_template("search_html")

#todoo indsæt data fra api og render det på html



if __name__ == "__main__":
    app.run()


