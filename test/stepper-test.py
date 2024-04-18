# import RPi.GPIO as GPIO
# from RpiMotorLib import RpiMotorLib
# import time
# 
# direction= 38 # Direction (DIR) GPIO Pin
# step = 36 # Step GPIO Pin
# EN_pin = 40 # enable pin (LOW to enable)
# 
# # Declare a instance of class pass GPIO pins numbers and the motor type
# mymotortest = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DM542")
# GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output
# 
# GPIO.output(EN_pin,GPIO.LOW) # pull enable to low to enable motor
# mymotortest.motor_go(False, # True=Clockwise, False=Counter-Clockwise
#                      "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
#                      50, # number of steps
#                      .0005, # step delay [sec]
#                      False, # True = print verbose output 
#                      .05) # initial delay [sec]
# 
# GPIO.cleanup() # clear GPIO allocations after run


# ======================================================================


import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


on = GPIO.HIGH
off = GPIO.LOW


pul = 36
dir = 38
ena = 40


GPIO.setup(pul,GPIO.OUT)
GPIO.setup(dir,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)

GPIO.output(dir,off)
GPIO.output(pul,off)
GPIO.output(ena,on)
time.sleep(.0001)
GPIO.output(ena,off)
time.sleep(.0001)


def moveright(rotate):
    for i in range(rotate):
      GPIO.output(pul,on)
      time.sleep(.001/int(speed))
      GPIO.output(pul,off)
      time.sleep(.001/int(speed))

def moveleft(rotate):
    GPIO.output(dir,on)
    time.sleep(.0001)
    for i in range(rotate):
      GPIO.output(pul,on)
      time.sleep(.001/int(speed))
      GPIO.output(pul,off)
      time.sleep(.001/int(speed))



howmany = input("Please enter how many times to steps: ")
print("You entered: " + howmany)


speed = input("Please enter how fast to step: ")
print("You entered: " + speed)




moveright(int(howmany))
time.sleep(10)
moveleft(int(howmany))

GPIO.cleanup()