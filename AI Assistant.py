import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import webbrowser
import pyaudio
import os
import subprocess

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # Voice

def speak(audio):
    print("Jarvis:", audio)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")


# Function to perform Google search
def search_google(query):
    speak(f"Searching Google for {query}")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

def search_wikipedia(query):
    wikipedia.set_lang("en",)
    try:
        results = wikipedia.search(query)
        if results:
            summary = wikipedia.summary(results[0], sentences=5)

            speak(f"You asked about {query}. Let me check Wikipedia...")
            speak(summary)
            # print(summary)
        else:
            speak("No results found.")

            
    except wikipedia.exceptions.DisambiguationError as e:
        speak("Your query is ambiguous. Try being more specific.")
    except wikipedia.exceptions.PageError:
        speak("Page not found.")
    except Exception as e:
        speak("An error occurred while searching Wikipedia.")

# # Main loop
# speak("Hello, I am Jarvis. What would you like to know from Wikipedia?")
wishMe()


while True:
    command = listen()
    if "exit" in command or "stop" in command:
        speak("Goodbye!")
        break
    elif "youtube" in command:
        speak("Opening YouTube now.")
        # webbrowser.open("https://www.youtube.com")
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome_proxy.exe  --profile-directory=Default --app-id=agimnkijcaahngcdmfeangaknmldooml"
        url = "https://www.youtube.com"
        subprocess.Popen(f'{chrome_path} {url}')    


    elif "chrome" in command:
        speak("Opening Chrome now.")
        
        path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        #   webbrowser.open("https://www.google.c  om")
        url = "https://www.google.com"
        subprocess.Popen(f'{path} {url}')    

    elif " the time" in command:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir, the time {strTime}")
    elif "vs code" in command:
        codePath = "C:\\Users\\LENOVO L-470\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    elif "pycharm" in command:
        code = "C:\\Program Files\\JetBrains\\PyCharm 2025.1.3\\bin\\pycharm64.exe"
        os.startfile(code)
# Inside your main loop
    elif "search google for" in command:
        query = command.replace("search google for", "").strip()
        if query:
            search_google(query)
        else:
            speak("Please tell me what to search for.")        
    

    elif command:
        search_wikipedia(command)
