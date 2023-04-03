import time
import board
import digitalio

relay1 = digitalio.DigitalInOut(board.GP16)
relay1.direction = digitalio.Direction.OUTPUT

relay2 = digitalio.DigitalInOut(board.GP17)
relay2.direction = digitalio.Direction.OUTPUT

relay3 = digitalio.DigitalInOut(board.GP18)
relay3.direction = digitalio.Direction.OUTPUT

startbutton = digitalio.DigitalInOut(board.GP20)
startbutton.switch_to_input(pull=digitalio.Pull.UP)

startbuttonled = digitalio.DigitalInOut(board.GP21)
startbuttonled.direction = digitalio.Direction.OUTPUT

key = digitalio.DigitalInOut(board.GP19)
key.switch_to_input(pull=digitalio.Pull.UP)

def reset():
    relay1.value = False
    relay2.value = False
    startbuttonled.value = False
    print("resetetetet")

def an():
    relay1.value = True
    relay3.value = True
    time.sleep(0.2)
    relay1.value = False
    relay3.value = False
    

def aus():
    relay2.value = True
    relay3.value = True
    time.sleep(0.2)
    relay2.value = False
    relay3.value = False

reset()
while True:
    if key.value == False:
        if startbutton.value == False:
            print("startbutton gedrückt")
            startbuttonled.value = True
            print("led an")
            while startbutton.value == False:
                pass
            print("startbutton net mehr gedrückt")
            startbuttonled.value = False
            print("led aus")
            an()
            print("steckdose an")
            startbuttonled.value = True
            print("led wieder an")
            while key.value == False:
                pass
            startbuttonled.value = False
            aus()
            startbuttonled.value = True
            time.sleep(0.1)
            startbuttonled.value = False
            print("ist aus lol ")
    while key.value == True:
        pass
