from machine import Pin, I2C 
from time import sleep
from picozero import RGBLED
from servo import Servo
import tsl2561
#Created by Drew Rigby for group The Melting Pot
#Version 1.0 4/24/24
#Feel free to use this API for whatever you need just make sure
#to credit if used :)
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
    
    def turnOnPhenolRed(self):
        self.turnOnGreen(70)
        self.turnOnBlue(255)
        
    def turnOffPhenolRed(self):
        self.turnOffGreen()
        self.turnOffBlue()
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
class servoMove:
    def __init__(self, servoPinNum):
        servoPin = Pin(servoPinNum, Pin.OUT)
        self.servo = Servo(servoPin)
        startAngle = 100;
        endAngle = -30
        print(servoPin)
    
    def move(self):
        self.servo.write(100)
        sleep(1)
        self.servo.write(-30)
        sleep(1)
        self.servo.write(100)
        
class powerRelay:
    def __init__(self, pinNum):
        self.relay = (pinNum, Pin.OUT)
        
    def enableRelay(self):
        self.relay.value(1)
    
    def disableRelay(self):
        self.relay.value(0)
        
    
class lightSensor:
    def __init__(self,outPin,sclPin,sdaPin):
        i2c= I2C(outPin, scl = Pin(sclPin), sda = Pin(sdaPin))
        self.sensor = tsl2561.TSL2561(i2c)
    def returnSensor(self):
        return self.sensor
