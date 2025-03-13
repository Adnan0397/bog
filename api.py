import requests

url = "https://www.google.com/books/jsapi.js"
status = requests.get(url)

print(status.status_code)
