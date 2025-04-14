import requests

url = "https://official-joke-api.appspot.com/random_joke"

respons = requests.get(url)
if respons.status_code==200:
    data = respons.json()
    print("Quesion : ",data["setup"])
    print("Answer : ",data["punchline"])
else : 
    print("status_code : ",respons.status_code)