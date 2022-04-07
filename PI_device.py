import paho.mqtt.publish as publish
from picamera import PiCamera
from time import sleep



MQTT_SERVER = "test.mosquitto.org"
MQTT_PATH = "ef37917e08872c2f2a16d233ec4925ce"


camera = PiCamera()
camera.resolution = (400,400)
camera.start_preview()
sleep(1)
camera.capture('index.png')
sleep(1)

f = open('index.png','rb')
fileContent = f.read()
byteArray = bytearray(fileContent)

publish.single(MQTT_PATH,byteArray, hostname=MQTT_SERVER)
print('Image sent to Cloud!')