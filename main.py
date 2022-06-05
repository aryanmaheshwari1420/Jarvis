from pip import main
import datetime
import pyttsx3
import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

# f = open("C:\\Users\\Aryan Maheshwari\\Desktop\\Jarvis\\password.txt",'r')
# password = f.readlines()
new_password = '' #password required

# from speech_recognition import Microphone

engine  = pyttsx3.init('sapi5') # sapi5 is a inbuilt audio provided my mircrosoft
voices  = engine.getProperty('voices')
# print(voices) # show the two voices in my laptop once is male another is female
engine.setProperty('voices',voices[0].id)
# print(voices[1].id) , print(voices[0].id) # two voices we having one is david voic which is of male and another is ziva voice that is female voice



def speak(audio):
    engine.say(audio) # it will speak the main method speak statement
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! ")
    elif hour>=12 and hour<18:
        speak("Good afternoon! ")
    elif hour>=18 and hour<24:
        speak("Hey! In the night what can i help for you")    

    speak("I am your roboo  Speed 1 terahertz, memory 1 zeta byte. what i can help for you ") 
    # speak(" main aapka robot hu ky madad kr skta hu aapki")  just for testing 

def takeCommand():
    # It takes microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognition...")
        query = r.recognize_google(audio,language='en-in') # using recognize_google for recognize our language 
        print(f"User said: {query}\n") 

    except Exception as e:
        # print(e)       
        print("Say that again please...")
        return "None" # if any problem occur then it return none
    return query    

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('aryanmaheshwari1420@gmail.com',new_password)
    server.sendmail('aryanmaheshwari1420@gmail.com',to,content)
    server.close()
    


if __name__ == "__main__":
    # speak("Aryan is a good boy") # just for testing
    wishMe()
    # takeCommand() just for testing
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace('wikipedia',"")
            result = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open linkedin' in query:
            webbrowser.open('linkedin.com')

        elif 'play music' in query: # to play random music from a particular directory use random moudule and your brain
            # music_dir = "D:\english song"
            # songs = os.listdir(music_dir)
            # print(songs)
            music_dir = "D:\hindi song"
            songs = os.listdir(music_dir)
            # os.startfile(os.path.join(music_dir,songs[0]))
            os.startfile(os.path.join(music_dir,random.choice(songs)))

        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strtime("%H:%H:%S")
            speak(f"str,the time is{str.time}")    

        elif 'open vscode' in query:
            codepath = "C:\\Users\\Aryan Maheshwari\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open java ide' in query:
            codepath = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2021.2\\bin\\idea64.exe"   
            os.startfile(codepath)

        elif 'send email' in query:
            # work on to send on special one by creating dictionary at the top
            try:
                speak("what should i say?")
                content  = takeCommand()
                to = "" # mandatory to use official gmail id at this point
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend i am unable to send this email ...please try again!")
        elif 'quit' in query: 
            exit()            






