import paho.mqtt.publish as publish

MQTT_SERVER = "test.mosquitto.org"
MQTT_PATH = "ef37917e08872c2f2a16d233ec4925ce"

f=open("image_test.jpg", "rb") #3.7kiB in same folder
fileContent = f.read()
byteArr = bytearray(fileContent)

publish.single(MQTT_PATH, byteArr, hostname=MQTT_SERVER)