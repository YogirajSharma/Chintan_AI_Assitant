import os  # Importing OS module to interact with the operating system
from shlex import quote  # Importing quote for safely encoding shell arguments
import sqlite3  # Importing SQLite3 for database operations
import struct  # Importing struct for binary data handling
import subprocess  # Importing subprocess to execute system commands
import time  # Importing time module for delays
import webbrowser  # Importing webbrowser module to open URLs
from playsound import playsound  # Importing playsound for playing audio files (pip install playsound==1.2.2)
import eel  # Importing Eel for Python-JavaScript interaction
import pvporcupine  # Importing Porcupine for wake word detection (pip install pvporcupine==1.9.5)
import pyaudio  # Importing PyAudio for audio input/output
import pyautogui  # Importing PyAutoGUI for GUI automation
from engine.command import speak  # Importing speak function from engine.command module
from engine.config import ASSISTANT_NAME  # Importing assistant's name from config
import pywhatkit as kit  # Importing pywhatkit for YouTube playback and other tasks
from hugchat import hugchat  # Importing HugChat for chatbot functionality (pip install hugchat)
from engine.helper import extract_yt_term, remove_words  # Importing helper functions(pip install pywhatkit)
# Connecting to SQLite database
con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

# Function to play assistant startup sound
@eel.expose  # Exposing function to JavaScript
def playAssistantSound():
    music_dir = "web\\assets\\audio\\start_sound.mp3" # Path to startup sound file
    playsound(music_dir) # Playing the startup sound
# Function to open applications or URLs based on user command
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "") # Removing assistant name from query
    query = query.replace("open", "") # Removing "open" keyword from query
    query.lower()   # Converting query to lowercase

    app_name = query.strip()  # Removing extra spaces

    if app_name != "":

        try:
             # Searching for application path in system command database
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query) # Announcing opening action
                os.startfile(results[0][0]) # Opening the application

            elif len(results) == 0: 
                # Searching for URL in web command database
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query) # Announcing opening action
                    webbrowser.open(results[0][0])  # Opening the URL

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query) # Attempting to open using system command
                    except:
                        speak("not found") # If unable to open
        except:
            speak("some thing went wrong") # Handling exceptions
# Function to play a YouTube video based on user query
def PlayYoutube(query):
    search_term = extract_yt_term(query) # Extracting search term from query
    speak("Playing "+search_term+" on YouTube") # Announcing playback action
    kit.playonyt(search_term) # Announcing playback action
# Function to detect hotword and trigger assistant
def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # Initializing Porcupine for wake word detection with predefined keywords  
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # Continuous listening loop
        while True:
            keyword = audio_stream.read(porcupine.frame_length)  # Reading audio input
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)  # Converting audio data

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")# Indicating hotword detection

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")# Simulating Windows key press
                autogui.press("j")# Pressing 'J' for assistant activation
                time.sleep(2)# Delay
                autogui.keyUp("win")# Releasing Windows key
                
    except:
        # Cleaning up resources on error
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

# Function to find a contact in the database
def findContact(query):
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])

        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0

# Function to send a WhatsApp message or call
def whatsApp(mobile_no, message, flag, name):
    

    if flag == 'message':
        target_tab = 11
        jarvis_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7
        message = ''
        jarvis_message = "calling to "+name

    else:
        target_tab = 6
        message = ''
        jarvis_message = "staring video call with "+name


    # Encode the message for URL
    encoded_message = quote(message)
    print(encoded_message)
    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(jarvis_message)

# Chatbot function
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\\cookies.json")  # Initializing chatbot
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)  # Getting chatbot response
    print(response)
    speak(response)  # Speaking response
    return response
    
