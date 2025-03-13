import requests

search = input("Enter book titel") #burgeren skal skrive titel.  
url = f"https://openlibrary.org/search.json?q={search}" #bruger f" da det gør det nemmer at indsætte variabler i tekststrenge. en f" er en række af karaktere/bogstaver. 

#{} er placeholders

response= requests.get(url) # laver et reponse til url 

if response.status_code == 200: # if statment. hvis der er reponse til url gør nu...
    data = response.text # variabel data der gemmer forespørgsel
    print(data)



