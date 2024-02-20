import time
import usb_hid
from adafruit_hid.mouse import Mouse
import board
import digitalio

mouse = Mouse(usb_hid.devices)

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

led.value = False
time.sleep(5)

def movex(param):
    mouse.move(x=param)
def movey(param):
    mouse.move(y=param)

# You can put how many times do you want to move, if you have any problems testing, just put break to end the loop.

while True:
    led.value = True
    movex(550)
    time.sleep(0.2)
    movey(550)
    time.sleep(0.2)
    movex(-550)
    time.sleep(0.2)
    movey(-550)
    time.sleep(0.2)
    
