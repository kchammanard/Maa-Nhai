import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


ledpinred = 11
ledpinblue = 15
# 11 = Red, 13 = Green, 15 = Blue
pushpin1 = 16
pushpin2 = 18
# Button1 = 16, Button2 = 18
GPIO.setup(ledpinred, GPIO.OUT)
GPIO.setup(ledpinblue, GPIO.OUT)
# set ledpin as an output
GPIO.setup(pushpin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pushpin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# with pull up resistor

while True:
    GPIO.output(ledpinred, not GPIO.input(pushpin2))
    sleep(0.1)
    GPIO.output(ledpinblue, not GPIO.input(pushpin1))
    sleep(0.1)
