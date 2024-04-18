import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ledpinred = 11
ledpinblue = 15
# 11 = Red, 13 = Green, 15 = Blue                                               
limitswitchpulley = 32
limitswitchmotor = 31
# LM_MIN = 32, LM_MAX = 31 (MAX is the side with stepper)                                      
GPIO.setup(ledpinred, GPIO.OUT)
GPIO.setup(ledpinblue, GPIO.OUT) 
GPIO.setup(limitswitchpulley, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(limitswitchmotor, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
           GPIO.output(ledpinred, GPIO.input(limitswitchpulley))
           sleep(0.2)
           GPIO.output(ledpinblue, GPIO.input(limitswitchmotor))
           sleep(0.2)
           