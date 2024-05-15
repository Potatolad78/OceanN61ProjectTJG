from machine import Pin
from time import sleep
from servo import Servo

servoPin = Pin(3, Pin.OUT)
servo = Servo(servoPin)

servo.write(80)
sleep(1)
servo.write(-50)