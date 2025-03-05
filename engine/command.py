import time # Importing time module for delays
import pyttsx3 # Importing Python-based text-to-speech conversion library that works offline(pip install pyttsx3)
import speech_recognition as sr # Importing speech_recognition for voice input(pip install SpeechRecognition)
import eel # Importing eel for Python-JavaScript interaction

# Function to convert text to speech
def speak(text):
    text = str(text)  # Ensuring the text is in string format
    engine = pyttsx3.init('sapi5')  # Initializing the pyttsx3 engine with sapi5 (Windows API for speech)
    voices = engine.getProperty('voices')  # Getting available voices
    engine.setProperty('voice', voices[0].id)  # Setting the voice to the first available one
    engine.setProperty('rate', 190)  # Setting the speech rate
    eel.DisplayMessage(text)  # Sending the message to the frontend
    engine.say(text)  # Speaking the text
    eel.receiverText(text)  # Displaying received text in the frontend
    engine.runAndWait()  # Running the speech engine until it finishes speaking

# Function to recognize voice commands
@eel.expose # Exposing function to JavaScript
def takecommand():
    r = sr.Recognizer()  # Initializing the speech recognizer
    with sr.Microphone() as source:  # Using the default microphone as input source
        print('listening....')  # Printing status message
        eel.DisplayMessage('listening....')  # Displaying listening status in the frontend
        r.pause_threshold = 1  # Setting pause threshold for speech detection
        r.adjust_for_ambient_noise(source)  # Adjusting for background noise
        audio = r.listen(source, 10, 6)  # Listening to the audio input (timeout 10s, phrase limit 6s)
    try:
        print('recognizing')  # Printing status message
        eel.DisplayMessage('recognizing....')  # Displaying recognizing status in the frontend
        query = r.recognize_google(audio, language='en-in')  # Converting speech to text using Google API
        print(f"user said: {query}")  # Printing recognized text
        eel.DisplayMessage(query)  # Displaying recognized text in the frontend
        time.sleep(2)  # Adding a small delay
        # speak(query)  # (Commented out) Optionally, speak the recognized text
    
       
    except Exception as e:
        return "" # Returning an empty string if recognition fails
    
    return query.lower() # Returning the recognized text in lowercase
# Function to process voice or text commands
@eel.expose  # Exposing function to JavaScript
def allCommands(message=1):

    if message == 1:
        query = takecommand() # Taking voice command
        print(query) # Printing the query
        eel.senderText(query) # Sending meassage to frontend
    else:
        query = message #if a text messsage is provided, use it directly
        eel.senderText(query) # Sending message to the frontend
    try:
        # query = takecommand()
        # print(query)
        if "open" in query:
            from engine.features import openCommand # Importing function to open applications
            openCommand(query) # Executing open command
        elif "on Youtube" in query:
            from engine.features import PlayYoutube  # Importing function to play YouTube videos
            PlayYoutube(query)  # Executing YouTube playback
        
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp  # Importing functions for WhatsApp operations
            flag = "" # Initializing flag variable
            contact_no, name =findContact(query) # Finding contact details from query
            if(contact_no != 0): # Checking if a valid contact was found

                if "send message" in query:
                    flag = 'message'  # Setting flag for message sending
                    speak("what message to send")  # Asking user for message content
                    query = takecommand()  # Taking message input
                elif "phone call" in query:
                    flag = 'call'  # Setting flag for phone call
                else:
                    flag = 'video call'  # Setting flag for video call
                    
                whatsApp(contact_no, query, flag, name) # Sending WhatsApp message or initiating call
            
        else:
            from engine.features import chatBot  # Importing chatbot function
            chatBot(query)  # Sending query to chatbot
    except:
        print("error")  # Printing error message if something fails
    
    eel.ShowHood()  # Displaying the chat hood in the frontend