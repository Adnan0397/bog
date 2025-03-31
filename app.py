from flask import Flask, render_template, request
import requests
import re
import database

database.init_db()


app = Flask(__name__) #initialiser vores flask

@app.route("/")
def index():
    return render_template("index.html")

#if __name__ == '__main__':
 #   app.run(host="0.0.0.0", port=8000)

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
        cover = f"https://covers.openlibrary.org/b/ID/{cover_id}-L.jpg"

        #pattern = re.compile(r"isbn_(\d+)")

        #isbn = "isbn"

        #for i in values:
            #match = pattern.match(i)
            #if match:
                 #isbn = match.group(1)
                # break
        
        if cover_id: 
            database.add_db(title, author, year, cover_id, reading_status=None)

            print(f"{title}, {author}, {year}, {cover}")

    
        return render_template("search_book.html", title=title, author=author, year=year, cover=cover_id) #sender data videre til search side

    
            

           
         

 
@app.route("/status")               
def status():  
        return render_template("status.html")          
                  

        

  

        




        



#todoo indsæt data fra api og render det på html



if __name__ == "__main__":
    app.run()


