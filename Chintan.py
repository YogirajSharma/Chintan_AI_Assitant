# Import necessary libraries 
import pyttsx3  # For text-to-speech conversion (pip install pyttsx3) 
import speech_recognition as sr  # For speech recognition (pip install SpeechRecognition) 
import datetime  # To get the current date and time 
import wikipedia  # To fetch information from Wikipedia (pip install wikipedia) 
import webbrowser  # To open web pages 
import os  # To interact with the operating system 
import smtplib  # To send emails 
import pyaudio
 
# Initialize the text-to-speech engine 
engine = pyttsx3.init('sapi5')  # Uses Microsoft Speech API (sapi5) 
voices = engine.getProperty('voices')  # Get available voices 
engine.setProperty('voice', voices[0].id)  # Set the voice (0 = male, 1 = female) 
 
def speak(audio): 
    """Function to make the assistant speak the given text.""" 
    engine.say(audio)  # Pass the text to the speech engine 
    engine.runAndWait()  # Execute the speech 
 
def wishMe(): 
    """Function to greet the user based on the current time.""" 
    hour = int(datetime.datetime.now().hour)  # Get the current hour (0-23 format) 
     
    # Determine the appropriate greeting 
    if hour >= 0 and hour < 12: 
        speak("Good Morning!") 
    elif hour >= 12 and hour < 18: 
        speak("Good Afternoon!") 
    else: 
        speak("Good Evening!") 
 
    speak("I am Chintan Sir. Please tell me how may I help you.")  # Introduce the assistant 
 
def takeCommand(): 
    """Function to take voice input from the user and return it as a 
text string.""" 
    r = sr.Recognizer()  # Initialize the recognizer 
    with sr.Microphone() as source:  # Use the system microphone as the input source 
        print("Listening...") 
        r.pause_threshold = 1  # Pause time before processing the next input 
        audio = r.listen(source)  # Capture the audio input 
 
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language='en-in')  # Convert speech to text 
        print(f"User said: {query}\n")  # Print recognized text 
 
    except Exception: 
        print("Say that again, please...")  # If recognition fails 
        return "None"  # Return "None" to indicate failure 
     
    return query  # Return the recognized text 
# Main execution starts here 
if __name__ == "__main__": 
    wishMe()  # Call the function to greet the user 
 
    while True: 
        query = takeCommand().lower()  # Convert the recognized text to lowercase 
 
        if query == "none": 
            continue  # Skip if no valid input is received 
        if "stop listening" in query: 
            speak("Okay, I will stop listening. Have a great day!") 
            break  # Exit the loop
 
        # Search Wikipedia 
        if 'wikipedia' in query: 
            speak('Searching Wikipedia...') 
            query = query.replace("wikipedia", "").strip()  # Remove "wikipedia" and extra spaces  
            try:
                results = wikipedia.summary(query, sentences=2)  # Fetch summary (2 sentences)  
                webbrowser.open(f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}")  # Open relevant Wikipedia page  
                speak("According to Wikipedia")  
                print(results)  # Print the Wikipedia summary  
                speak(results)  # Read out the summary  
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results. Please be more specific.")
                print(e)
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any relevant Wikipedia page.")
 
        # Open popular websites 
        elif 'open youtube' in query: 
            webbrowser.open("https://www.youtube.com")  # Open YouTube in the browser 
 
        elif 'open google' in query: 
            webbrowser.open("https://www.google.com")  # Open Google in the browser 
 
        elif 'open stackoverflow' in query: 
            webbrowser.open("https://stackoverflow.com")  # Open Stack Overflow 
 
        # Play music on YouTube based on user demand 
        elif 'play music' in query: 
            speak("Which song would you like to hear?") 
            song = takeCommand().lower()  # Get the song name from the user 
            if song != "none": 
                webbrowser.open(f"https://www.youtube.com/results?search_query={song}")  # Search for the song on YouTube 
                speak(f"Playing {song} on YouTube")  # Inform the user 
            else: 
                speak("Sorry, I couldn't recognize the song name.")  # Handle unrecognized input 
 
        # Tell the current time 
        elif 'what is the time' in query: 
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  # Get current time in HH:MM:SS format 
            speak(f"Sir, the time is {strTime}")  # Announce the time 
 
        # Open Visual Studio Code (VS Code) 
        elif 'open code' in query: 
            codePath = "C:\\Users\\yogir\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # Adjust path 
            os.startfile(codePath)  # Open VS Code 
 
        elif 'send mail' in query: 
            speak("Opening Gmail and composing a new email...")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")  # Opens Gmail in Compose mode

