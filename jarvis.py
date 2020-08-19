import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #it takes micophone input from the others

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'google' in query:
            webbrowser.open("www.google.com")

        elif 'stack overflow' in query:
            webbrowser.open("www.stackoverflow.com") 


        elif 'music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is:{strTime}") 

        elif 'code' in query:
            codePath = "C:\\Users\\cyberpoint\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"   
            os.startfile(codePath)

        elif 'sololearn' in query:
            webbrowser.open("www.sololearn.com")

        elif 'movie' in query:
            movies_dir = 'D:\\movies\\X Men Dark Phoenix 2019 1080p BRRip x264 Hindi English DD 5.1 ESubs - LOKiHD - Telly' 
            movies = os.listdir(movies_dir) 
            print(movies) 
            os.startfile(os.path.join(movies_dir, movies[2]))

        elif 'lords' in query:
            webbrowser.open("https://www.lordz.io/")
              
        elif 'battle' in query:
                webbrowser.open("https://zombsroyale.io/") 

        elif 'guessing' in query:
                webbrowser.open("https://gartic.io/") 

        elif 'snake' in query:
                webbrowser.open("http://slither.io/")

            
        elif 'opera' in query:
            webbrowser.open("C:\\Users\\cyberpoint\\AppData\\Local\\Programs\\Opera\\launcher.exe")
                        
        elif 'firefox' in query:
            webbrowser.open("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

        elif 'torrent' in query:
            webbrowser.open("C:\\Users\\cyberpoint\\AppData\\Roaming\\uTorrent\\uTorrent.exe")
            
        elif 'map' in query:
            webbrowser.open("https://www.google.com/maps") 
            
        elif 'image' in query:
            webbrowser.open("https://imagemap.org/") 
            
        elif 'gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?pli=1#inbox")
            
        elif 'whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
            
        elif 'facebook' in query:
            webbrowser.open("www.facebook.com")
            
        elif 'subscribed' in query:
            webbrowser.open("https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww")
            
        elif 'who are you' in query:
            speak("I am JARVIS, an voice assistant.Made by Vinit sir!") 