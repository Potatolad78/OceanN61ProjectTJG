from machine import Pin, I2C 
from time import sleep
from picozero import RGBLED
from servo import Servo
import tsl2561
import urtc
"""
Created by Drew Rigby for group The Melting Pot
Version 1.1 5/31/24
Feel free to use this API for whatever you need just make sure to credit if used :)

Includes: All needed functionality needed for TJG pH sensor.

How to import:
from RGBLightLibrary import followed by the classes that you need to import 
"""

"""
Abstracts a RGB Light that is common ground and allows the user to manipulate it

init(redPin,greenPin,blue1):

Input parameters would be the gpio pins you have to red , green, and blue in this specific 
order and returns an object that represents the RGB light

Functions:
    
turnOnGreen(level):
Turns on the green LED at a specified brightness level.
Input: level - an integer (0-255) representing the brightness level of the green LED.
    
turnOnRed(level):
Turns on the red LED at a specified brightness level.
Input: level - an integer (0-255) representing the brightness level of the red LED.
    
turnOnBlue(level):
Turns on the blue LED at a specified brightness level.
Input: level - an integer (0-255) representing the brightness level of the blue LED.
    
turnOffGreen():
Turns off the green LED.
No input parameters.
    
turnOffRed():
Turns off the red LED.
No input parameters.
    
turnOffBlue():
Turns off the blue LED.
No input parameters.
    
turnOnPurple():
Turns on the red and blue LEDs to simulate purple light.
No input parameters.
    
turnOffPurple():
Turns off the red and blue LEDs to disable purple light.
No input parameters.
    
turnOnCyan():
Turns on the blue and green LEDs to simulate cyan light.
No input parameters.
    
turnOffCyan():
Turns off the blue and green LEDs to disable cyan light.
No input parameters.
    
turnOnBrown():
Turns on the red and green LEDs to simulate brown light.
No input parameters.
    
turnOffBrown():
Turns off the red and green LEDs to disable brown light.
No input parameters.
    
turnOnWhite():
Turns on all LEDs to simulate white light.
No input parameters.
    
turnOffWhite():
Turns off all LEDs.
No input parameters.
    
cycleThroughLights():
Cycles through the red, green, and blue LEDs, turning each on for 5 seconds in sequence.
No input parameters.
    
takeMeassurments(color, sleepTime, sensor, loop):
Takes sensor measurements for a specified color LED over a number of loops.
Input: color - a string representing the color to measure ('red', 'green', 'blue', 'purple').
sleepTime - an integer representing the time to wait between measurements.
sensor - an object representing the sensor to read values from.
loop - an integer representing the number of measurement loops to perform.


Example of use:

led = RGBLight(1,2,3)

led.turnOnPurple()

sleep(2)

led.turnOffPurple()

This would turn on the red and blue lights to simulate purple for two seconds
then would turn it off
"""
class RGBLight():
    #Init allows for input of three pins that light up each line
    #Needs to hand in pins from the user code
    
    def __init__(self,red1,green1,blue1):
        self.RGBLight = RGBLED(red = red1, green = green1, blue = blue1)
        
    #Turns on the green led
    def turnOnGreen(self,level):
        self.RGBLight.color = (self.RGBLight.color[0],level,self.RGBLight.color[2])
    
    #Turns on the red led
    def turnOnRed(self,level):
        self.RGBLight.color = (level,self.RGBLight.color[1],self.RGBLight.color[2])
    
    #Turns on the blue led
    def turnOnBlue(self,level):
        self.RGBLight.color = (self.RGBLight.color[0],self.RGBLight.color[1],level)
    
    #Turns off the green led
    def turnOffGreen(self):
        self.RGBLight.color = (self.RGBLight.color[0],0,self.RGBLight.color[2])
    
    #Turns off the red led
    def turnOffRed(self):
        self.RGBLight.color = (0,self.RGBLight.color[1],self.RGBLight.color[2])
    
    #Turns off the blue led
    def turnOffBlue(self):
        self.RGBLight.color = (self.RGBLight.color[0],self.RGBLight.color[1],0)
    
    #Turns on Red and Blue lights to simulate purple light
    def turnOnPurple(self):
        self.turnOnRed(255)
        self.turnOnBlue(255)
    
    #Turns off Red and Blue lights to disable purple light
    def turnOffPurple(self):
        self.turnOffRed()
        self.turnOffBlue()
    
    #Turns on blue and green to simulate cyan
    def turnOnCyan(self):
        self.turnOnBlue()
        self.turnOnGreen()
        
    #Turns off blue and green to simulate cyan
    def turnOffCyan(self):
        self.turnOffBlue()
        self.turnOffGreen()
    
    #Turns on red and green to simulate brown
    def turnOnBrown(self):
        self.turnOnRed()
        self.turnOnGreen()
    
    #Turns off red and green
    def turnOffBrown(self):
        self.turnOffRed()
        self.turnOffGreen()

    #Turns on all LEDS to simulate white
    def turnOnWhite(self):
        self.turnOnRed()
        self.turnOnGreen()
        self.turnOnBlue()
    
    #Turns off all LEDS
    def turnOffWhite(self):
        self.turnOffRed()
        self.turnOffGreen()
        self.turnOffBlue()
    #Turns on lights in a order of RGB
    #Five seconds between light usage
    def cycleThroughLights(self):
        #Turns off all of the lights
        self.turnOffRed()
        self.turnOffGreen()
        self.turnOffBlue()
        
        #Turns on the red light then waits 5 seconds
        self.turnOnRed()
        sleep(5)
        
        #Turns off red and then turns on green for five seconds
        self.turnOffRed()
        self.turnOnGreen()
        sleep(5)
        
        #Turns off green then turns on blue for five seconds
        self.turnOffGreen()
        self.turnOnBlue()
        sleep(5)
        
        #finishes off by turning off the blue led
        self.turnOffBlue()
    def takeMeassurments(self,color, sleepTime, sensor,loop):
        f = open("results.txt", "a")
        for i in range(loop):
            f.write("Test" + str(i + 1) + "\n")
            average = 0
            totalAverage = 0
            if(color == "red"):
                f.write("RED: ")
                self.turnOnRed(255)
                sensor.read()
                sleep(sleepTime)
                for j in range(3):
                    for i in range(5):
                        #print(sensor.read())
                        average += sensor.read()
                        #sleep(1)
                    average = average/5
                    totalAverage += average
                    f.write("Average" + str(j + 1)+ ": " + str(average)+ " ")
                    average = 0
                self.turnOffRed();
                f.write("Total Average:" + str(totalAverage / 3) + " Sleep Time: " + str(sleepTime)+ " \n")
                f.write("\n")
            elif(color == "green"):
                sleep(sleepTime)
                f.write("GREEN: ")
                self.turnOnGreen(255)
                sensor.read()
                sleep(sleepTime)
                for j in range(3):
                    for i in range(5):
                        #print(sensor.read())
                        average += sensor.read()
                        #sleep(1)
                    average = average/5
                    totalAverage += average
                    f.write("Average" + str(j + 1)+ ": " + str(average)+ " ")
                    average = 0
                self.turnOffGreen();
                f.write("Total Average:" + str(totalAverage / 3) + " Sleep Time: " +  str(sleepTime)+" \n")
                f.write("\n")
                
            elif(color == "blue"):
                f.write("BLUE: ")
                self.turnOnBlue(255)
                sensor.read()
                sleep(sleepTime)
                for j in range(3):
                    for i in range(5):
                        #print(sensor.read())
                        average += sensor.read()
                        #sleep(1)
                    average = average/5
                    totalAverage += average
                    f.write("Average" + str(j + 1)+ ": " + str(average)+ " ")
                    average = 0
                self.turnOffBlue();
                f.write("Total Average:" + str(totalAverage / 3) + " Sleep Time: " +  str(sleepTime)+" \n")
                f.write("\n")
            elif(color == "purple"):
                sleep(sleepTime)
                f.write("PURPLE: ")
                self.turnOnPurple()
                sensor.read()
                sleep(sleepTime)
                for j in range(3):
                    for i in range(5):
                        #print(sensor.read())
                        average += sensor.read()
                        #sleep(1)
                    average = average/5
                    totalAverage += average
                    f.write("Average" + str(j + 1)+ ": " + str(average)+ " ")
                    average = 0
                self.turnOffPurple();
                f.write("Total Average:" + str(totalAverage / 3) + " Sleep Time: " +  str(sleepTime)+ " \n")
                f.write("\n")
        f.close()
