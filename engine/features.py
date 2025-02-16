from playsound import playsound #(pip install playsound==1.2.2)
import eel
#playing assistant sound
@eel.expose
def playAssistantSound():
    music_dir = "web\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)