#import pyautogui
#from pynput.keyboard import Key, Controller
GPIOport=10
CoinMaxTimeinInStatus=200 # in milliseconds
TimeBetweenCoins=500 # in Milliseconds
from chronometer import Chronometer
import datetime
import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
#keyboard = Controller()
count=0
while True:
    while GPIO.input(10) == GPIO.HIGH:
        print("IN")
        with Chronometer() as t:
            while GPIO.input(GPIOport) == GPIO.HIGH:
                time.sleep(50 / 1000)
        timeout = float('{0:.0f}'.format(float(t)*1000))
        print("OUT")
        if timeout < 250:
            print("Credit")
            count = count+1
            print(count)
        else:
            print("Coin time out")
#        pyautogui.press('enter')
#        print('{:.3f} secs.'.format(float(t)))
