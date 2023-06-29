import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) 



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greeting():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    
    speak("Hope you are good. My name is babu lal, I am a voice assistant developed by Soham kanti jana. Please tell me How may I help you ?")
    
    
    
def inputcommand(): #It will take input or listen from the user's microphone and return string output
    
    query=''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..... Please say something")
        r.pause_threshold    # seconds of non-speaking audio before a phrase is considered complete
        audio=r.listen(source)
    
    try:
        print("Recognizing ..... Hold on")
        query=r.recognize_google(audio, language='en-in')
        print(f'You said : {query}\n')  #use of f-string
    
    except Exception as e:
        #print(e)
        print("It was not you, it was me..... Please say that again.")

    
    return query
        
if __name__=="__main__":
    greeting()
    while True:
        query = inputcommand().lower()  
    
    #logics for executing the different tasks
        if 'wikipedia' in query:
            speak('Searching wikipedia.......')
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
            
        elif 'open google' in query:
            webbrowser.open("google.com")
             
        elif 'youtube' in query:
            query=query.replace("search youtube","")
            if len(query)==0:
                speak("please say again.")
            else:
                
                try:
                    speak("searching on youtube.")
                    youtube = 'https://www.youtube.com/results?search_query=' + query
                    webbrowser.open(youtube)
                except Exception as e:
                    print("I didn't understand please say it again.")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif'open gfg' in query:
            webbrowser.open("http s://practice.geeksforgeeks.org")
        elif'open zoro' in query:
            webbrowser.open("https://sanji.to/home")
        

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}\n")
        
        elif 'google' in query :
            speak("What to search ?")
            s_query=inputcommand().lower()
            s_query = s_query.replace("search google", "")
            
            try :
                pywhatkit.search(s_query)
                result=wikipedia.summary(s_query,2)
                speak(result)
            except Exception as e:
                print("Sorry, I am not able to search this.")
        
        elif 'stop'  in query:
            speak("Are you sure you want to exit ?")
            exit_query = inputcommand().lower()
            if 'yes' in exit_query:
                speak("Thank you. Have a nice day.")
                exit()
            else:
                continue
            
