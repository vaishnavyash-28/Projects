# implement the basic jarvis...


import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer= sr.Recognizer()
engine=pyttsx3.init()
newsapi= "e71eb2eadde24041b7996794d77dbb15"


def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link= musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r= requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
         data = r.json()
         articles = data.get('articles', [])
    
         for article in articles:
               speak(article['title'])

    else:
        #let openAi  handle the request
        pass


if __name__=="__main__":
    speak("initializing jarvis....")
    while True:
         #listen for the weak word "jarvis"
         #obtain audion from the microphone

         r=sr.Recognizer()
        
    

         #reconize speech using sphinx
         print("recognizing..")
         try:
              with sr.Microphone() as source:
                 print("Listening...")
                 audio=r.listen(source,timeout=2,phrase_time_limit=1)

              word = r.recognize_google(audio)
              if(word.lower()=="jarvis"):
                  speak("Ya")
                  #listen for command

                  with sr.Microphone() as source:
                        print("Jarvis Active...")
                        audio=r.listen(source)
                        command = r.recognize_google(audio)

                        processCommand(command)
         except Exception as e:
            print("error;{0}" .format(e))

