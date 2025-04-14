import requests #pip install requests
import pyttsx3 #pip install pyttsx3


url = "https://official-joke-api.appspot.com/random_joke"
talk=pyttsx3.init()
talk.getProperty("rate")
talk.setProperty("rate",110)
respons = requests.get(url)
if respons.status_code==200:
    data = respons.json()
    print("Quesion : ",data["setup"])
    talk.say(data["setup"])
    talk.runAndWait()
    print("Answer : ",data["punchline"])
    talk.runAndWait()
    talk.say("Answer")
    talk.runAndWait()
    talk.say(data["punchline"])
    talk.runAndWait()
else : 
    print("status_code : ",respons.status_code)import requests

url = "https://official-joke-api.appspot.com/random_joke"

respons = requests.get(url)
if respons.status_code==200:
    data = respons.json()
    print("Quesion : ",data["setup"])
    print("Answer : ",data["punchline"])
else : 
    print("status_code : ",respons.status_code)
