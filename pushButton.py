import RPi.GPIO as GPIO
from time import sleep
import subprocess

GPIO.setmode(GPIO.BOARD)

GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(10) == GPIO.HIGH:
        print("Button pushed")
        subprocess.call(["python3", "/home/pi/Desktop/CE4171/PI_device.py"])
        sleep(0.2)