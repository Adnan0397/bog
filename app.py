from flask import Flask, render_template, request
import requests
app = Flask(__name__) #initialiser vores flask

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search_book", methods=["GET"])
def search():
    if request.method == "GET": 
        bookquery = request.args["bookquery"]
        url = f"https://openlibrary.org/search.json?q={bookquery}"
        response= requests.get(url)
        data = response.json()
        print(data["docs"][0])
        return render_template("search_book.html")

#todoo indsæt data fra api og render det på html



if __name__ == "__main__":
    app.run()


