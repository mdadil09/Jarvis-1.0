import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia 
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha
import time
import pywhatkit as kit
from contacts import contact
import requests




engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
wolframalpha_app_id = 'J637LG-5E2HTQAVYR'

def speak(audio):
     engine.say(audio)
     engine.runAndWait()

def time_():
     Time=datetime.datetime.now().strftime("%I:%M:%S")
     speak("The current time is")
     speak(Time)



def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)



 #Greetings
def wishme():
    speak("Wlecome back Mr. Mohammad Adil!")
    time_()
    date_()

    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour>=18 and hour<24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

    speak("Jarvis at your service. Please tell me how can I help you today?")

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print("Say that again please.....")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('username@gmail.com','password')
    server.sendmail('username@gmail.com'.to,content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/Md. Adil/Desktop/screenshot.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)

    battery = psutil.sensors_battery()
    speak('Battrey is at')
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())

def Introduction():
    speak("I am JARVIS 1.0 , Personal AI assistant , "
    "I am created by Mr. Adil , "
    "I can help you in various regards , "
    "I can search for you on the Internet , "
    "I can also grab definitions for you from wikipedia , "
    "In layman terms , I can try to make your life a bed of roses , "
    "Where you just have to command me , and I will do it for you , ")

def Creator():
    speak("Mr. Adil is an extra-ordinary person ,"
    "He has a passion for Robotics, Artificial Intelligence and Machine Learning ,"
    "He is very co-operative ,"
    "If you are facing any problem regarding the 'Jarvis', He will be glad to help you ")


if __name__=='__main__':

    clear = lambda: os.system('cls')
    clear()

    wishme()

    while True:
        query = TakeCommand().lower()

        if 'time' in query:
            time_()

        elif 'date' in query:
            date_()

        elif 'how are you' in query:
            speak("I am fine, Sir Thanks for asking")
            speak("How are you Sir?")
            if 'fine' in query or "good" in query: 
                speak("It's good to know that your fine")
            else:
                speak("I hope you get well soon.")
        
        elif "who am i" in query:
            speak("If you can talk, then definitely you are a human")
        elif "why you came to this world" in query:
            speak("Thanks to Mr. Adil. further it is a secret")

        elif 'what is love' and 'tell me about love' in query:
            speak("It is 7th sense that destroy all other senses , "
            "And I think it is just a mere illusion , "
            "It is waste of time")

        elif 'wikipedia' in query:
            speak("Searching......")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            speak('According to Wikipedia')
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content=TakeCommand()
                speak("Who is the Reciever?")
                reciever=input("Enter Reciever's Email : ")
                to = reciever
                sendEmail(to,content)
                speak(content)
                speak('Email has been sent.')

            except Exception as e:
                print(e)
                speak("Unable to send Email")
        
        elif 'search in chrome' in query:
            speak('What should i search?')
            chromepath = 'c:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'search youtube' in query:
            speak('What should I search?')
            search_Term = TakeCommand().lower()
            speak("Here We go to YOUTUBE!")
            wb.open('https://www.youtube.com/results?search_query='+search_Term)

        elif 'search google' in query:
            speak('What should I search?')
            search_Term = TakeCommand().lower()
            speak('Searching...')
            wb.open('https://www.google.com/search?q='+search_Term)

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'go offline' in query:
            speak('Going offline Sir!')
            quit()

        elif 'word' in query:
            speak('Opening Ms Word Sir.....')
            ms_word = r'C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE'
            os.startfile(ms_word)

        elif 'write a note' in query:
            speak("What should I write, Sir?")
            notes = TakeCommand()
            file = open('notes.txt','w')
            speak("Sir should I include Date and Time?")
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done Taking Notes, SIR!')
            else:
                file.write(notes)

        elif 'display note' in query:
            speak('showing notes Sir!')
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            screenshot()
            speak("screenshot has been taken, Sir!")

        elif "play music" in query or "hit some music" in query:
                music_dir = "C:/Users/Md. Adil/Desktop/SONGS"
                songs = os.listdir(music_dir)
                for song in songs:
                    os.startfile(os.path.join(music_dir, song))


        
        elif 'remember that' in query:
            speak("what should I remember Sir?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('memory.txt','r')
            speak("You asked me to remember that"+memory)

        elif 'news' in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/everything?q=Apple&from=2021-12-15&sortBy=popularity&apiKey=8a8df5dd9cf447c68a7598093060dc4d")
                data = json.load(jsonObj)
                i = 1

                speak('Here are the some headlines from the news Sir!')
                print('=======TOP HEADLINES========'+'\n')
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1
            except Exception as e:
                print(str(e))

        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("User asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('The answer is : '+answer)
            speak('The Answer is '+answer)
        
        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No Results")



        elif 'stop listening' in query:
            speak("For how many seconds you want me to listening to your command Sir?")
            ans = int(TakeCommand())
            time.sleep(ans)
            print(ans)


          #whatsapp function
        
        elif 'send a whatsapp message' in query:
            speak('Whom do you want to contact?')
            user = TakeCommand().lower()  
            speak("What do you want to say?")
            message = TakeCommand().lower()
            speak("When to send?")
            s_time = TakeCommand().lower()
            if 'later' in s_time:
                speak("Tell me about the hour?")
                hour__ = int(TakeCommand().lower())
                speak("Tell me about the minutes?")
                minute__ = int(TakeCommand().lower())
            elif 'now' in s_time:
                hour__ = datetime.datetime.now().hour
                if (datetime.datetime.now().second) < 30:
                    minute__ = (datetime.datetime.now().minute) + 1
                else:
                    minute__ = (datetime.datetime.now().minute) + 2
            speak("Sending Message.")
            kit.sendwhatmsg(contact[user]["phone"],message,hour__,minute__)   
        
         #most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
            
        elif "i love you" in query:
            speak("It's hard to understand, I am still trying to figure this out.")
        

            #system function
        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t l")    

        





#Api key 8a8df5dd9cf447c68a7598093060dc4d
#APPID: J637LG-5E2HTQAVYR


                

        