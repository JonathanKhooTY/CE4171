import paho.mqtt.publish as publish

MQTT_SERVER = "test.mosquitto.org"
MQTT_PATH = "ef37917e08872c2f2a16d233ec4925ce"

f = open('index.png','rb')
fileContent = f.read()
byteArray = bytearray(fileContent)

publish.single(MQTT_PATH,byteArray, hostname=MQTT_SERVER)