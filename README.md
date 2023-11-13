# RaspberryPi-Arduino-i2c-Robot
This project connects a Raspberry Pi and Arduino Uno via i2c to control a robot.

## Getting Started
First you'll need a Raspberry Pi. For the sake of power efficiency, I recommend not using a Pi 5 as that draws too much power. However any other Pi can be used. An Arduino Uno R3 is recommended but others can be used. Follow the Wiring Diagram shown below.
To get started there's no need to install any libraries. First open the `i2c-robot` folder using the Arduino IDE 2.0 and upload the code. The code should then be ready to run. Make sure to have your Robot assembled and follow the wiring diagram shown below. Copy the Python code to the Pi and run it with `python3 i2c-robot.py`. However, make sure to have i2c enabled by running `sudo raspi-config` and then going to Interfaces and enable I2C. 

![i2c](https://github.com/sentairanger/RaspberryPi-Arduino-i2c-Robot/blob/main/i2c-robot_bb.png)