"""
Abstracts the creation of a servo and allows the user to move the servo between 
100 to -30 back to 100

init(servoPinNum, OPTIONAL pumpRelay):
Input parameter of gpio pin the servo is using along with the optional inclusion
of a pumpRelay. If the pump relay is passed it will be activated in sequence with
the servo when using the move function. If it is not included then the servo will
just move as intended.

Functions:

move():
No Input parameters. If pumpRelay was given then the servo will move to 100 then
turn on the pump for two seconds then turn it off and in another 3 seconds will move
to the orginal position of -30. If the pumpRelay is not included then the servo will
move to 100 and wait 5 seconds then move back to the start position of -30

Example of use using pumpRelay:

pumpRelay = powerRelay(22)
servo = servoMove(27,pumpRelay)

servo.move()

The servo will act acording to the description of move

Example of use without using pumpRelay:

servo = servoMove(27)

servo.move()

The servo will act in accordince to the description of move
"""
class servoMove:
    def __init__(self, servoPinNum, pumpRelay = None):
        servoPin = Pin(servoPinNum, Pin.OUT)
        self.servo = Servo(servoPin)
        self.pumpRelay = pumpRelay
    
    def move(self):
        self.servo.write(-30)
        sleep(0.1)
        self.servo.write(100)
        if self.pumpRelay:
            self.pumpRelay.enable()
            sleep(2)
            self.pumpRelay.disable()
            sleep(3)
            self.servo.write(-30)
        else:
            sleep(5)
            self.servo.write(100)
