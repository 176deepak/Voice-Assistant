import speech_recognition as sr
import wikipedia as wp
import webbrowser as wb
import pyttsx3 as ptx
import datetime
import tkinter as tk

engine = ptx.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

app_window = tk.Tk()
app_window.title("Voice Assistant")
app_window.geometry("220x250")
app_window.resizable(False, False)
app_window.configure(background='')
icon_photo = tk.PhotoImage(file = "E:\VoiceAssistant\iconphoto.png")
display_img = tk.PhotoImage(file="E:\VoiceAssistant\mic.png")

app_window.iconphoto(False, icon_photo)
tk.Label(image=display_img, border=0).pack(pady=40)


def gretings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your P A. Please tell me how may I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        return "None"

    return query


if __name__ == "__main__":
    app_window.update()
    gretings()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wp.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            wb.open("youtube.com")

        elif 'open google' in query:
            wb.open("google.com")

        elif 'open stackoverflow' in query:
            wb.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'exit' in query:
            break