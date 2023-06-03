import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import os 
import webbrowser
import random 
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')

# for voice in voices:
#     print("Voice ID:", voice.id)
#     print("Name:", voice.name)
#     print("Languages:", voice.languages)
#     print("Gender:", voice.gender)
#     print("Age:", voice.age)
#     print("```````````````````````````````````````````````````````````````\n")


engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")
    elif  hour >=12 and hour<18:
        speak("Good Afternoon ! ") 
    else:
        speak("Good Evening!")
    speak("HI i am JARVIS,  how my i help you !")
def take_command():
    # This function take microphone input and convert it into the string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognising........")
        query=r.recognize_google(audio, Language="en-in")
        print(f"user said :{query}\n")
    except  Exception as e :
        #print(e)
        print("Say Once Again Please!")
        return "none "
    return query
         


if __name__=='__main__':
    speak("Mukul you are a python Developer")
    wish()
    while True:
        query=take_command().lower()
        if 'wikipedia' in query:
            speak("Searhing in Wikipedia ....")
            query.replace('wikipedia', '')
            result=wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia")
            print(result)
            speak(result)
        elif 'open youtube ' in query:
            speak("opening youtube ")
            webbrowser.open("youtube.com")
        elif 'open google ' in query:
            speak("opening google ")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open('github.com')
        elif 'play music' or 'play songs' in query:
            music_dir="M:\data\songs"
            song=os.listdir(music_dir)
            print(song)
            n=random.randint(1, 6)
            os.startfile(os.path.join(music_dir, song[n]))
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open('web.whatsapp.com')
        elif 'time now '  or 'timing now' in query:
            strtime=datetime.datetime().now().strftime("%H:%M:%S")
            speak(f"The current time is {strtime}")
        elif 'open vs code ' or 'open code' in query:
            code="C:\\Users\\Mukul Rana\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code)
        

            