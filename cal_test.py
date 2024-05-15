import tsl2561
from machine import Pin, I2C 
from RGBLightLibrary import RGBLight
from time import sleep
from servo import Servo



f = open("results.txt", "a")

average = 0
totalAverage = 0
i2c= I2C(1, scl = Pin(7), sda = Pin(6))
print(i2c.scan())

LED = RGBLight(0,1,2)
sensor = tsl2561.TSL2561(i2c)
servoPin = Pin(3, Pin.OUT)
servo = Servo(servoPin)

servo.write(80)
sleep(1)
servo.write(-50)
LED.turnOnPhenolRed()
sleep(5)
LED.turnOffPhenolRed()
def takeMeassurments(color, sleepTime):
    average = 0
    totalAverage = 0
    if(color == "red"):
        f.write("RED: ")
        LED.turnOnRed(255)
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
        LED.turnOffRed();
        f.write("Total Average:" + str(totalAverage / 3) + " Sleep Time: " + str(sleepTime)+ " \n")
        f.write("\n")
    elif(color == "green"):
        sleep(sleepTime)
        f.write("GREEN: ")
        LED.turnOnGreen(255)
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
        LED.turnOffGreen();
        f.write("Total Average:" + str(totalAverage / 3) + " Sleep Time: " +  str(sleepTime)+" \n")
        f.write("\n")
        
    elif(color == "blue"):
        f.write("BLUE: ")
        LED.turnOnBlue(255)
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
        LED.turnOffBlue();
        f.write("Total Average:" + str(totalAverage / 3) + " Sleep Time: " +  str(sleepTime)+" \n")
        f.write("\n")
    elif(color == "purple"):
        sleep(sleepTime)
        f.write("PURPLE: ")
        LED.turnOnPurple()
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
        LED.turnOffPurple();
        f.write("Total Average:" + str(totalAverage / 3) + " Sleep Time: " +  str(sleepTime)+ " \n")
        f.write("\n")

for i in range(5):
    f.write("Test" + str(i) + "\n")
    #takeMeassurments("green", 0.5)
    takeMeassurments("purple", 0.5)
f.close()
