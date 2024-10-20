import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import board
import digitalio
import time

keyboard = Keyboard(usb_hid.devices)

led1 = digitalio.DigitalInOut(board.GP0)
led1.direction = digitalio.Direction.OUTPUT
led1.value = False

led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT
led.value = True

button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

led2 = digitalio.DigitalInOut(board.GP26)
led2.direction = digitalio.Direction.OUTPUT
led2.value = True

button2 = digitalio.DigitalInOut(board.GP27)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.DOWN

led3 = digitalio.DigitalInOut(board.GP21)
led3.direction = digitalio.Direction.OUTPUT
led3.value = True

button3 = digitalio.DigitalInOut(board.GP22)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.DOWN


while True:
    print(button.value)
    
    if button.value :
        led1.value = True
        keyboard.press(Keycode.WINDOWS, Keycode.D)
        keyboard.release_all()
        time.sleep(3)
        led1.value = False
        
    if button2.value :
        led1.value = True
        keyboard.press(Keycode.WINDOWS, Keycode.TAB)
        keyboard.release_all()
        time.sleep(3)
        led1.value = False
        
    if button3.value :
        led1.value = True
        keyboard.press(Keycode.U) 
        keyboard.release_all() 
        keyboard.press(Keycode.N)
        keyboard.release_all() 
        keyboard.press(Keycode.K) 
        keyboard.release_all()
        keyboard.press(Keycode.O)
        keyboard.release_all() 
        time.sleep(3)
        led1.value = False
        
    time.sleep(0.3)     # 1秒待機
