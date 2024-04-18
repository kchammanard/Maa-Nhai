import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

red = 11
green = 13
blue = 15

ledpin = green

GPIO.setup(ledpin, GPIO.OUT)

# While loop
while True:
        # set GPIO14 pin to HIGH
        GPIO.output(ledpin,GPIO.HIGH)
        # show message to Terminal
        print("LED is ON")
        # pause for one second
        time.sleep(1)

        # set GPIO14 pin to HIGH
        GPIO.output(ledpin,GPIO.LOW)
        # show message to Terminal
        print("LED is OFF")
        # pause for one second
        time.sleep(1)