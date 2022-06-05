from gpiozero import Button
from mainModule import *
import time
from TTS import *
button = Button(3)

while True:
    if(button.wait_for_press(button)):
        try:
            print("Function 2 started")
            mainModule()
            print("Function 2 finished")
        except:
            TTS("An error has occurred, please try again")
        time.sleep(10)
