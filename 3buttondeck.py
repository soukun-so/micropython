import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import board
import digitalio
import time

keyboard = Keyboard(usb_hid.devices)

# ピン番号を指定して、GPIOの設定
led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT
led.value = True

button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

# ピン番号を指定して、GPIOの設定
led2 = digitalio.DigitalInOut(board.GP26)
led2.direction = digitalio.Direction.OUTPUT
led2.value = True

button2 = digitalio.DigitalInOut(board.GP27)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.DOWN

# ピン番号を指定して、GPIOの設定
led3 = digitalio.DigitalInOut(board.GP21)
led3.direction = digitalio.Direction.OUTPUT
led3.value = True

button3 = digitalio.DigitalInOut(board.GP22)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.DOWN


while True:
    print(button.value)
    
    if button.value :
        keyboard.press(Keycode.WINDOWS, Keycode.D)  # Windowsキー+Dを送信
        keyboard.release_all()  # キーを離す
        time.sleep(3)
        
    if button2.value :
        keyboard.press(Keycode.WINDOWS, Keycode.TAB)  # Windowsキー+Dを送信
        keyboard.release_all()  # キーを離す
        time.sleep(3)
        
    if button3.value :
        keyboard.press(Keycode.U)  # Windowsキー+Dを送信
        keyboard.release_all()  # キーを離す
        keyboard.press(Keycode.N)  # Windowsキー+Dを送信
        keyboard.release_all()  # キーを離す
        keyboard.press(Keycode.K)  # Windowsキー+Dを送信
        keyboard.release_all()  # キーを離す
        keyboard.press(Keycode.O)  # Windowsキー+Dを送信
        keyboard.release_all()  # キーを離す
        time.sleep(3)
        
    time.sleep(0.3)     # 1秒待機
