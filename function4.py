from gpiozero import Button
from movingfiles import *
import time
from TTS import *
button = Button(17)

while True:
    if(button.wait_for_press(button)):
        try:
            print("Function 4 started")
            movingfiles()
            print("Function 4 finished")
        except:
            TTS("An error has occurred, please try again")

        time.sleep(10)
