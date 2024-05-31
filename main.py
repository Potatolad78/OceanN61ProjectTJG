from RGBLightLibrary import RGBLight, servoMove, powerRelay, lightSensor
from machine import Pin, I2C
from time import sleep
import tsl2561
#Creates an LED object for you to use
valveRelay = powerRelay(28)
valveRelay.disable()
led = RGBLight(15,14,13)
#creates a servo object with the method move to move it the way that we described in class
#greenPin = Pin(13,Pin.OUT)
#greenPin.value(1)

#i2c= I2C(1, scl = Pin(7), sda = Pin(6))
#sensor = tsl2561.TSL2561(i2c)

#Creates the light sensor on the correct bus and assignes it to the lightSensor variable
lightSensor = lightSensor(1,7,6)
lightSensor = lightSensor.returnSensor()

#Makes a simple powerRelay object for both the pump and valve which has the methods
#enable and disable

pumpRelay = powerRelay(22)
servo = servoMove(27,pumpRelay)
#clockPowerPin = Pin(3,Pin.OUT)
#clockPowerPin.value(1)

#clock = clock(0,5,4)

#Moves the servo holds it into the second position for 12 seconds and then moves back
servo.move()
#Enables the pump for 2 seconds then shuts it off

sleep(5)
#Takes meassurments with the green lights thw first parameter is the color the second parameter is how
#long the sensor waits after the light turns on to take meassuments, the third parameter is the lightSensor
#The fourth and final parameter is just how many sets of meassurments you want to take
led.takeMeassurments("green",0.5,lightSensor,5)


#Turns on the valve for 2 seconds then turns it off
valveRelay.enable()

sleep(60)

valveRelay.disable()



