import requests

search_query = input("Enter book titel") #burgeren skal skrive titel. 
url = f"https://openlibrary.org/search.json?q={search_query}" #bruger f" da det gør det nemmer at indsætte variabler i tekststrenge. en f" er en række af karaktere/bogstaver. 