""" 
Abstracts the creation of a relay that allows for simpler interaction with the 
device

init(pinNum):
Input parameter of the common pin in the relay. Creates the powerRelay object

Functions:

enable():
No input parameters and essentially allows the user to turn on the relay

disable():
No input parameters and essentially allows the user to turn off the relay


Example of use:
pumpRelay = powerRelay(22)

pumpRelay.enable()

sleep(2)

pumpRelay.disable()

This should turn on the relay for two seconds then turn it off

"""        
class powerRelay:
    def __init__(self, pinNum):
        self.relay = Pin(pinNum, Pin.OUT)
        
    def enable(self):
        self.relay.value(1)
    
    def disable(self):
        self.relay.value(0)
"""
Abstracts the creation of the light sensor tsl2561
NOTE: Should only be used if you are also planning on returning the sensor. This
class does not have any functions that allow you to do anything with the sensor.

init(busNum,sclPin, sdaPin):
Input parameters are the number of the bus that you are using for the scl and sda
pins and the pins themselves in the above order. Switching the order will cause 
the sensor to throw errors

Functions:

returnSensor():
No input parameter. Returns the sensor that you have created.

Example of use:
lightSensor = lightSensor(1,7,6)
lightSensor = lightSensor.returnSensor()

print(lightSensor.read())

Console: 
1124
"""

class lightSensor:
    def __init__(self,busNum,sclPin,sdaPin):
        i2c= I2C(busNum, scl = Pin(sclPin), sda = Pin(sdaPin))
        self.sensor = tsl2561.TSL2561(i2c)
    def returnSensor(self):
        return self.sensor
"""   Disregard This as a work in progress DOES NOT WORK 
class clock:
    def __init__(self, busNum, sclPin, sdaPin):
        i2c =I2C(busNum, scl = Pin(sclPin), sda = Pin(sdaPin))
        self.clock = urtc.DS3231(i2c)
    def returnClock(self):
        return self.clock
"""
