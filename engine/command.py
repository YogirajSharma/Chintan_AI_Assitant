import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install SpeechRecognition


def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 190)
    #eel.DisplayMessage(text)
    engine.say(text)
    #eel.receiverText(text)
    engine.runAndWait()
def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
       # eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        #eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        #eel.DisplayMessage(query)
        #time.sleep(2)
       
    except Exception as e:
        return ""
    
    return query.lower()
text = takecommand()
speak(text)