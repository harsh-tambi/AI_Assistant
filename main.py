import openai
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import datetime

def say(text):
    os.system(f"say {text}")


def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language = 'en-in')
            print (f"User Said - {query}")
            return query
        except Exception as e:
            return "Sorry, please try again."
if __name__ == '__main__':
    say('Hi! How can I help you?')
    while True:
        print ('Listening')
        text = takeCommand()
        sites = [
                 ["youtube", "https://youtube.com"], 
                 ["google", "https://google.com"], 
                 ["facebook", "https://facebook.com"], 
                 ["wikipedia", "https://wikipedia.com"]
                ]
        for site in sites:
            if f"Open {site[0]}".lower() in text.lower():
                say(f"Opening {site[0]} boss")
                webbrowser.open(site[1])
        
        if "open music" in text:
            musicpath = "/Users/harshtambi/Downloads/summer-walk-152722.mp3"
            os.system(f"open {musicpath}")

        if "time" in text:
            strftimme = datetime.datetime.now().strftime("%H:%M")
            say(f"The time is {strftimme}")



        # say(text)]
       

