from gpiozero import Button
from meow import *
import time
from TTS import *
button = Button(27)

while True:
    if(button.wait_for_press(button)):
        try:
            print("Function 5 started")
            meow()
            print("Function 5 finished")
        except:
            TTS("An error has occurred please try again")

        time.sleep(10)
