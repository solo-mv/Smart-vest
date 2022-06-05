from gpiozero import Button
from location import *
from TTS import *
import time
button = Button(4)

while True:
    if(button.wait_for_press(button)):
        try:
            print("Function 3 started")
            location()
            print("Function 3 finished")
        except:
            TTS("An error has occurred, please try again")

        time.sleep(10)
