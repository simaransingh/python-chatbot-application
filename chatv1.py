from datetime import datetime
import requests
#if msg== "hi" or msg == "hello" or msg =="hey":
  #print("Hello how are you...!")
#else:
 #   print("I didn't understand that.")
greet_keywords = ["hi","hello","hey","hii","hi there","hey there","hello there"]
date_intent = ["date","what is the date","what's the date", "tell me the date","current date"]
time_intent = ["time","current time","what is the time","what's the time" , "tell me the time"]
news_intent = ["news","current news","what's the news" , "tell me the news" , "latest news"]
weather_intent = ["weather","current weather","what's the weather" , "tell me the weather" , "weather update"]
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
  msg = input("Enter your message: ").lower()
  
 
  if msg in greet_keywords:
   print("Hello how are you...!")
  elif msg in date_intent:
   date = datetime.now().strftime("%d %b, %Y")
   print("today's date is : ",date)
  elif msg in time_intent:
   time = datetime.now().strftime("%I:%M:%S %p")
   print("current time is :",time)
  elif msg in news_intent:
   print("here are the latest news :")
   get_news()
  elif msg in weather_intent:
   print("the Current weather is :")
   get_weather()
  elif msg == "exit" or msg == "bye":
   print("Goodbye !")
   chat = False
  else:
   print("I didn't understand that.")
