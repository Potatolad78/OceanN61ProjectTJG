from RGBLightLibrary import RGBLight, servoMove, powerRelay, lightSensor, clock
from machine import Pin, I2C
from time import sleep
import tsl2561
#Creates an LED object for you to use
led = RGBLight(13,14,15)

#creates a servo object with the method move to move it the way that we described in class
servo = servoMove(27)


#i2c= I2C(1, scl = Pin(7), sda = Pin(6))
#sensor = tsl2561.TSL2561(i2c)

#Creates the light sensor on the correct bus and assignes it to the lightSensor variable
lightSensor = lightSensor(1,7,6)
lightSensor = lightSensor.returnSensor()

#Makes a simple powerRelay object for both the pump and valve which has the methods
#enable and disable
valveRelay = powerRelay(22)

pumpRelay = powerRelay(28)

#clockPowerPin = Pin(3,Pin.OUT)
#clockPowerPin.value(1)

#clock = clock(0,5,4)

#Moves the servo holds it into the second position for 12 seconds and then moves back
servo.move()

#Enables the pump for 2 seconds then shuts it off
pumpRelay.enable()
sleep(2)
pumpRelay.disable()

#Takes meassurments with the green lights thw first parameter is the color the second parameter is how
#long the sensor waits after the light turns on to take meassuments, the third parameter is the lightSensor
#The fourth and final parameter is just how many sets of meassurments you want to take
led.takeMeassurments("green",0.5,lightSensor,5)


#Turns on the valve for 2 seconds then turns it off
valveRelay.enable()

sleep(2)

valveRelay.disable()




