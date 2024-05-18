MANUAL:

HOW TO TURN ON/RUN SENSOR:

When looking at how to turn on the sensor and run said sensor there are multiple ways you could go about it.
The way that is easiest and intended for use simply involves turning on the battery that powers the microcontoller.
This will turn on the controller and cause it to instantly start running the code on boot. However this is not the
only way to turn on/run the sensors. If you would like to modify the code for whatever reason you can simply plug
the pi into a computer with a usb2.0 adapter and stop code execution. From there on out you will be able to modify
the code in main.py and when you are done simply unplud the adaptor and plug back in the power. If done corretly 
you will see that the code that you wrote will be running on the py starting at boot.

HOW TO RETRIEVE DATA FROM SENSOR:

When collecting data from the sensor there are two files that you can look at on the pi that contain said data.
The first file is results.txt, this file will contain averaged results that will be dated with month,day,year,hour,
minute taken. This will be the easiest way to read the data as it will be in a format that is focused on user 
readability. Each average is taken from 3 averages of 5 samples to make sure that it is accurate and percise. The other 
file will be full.txt, this will contain each and every average taken. This means that it will be much harder to read 
however it will be useful for debuging purposes if you change our code or are seeing reading that do not make sense.
We would like to soon have the ability to just copy the file over into an excel file and to instantly map it from there.
