import pyttsx3
import speech_recognition #s sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")


    speak("I am Jarvis Sir. Please tell me how may i help you")

def takeCommand():

    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")


    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query



if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia")
            print(results)
            speak(results)


        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'play music' in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H;%M:%S")
            speak(f"Sir The Current time is {strTime}")


        elif 'open chrome' in query:
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)


        elif 'open folder drive' in query:
            path = "E:"
            os.startfile(path)


        elif 'open windows drive' in query:
            path = "C:"
            os.startfile(path)



        elif 'open discord' in query:
            path = "C:\\Users\\prahl\\AppData\\Local\\Discord\\Update.exe"
            os.startfile(path)


        elif 'open minecraft' in query:
            mcPath = "C:\\Users\\prahl\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
            os.startfile(mcPath)


        elif 'about jarvis' in query:
            speak("I am Jarvis made By Ansh Dhakad 14years I was maded for helping peoples for using their pc fast "
                  "opening files apps and other things i can send an email and etc.. Dont Forget To Visit github for my"
                  "source code and you can make changes to my code Thanks For Using Jarvis ")


        elif 'open droidcam' in query:
            drPath = "C:\\Program Files (x86)\\DroidCam\\DroidCamApp.exe"
            os.startfile(drPath)


        elif 'start minecraft server' in query:
            sPath = "C:\\Users\\prahl\\OneDrive\\Desktop\\Spigot Server"
            os.startfile(sPath)