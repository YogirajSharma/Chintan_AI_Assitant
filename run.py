 

import multiprocessing # Import multiprocessing for parallel execution#import subprocess

# Function to start the Jarvis assistant
def startJarvis():
        # Code for process 1
        print("Process 1 is running.")# Indicate that Process 1 has started
        from jarvis import start # Import the start function from the jarvis module
        start() #start jarvis assistant

# Import the start function from the Chintan module
def listenHotword():
        # Code for process 2
        print("Process 2 is running.") # Indicate that Process 2 has started
        from engine.features import hotword  # Import the hotword detection function
        hotword() # Start listening for the hotword


    # Start both processes
if __name__ == '__main__':
        # Create two separate processes
        p1 = multiprocessing.Process(target=startJarvis) # Process 1 for Jarvis
        p2 = multiprocessing.Process(target=listenHotword) # Process 2 for hotword detection
        p1.start()  # Start Process 1
        p2.start()  # Start Process 2
        p1.join() # Wait for Process 1 to finish

         # If Process 2 is still running after Process 1 ends, terminate it
        if p2.is_alive():
            p2.terminate()  # Force stop Process 2
            p2.join() # Ensure it has stopped

        print("system stop")  # Indicate that both processes have ended