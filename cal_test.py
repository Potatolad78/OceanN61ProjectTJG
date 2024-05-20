from RGBLightLibrary import RGBLight, servoMove, powerRelay, lightSensor
from time import sleep



servo = servoMove(3)

#22 26
valveRelay = powerRelay(26)
pumpRelay = powerRelay(22)
sensor = lightSensor(1,7,6)
sensor = sensor.returnSensor()
print(sensor.read())

LED = RGBLight(0,1,2)
servo.move()
#servoPin = Pin(3, Pin.OUT)
#servo = Servo(servoPin)

#servo.write(80)
#sleep(1)
#servo.write(-50)

LED.takeMeassurments("green", 0.5,sensor,5)
LED.takeMeassurments("purple", 0.5, sensor,5)
