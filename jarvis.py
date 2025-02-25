import os  # Import OS module to run system commands
import eel  # Import Eel for creating the web-based UI

# Import required features from engine
from engine.features import *  # Import all features
from engine.command import *  # Import all commands 

def start():
    """Initialize the assistant's web interface and start the Eel application."""

    eel.init("web")  # Set "web" as the directory for UI files

    playAssistantSound()  # Play startup sound for the assistant

    # Open Microsoft Edge in app mode and load the assistant interface
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    # Start the Eel web server, listening on localhost, and blocking execution
    eel.start('index.html', mode=None, host='localhost', block=True)
