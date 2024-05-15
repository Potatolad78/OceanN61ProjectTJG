from machine import Pin
from time import sleep
from picozero import RGBLED
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
    

