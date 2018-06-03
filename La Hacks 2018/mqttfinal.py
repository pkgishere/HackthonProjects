import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.serwarnings(False)
GPIO.setup(18, GPIO.OUT)    #LED
GPIO.setup(19, GPIO.OUT)    #Right
GPIO.setup(20, GPIO.OUT)    #Left

def moveForward():
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)

def turnRight():
    GPIO.output(19, GPIO.LOW)
    GPIO.output(20, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)

def turnLeft():
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(20, GPIO.LOW)
    time.sleep(2)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)

def ledTurn():
	GPIO.output(18, GPIO.HIGH)
	time.sleep(2)
	GPIO.output(18, GPIO.LOW)


def on_connect(client, userdata, flags, rc):
    print(str(rc))
    client.subscribe("anith/test")
    client.subscribe("anith/topic")
    client.subscribe("avyay/test")
    client.subscribe("avyay/topic")
    

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    if msg.payload == "LED":
        print("Led will turn ON and OFF")
        ledTurn()
    if msg.payload == "Forward":
        print("Bot will move forward")
        moveForward()
    if msg.payload == "Left":
    	print("Bot will move left")
    	turnLeft()
    if msg.payload == "Right":
    	print("Bot will move right")
    	turnRight()	    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()