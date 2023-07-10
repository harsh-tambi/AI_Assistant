import openai
import speech_recognition as sr
import wikipedia
import os

def say(text):
    os.system(f"say {text}")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio, language = 'en-in')
        print (f"User Said - {query}")
        return query

if __name__ == '__main__':
    say('Hi! How can I help you?')
    print ("You can speak now...... I'm listening")
    text = takeCommand()
    say ('Audio Recieved')
    say(text)



