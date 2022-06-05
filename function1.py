from gpiozero import Button
from main import *
import time
from TTS import *
button = Button(2)

while True:
    if(button.wait_for_press(button)):
        try:
            print("Function 1 started")
            main()
            print("Function 1 finished")
        except:
            TTS("An error as occurred, please try again")
        time.sleep(10)

