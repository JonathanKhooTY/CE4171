# CE4171
## **IoT Project Description**

This independent IoT project concept is meant to simulate a doorbell, with an integrated facial recognition camera system, to process the images taken upon a guest pressing the doorbell.

The image processing and inference model is stored separately in a Cloud Machine (_In this case, a local machine_) while the IoT device is held on a Raspberry Pi 4 Model B+, with additional peripherals such as a NoIR camera, a pushbutton, as well as a breadboard and circuitry to enable real-time user input. 

Wireless protocol (Specifically MQTT) was used to enable communication between the IoT Device and the Cloud Machine. The GPIO pins was used to simulate the doorbell button trigger.

***

## **Source Code Package Description**


The key modules include:
1) ###  _PI.device.py_
This is the code meant to send the image taken on the edge device, to the Cloud for inference.

2) ###  _PI_subscriber.py_
This is the code meant to receive the processed image from the Cloud, and display the processed image on the Raspberry Pi.

3) ###  _subscriber.py_
This is the code meant to run on the Cloud machine. It is a module which contains 2 channels, to receive the image from the Edge Device, as well as code to process the image, before sending it back to the Edge Device.

4) ### _init.sh_
This is a shell script that combines 1) and 2) on the Raspberry Pi, and serves to streamline the starting process for both the listener and sender channels.

***

## How To Operate

1) Git clone the repo to your local/cloud machine, and your IoT device.

2) Setup circuitry as seen in my [Youtube Video](https://youtu.be/GQaCXM83DeQ).

3) Connect to the Raspberry Pi via VNC viewer, on your local machine to be able to view the processed images after.

4) Type `python3 subscriber.py` on your local/Cloud machine. Import all required modules, if you face any error.

5) Type `./init.sh` on your Raspberry Pi/Edge Device to run both the listener and sender python scripts, as well as the pushbutton GPIO script. Import all required modules, if you face any error. If you are not able to execute `./init.sh`, type `sudo chmod +x init.sh` to enable execution of _init.sh_ script.

6) IoT edge device will now send an image to Cloud for image processing, before receiving the processed image back from Cloud.

***

## References
Facial recognition model design was adapted from [PyImageSearch](https://pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning/), utilizing OpenCV's publicly available DNN module, with the included Face_Detector modules.

GPIO wiring and coding was adapted from [razzpisampler](http://razzpisampler.oreilly.com/ch07.html).

MQTT knowledge adapted from various sources, such as [Steve's Internet Guide](http://www.steves-internet-guide.com/mqtt-python-beginners-course/).

