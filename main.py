import RPi.GPIO as GPIO
import requests
import datetime 
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

on = GPIO.HIGH
off = GPIO.LOW

# ===== API KEY and DATA ======
apiKey = "f95e6e0bb46a4aa520bfb13b9cf4a2b9"
lat = 13.74
long = 100.52

# ===== LED =====
red = 11
green = 13
blue = 15
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)


# ===== Button =====
buttonLeft = 18
buttonRight = 16
GPIO.setup(buttonLeft, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonRight, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# ===== Limit Switch =====
# Note : (MAX is the side with stepper)
lmMin = 32
lmMax = 31
GPIO.setup(lmMin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(lmMax, GPIO.IN, pull_up_down=GPIO.PUD_UP) 


# ===== Stepper =====
pul = 36
dir = 38
ena = 40
GPIO.setup(pul,GPIO.OUT)
GPIO.setup(dir,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)

speed = 3
rotate = 150


# ===== Functions =====
def ledOff():
    GPIO.output(red, off)
    GPIO.output(green, off)
    GPIO.output(blue, off)

def ledRed():
    GPIO.output(red, on)
    GPIO.output(green, off)
    GPIO.output(blue, off)

    
def ledGreen():
    GPIO.output(red, off)
    GPIO.output(green, on)
    GPIO.output(blue, off)
    
def ledBlue():
    GPIO.output(red, off)
    GPIO.output(green, off)
    GPIO.output(blue, on)

def moveToMax():
    GPIO.output(dir,off)
    time.sleep(.0001)
    for i in range(rotate):
      GPIO.output(pul,on)
      time.sleep(.001/int(speed))
      GPIO.output(pul,off)
      time.sleep(.001/int(speed))

def moveToMin():
    GPIO.output(dir,on)
    time.sleep(.0001)
    for i in range(rotate):
      GPIO.output(pul,on)
      time.sleep(.001/int(speed))
      GPIO.output(pul,off)
      time.sleep(.001/int(speed))

def stopMax():
    ledRed()
    time.sleep(0.01)
    for i in range(3):
        moveToMin()
        time.sleep(0.01)
    ledOff()
            
def stopMin():
    ledRed()
    time.sleep(0.01)
    for i in range(3):
        moveToMax()
        time.sleep(0.01)
    ledOff()
        
def moveUntilMax():
    while (not GPIO.input(lmMax)):
        moveToMax()
    stopMax()

def moveUntilMin():
    while (not GPIO.input(lmMin)):
        moveToMin()
    stopMin()
    
def call_weather_api():
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": long,
        "appid": apiKey
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        weather_main = weather_data['weather'][0]['main']  # Accessing weather.main
        print("Weather Main:", weather_main)
        return weather_main
    else:
        print("Failed to fetch weather data")
        return null


# ===== MAIN =====
# while True:    
#     ledGreen()
#     
#     if (GPIO.input(lmMax)):
#         stopMax()
#     else:
#         if (not GPIO.input(buttonLeft)):
#             ledBlue()
#             time.sleep(0.01)
#             moveToMax()
#             time.sleep(0.01)
#     if (GPIO.input(lmMin)):
#         stopMin()
#     else:
#         if (not GPIO.input(buttonRight)):
#             ledBlue()
#             time.sleep(0.01)
#             moveToMin()
#             time.sleep(0.01)

# ===== MAIN WITH AUTO MODE =====

currentPos = "min"
mode = "auto"

while True:
    current_time = datetime.datetime.now()
    current_time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
    current_hour = current_time.hour
    current_minute = current_time.minute
    print("Current Time:", current_time_string)
    
    if (mode == "auto"):
        ledBlue()
        print("Mode: auto")
        if (current_minute == 37):
            weather = call_weather_api()
            rains = ["rain", "shower rain", "thunderstorm"]
            if (weather in rains):
                moveUntilMin()
            else:
                moveUntilMax()
            time.sleep(60)
    elif (mode == "manual"):
        ledGreen()
        print("Mode: manual")
    
    if (not GPIO.input(buttonLeft)):
        if (currentPos == "min"):
            moveUntilMax()
            time.sleep(0.01)
            currentPos = "max"
        elif (currentPos == "max"):
            moveUntilMin()
            time.sleep(0.001)
            currentPos = "min"
    
    if (not GPIO.input(buttonRight)):
        if (mode == "auto"):
            mode = "manual"
        elif (mode == "manual"):
            mode = "auto"
    
    time.sleep(0.1)


