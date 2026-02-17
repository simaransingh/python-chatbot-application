# pip install speechrecognition  pyttsx3 pyaudio
from datetime import datetime
import requests
import speech_recognition as sr
import pyttsx3
import webbrowser
#if msg== "hi" or msg == "hello" or msg =="hey":
  #print("Hello how are you...!")
#else:
 #   print("I didn't understand that.")
greet_keywords = ["hi","hello","hey","hii","hi there","hey there","hello there"]
date_intent = ["date","what is the date","what's the date", "tell me the date","current date"]
time_intent = ["time","current time","what is the time","what's the time" , "tell me the time"]
news_intent = ["news","current news","what's the news" , "tell me the news" , "latest news"]
weather_intent = ["weather","current weather","what's the weather" , "tell me the weather" , "weather update"]
#text to speech
engine = pyttsx3.init()
engine.setProperty("rate",170)
def speak(text):
 engine.say(text)
 engine.runAndWait()
 
def take_input():
 print("welcome to chatbot...!!!")
 print(""""
please select your input method:
1. Keyboard Input
2. Voice Input
""")
 choice = int(input("Enter your choice (1 or 2): "))
 if choice == 1:
  msg = input("Enter your message: ").lower()
 elif choice == 2:


  #Speech to text
  rec = sr.Recognizer()
  with sr.Microphone() as source:
   print("Listening....")
   audio = rec.listen(source)
 try:
  query = rec.recognize_google(audio)  
  print("you :",query)
  msg = query.lower()
 except:
  speak("Can't understand what you said...")
  return""

def get_news():
 url ="https://newsapi.org/v2/everything?q=apple&from=2026-02-12&to=2026-02-12&sortBy=popularity&apiKey=2c3c263c1e0749cd9730dae2de16cb58"
 response = requests.get(url)
 data = response.json()
 total_results = data["totalResults"]
 print("Total news articles found :", total_results)
 articles = data["articles"]
 for i in range(12):
  print("News title: ",articles[i]["title"])
def get_weather():
 ip_url = "http://ip-api.com/json/"
 location= requests.get(ip_url).json()
 lat= location['lat']
 lon= location['lon']
 print("Your current location is:" ,location['city'],location["country"])
 api_key ="f211aabec1ccce2ce5fcdc4ac29a38d3"
 url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
 response = requests.get(url)
 data = response.json()
 print("current weather : ",data["weather"] [0]["description"])
 print("current temperature :",data["main"] ["temp"])
chat = True
while chat:
  msg = take_input()
  if msg in greet_keywords:
   speak("Hello how are you...!")
  elif msg in date_intent:
   date = datetime.now().strftime("%d %b, %Y")
   speak(f"today date is : {date}")
  elif msg in time_intent:
   time = datetime.now().strftime("%I:%M:%S %p")
   speak("current time is:{time}")
  elif msg in news_intent:
   print("here are the latest news :")
   get_news()
  elif msg in weather_intent:
   speak("the current weather is : ")
   get_weather()
  elif msg.startswith("open"):
   website = msg.split()[-1]
   webbrowser.open(f"https://www.{website}.com") 
  elif msg == "exit" or msg == "bye":
   speak( "Goodbye!")
   chat = False
  else:
   speak("I didn't understand that.")
