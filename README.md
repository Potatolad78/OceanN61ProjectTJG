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

When collecting data from the sensor, there is a single file on the Pi that contains the data: results.txt. This 
file will contain averaged results. This format focuses on user readability. Each average is taken from three 
averages of five samples to ensure accuracy and precision.
In the future, we aim to have the ability to copy this file directly into an Excel file for instant mapping.
