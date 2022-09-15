import socket
import time
import pyttsx3
import datetime
import wikipedia
import webbrowser
import requests
import sys
import os
import speech_recognition as sr
import requests
import json
import pywhatkit
import pyjokes
import smtplib
from playsound import playsound
import pyautogui
import wolframalpha
from pywikihow import search_wikihow
try:
    app=wolframalpha.Client("<your API ID>")
except Exception as e:
    print("something want wrong")



rec=sr.Recognizer()


#sapi5 is used to take the voices
engine=pyttsx3.init('sapi5')
voices =engine.getProperty('voices')

#to set a particular voice 
engine.setProperty('voice',voices[1].id)
#print(voices[0].id)


def speak(audio):
    '''
    this fucntion take input as a text and speak that function
    '''
    engine.say(audio)
    engine.runAndWait()

def wishme():
    '''
    this function wish you according to the time
    '''
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!! have a great day ahead")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    elif hour>=18 and hour<20:
        speak("Good Evening")
    elif hour>=20 and hour<24:
        speak("Good Night sir! have a Sweet dreams")

    speak("Hello sir i am dora ! how may i help you")

def takeCommand():
    '''
    this function take the voice input and return a string output
    '''

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio = r.listen(source,phrase_time_limit=5)

    try:
        print("Please wait DORA is working")
        query= r.recognize_google(audio,language='en-in')
        print(f"you said:{query}")
    except Exception as e:
        print(e)
        speak("DORA can't find what you are trying to say can you please say it again")
        return "None"
    return query


def SendEmail(to,content):
    # for sending a Email

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rroot310@gmail.com', 'shubhu@#7031')
    server.sendmail('rroot310@gmail.com',to, content)
    server.close()


app=wolframalpha.Client("79Q5YY-G9W8986KYE")

if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()
    #logic for the task to exceute based on requirement
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)

            #some basic task
        if 'who is dora' in query:
            speak("dora is the AI that is created by my master full form of dora is domestic operation remote access")
        if 'who is jarvis' in query:
            speak("jarivs is the AI that is created by my master full form of jarvis is just a rather advance virtual assiatance")

        elif 'what is the full form of dora' in query:
            speak("the full form of dora is domestic operation remote access")
        elif 'what is the full form of jarvis' in query:
            speak("the full form of jarvis is just a rather advance virtual assitance")
        elif 'who created dora' in query:
            speak("my master shubham created me and my purpose is to define the piece")
        elif 'who created Jarvis' in query:
            speak("my master shubham created me and my purpose is to define the piece")
        elif 'thank you' in query:
            speak("your welcome sir dora is for you ")
        elif 'how are you' in query:
            speak("i am fit and fine sir")
        elif 'hello dora' in query:
            speak("hello sir! i am Dora how may i help you")
        elif 'hello jarvis' in query:
            speak("hello sir! i am jarvis how may i help you")

        elif 'activate jarvis' in query:
            speak("initializing all the sequences")
            speak("transfering the control to the JARVIS")
            playsound('l1.mp3')
            engine.setProperty('voice', voices[0].id)
            speak("hello sir i am jarvis")

            #searching on youtube
        if 'youtube search' in query:
            speak("yes sir searching on youtube")
            query=query.replace("dora","")
            query=query.replace("youtube search","")
            web='https://www.youtube.com/results?search_query='+query
            webbrowser.open(web)
            speak("here is the result for the youtube search"+query)

        elif 'google search' in query:
            speak("please wait sir i am working on google")
            query=query.replace("dora","")
            query=query.replace("google search","")
            web1='https://www.google.com/search?q='+query
            webbrowser.open(web1)
            speak("here is the result of google search"+query)


        elif 'ask something' in query:
            speak("what should i search")
            s1=takeCommand().lower()
            res=app.query(s1)
            speak(next(res.results).text)
            #print(next(res.results).text)

        elif 'repeat after me' in query:
            speak("ok sir speak now i will repeat after you")
            r1=takeCommand().lower()
            speak(r1)

        elif 'play music' in query:
            song=query.replace('play','')
            speak('playing'+song)
            pywhatkit.playonyt(song)

        if 'time' in query:
            t1=datetime.datetime.now().strftime("%I:%M:%p")
            speak(f"sir the time is{t1}")
            print(t1)

        if 'open code' in query or 'open a code' in query:
            codepath="C:\\Users\\Shubham\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("open code for you sir")
            os.startfile(codepath)


        elif 'can you find me a some news ' in query:
            speak("yes sir finding a news for you")
            speak("the times of india news here are the news for you")
            url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=a9ad2d6937f549658ec01ef18e168634"
            news = requests.get(url).text
            news = json.loads(news)
            arts = news['articles']
            for article in arts:
                speak(article['title'])
                print(article['title'])
                speak("now the next & best news are comeing")



        elif 'open metrics for me' in query:
            path1="E:\\programing\\batch file script\\hack1.bat"
            speak("enetering into the matrix for you sir")
            os.startfile(path1)

        elif 'where i am' in query or 'where we are' in query:
            speak("wait sir,let me check")
            try:
                ipADD=requests.get('https://api.ipify.org').text
                print(ipADD)
                url='https://get.geojs.io/v1/ip/geo'+ipADD+'.json'
                geo_requests=requests.get(url)
                geo_data=geo_requests.json()
                city=geo_data['city']
                country=geo_data['country']
                speak(f"sir i am not sure, but i think we are in{city} city of{country} country")
            except Exception as e:
                speak("sorry sir due to some error i can't find out")


        elif 'ip address' in query:
            hostname= socket.gethostname()
            local_ip=socket.gethostbyname(hostname)
            print(local_ip)
            speak(local_ip)

        elif 'send email' in query:

            try:
                #speak("can i know the email id of receiver")
                speak("write the email id of receiver")
                e_id=input()
                #e_id=takeCommand().lower()
                to=e_id
                speak("what should you want to send in email")
                content=takeCommand().lower()
                SendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("the email was not send successfully")

        elif 'jokes' in query:
            speak(pyjokes.get_joke())

        elif 'open cmd' in query:
            os.system("start cmd")

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'open editor mode' in query or 'i want to edit' in query:
            speak("editor mode is open sir")
            task=takeCommand().lower()
            if 'select all' in task or 'select all text' in task:
                speak("selceting all the text for you sir")
                pyautogui.keyDown("ctrl")
                pyautogui.keyUp("a")
                pyautogui.keyDown("ctrl")
                speak("text has been selected sir")
            if 'copy' in task:
                speak("copying this text sir")
                pyautogui.keyDown("ctrl")
                pyautogui.keyUp("c")
                pyautogui.keyDown("ctrl")
                speak("text is copy sir")
            elif 'paste' in task:
                speak("pasteing text sir")
                pyautogui.keyDown("ctrl")
                pyautogui.keyUp("c")
                pyautogui.keyDown("ctrl")
                speak("text is pasted sir")

        elif 'how to' in query:
            speak("please wait sir DORA is working")
            lb=query.replace("dora","")
            max_result=1
            f1=search_wikihow(lb,max_result)
            assert len(f1) == 1
            f1[0].print()
            speak(f1[0].summary)

        elif 'open notepad' in query:
            os.system("start notepad")

        permission=takeCommand()
        if "wake up" in permission:
            speak("at your service sir")
            takeCommand()
        elif "goodbye" in permission:
            speak("when ever need me just call me")
            sys.exit()


        elif 'quit the program' in query:
            speak("Deactivating the program")
            break
