import paho.mqtt.client as mqtt
MQTT_SERVER = "test.mosquitto.org"
MQTT_PATH = "m0difiedef37917e08872c2f2a16d233ec4925ce"

# The callback for when the client receives a connect response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # on_connect() means that if we lose the connection and reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    f = open('modifiedData.jpg','wb')
    f.write(msg.payload)
    f.close()
    print('Facial recognition complete! Image received from Cloud!')
    #print(msg.topic+" "+str(msg.payload))
    # more callbacks, etc

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever() 