import RPi.GPIO as GPIO
import time
import pyrebase

GPIO.setmode(GPIO.BCM)

TRIGGER = 18
ECHO = 17
PINO_VIBRACALL = 21
DISTANCIA_OBSTACULO = 40
PINO_TOCAR = 4

GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(PINO_VIBRACALL, GPIO.OUT)
GPIO.setup(PINO_TOCAR, GPIO.OUT)
GPIO.output(TRIGGER, False)
GPIO.output(PINO_VIBRACALL, False)
GPIO.output(PINO_TOCAR, True)

config = {
  "apiKey": "yourAPIKEY",
  "authDomain": "yourauthdomain.firebaseapp.com",
  "databaseURL": "https://yourdatabaseurl.firebaseio.com/",
  "storageBucket": "yourstoragebucket.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def isConnected():
    conn = httplib.HTTPConnection("www.google.com")
    try:
        conn.request("HEAD", "/")
        return True
    except:
        return False

def vibrar():
    try:
        while True:
            GPIO.output(PINO_VIBRACALL, True)
            time.sleep(2)
            GPIO.output(PINO_VIBRACALL, False)
            print("vibracall...")
            return
    except KeyboardInterrupt:
        print("quit")
        GPIO.cleanup()

def tocar():
    try:
        while True:
            GPIO.output(PINO_TOCAR, False)
            time.sleep(2)
            GPIO.output(PINO_TOCAR, True)
            print("som...")
            return
    except KeyboardInterrupt:
        print("quit")
        GPIO.cleanup()

def salvar(distance):
    try:
            data = {"data": time.strftime("%d-%m-%y %H:%M:%S") , "distancia":distance}
            db.child("obstaculos").push(data)
            return
    except KeyboardInterrupt:
        print("quit")
        GPIO.cleanup()

try:
    while True:
        GPIO.output(TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(TRIGGER, False)
        start = time.time()
        while GPIO.input(ECHO)==0:
            start = time.time()
        while GPIO.input(ECHO)==1:
            stop = time.time()
        elapsed = stop-start
        distance = ( elapsed * 34300)/2
        print(distance)
        if (distance < DISTANCIA_OBSTACULO):
            vibrar()
            tocar()
            if(distance < DISTANCIA_LIMITE && isConnected()):
              salvar(distance)
        else:
            GPIO.output(PINO_VIBRACALL, False)
        time.sleep(1)
except KeyboardInterrupt:
    print("quit")
    GPIO.cleanup()
