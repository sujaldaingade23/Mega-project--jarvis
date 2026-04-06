import speech_recognition as sr

import webbrowser

import pyttsx3








recognizer =sr.Recognizer()
engine=pyttsx3.init()

          

r=sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

 
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif"open  google gemini" in c.lower():
        webbrowser.open("https://google gemini.com")
    elif"open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif"open vscode"in c.lower():
        webbrowser.open("httsp://vscode.com")        
    
        

if __name__=="__main__":
    speak("jarvis get activet")
    while True:
        
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio=r.listen(source,timeout=3,phrase_time_limit=2)
            word=r.recognize_google(audio)
            if"jarvis" in word.lower():
                speak("Ya")
                with sr.Microphone() as source:
                    print("jarvis Listening...")
                    audio=r.listen(source,timeout=3,phrase_time_limit=2)
                    command=r.recognize_google(audio)

                    processcommand(command)

        except Exception as e:
            print("Error;{0}".format(e))            
   
