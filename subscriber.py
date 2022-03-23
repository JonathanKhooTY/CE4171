import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

import imutils
import numpy as np
import cv2
import wget
import os
#from google.colab.patches import cv2_imshow
#from IPython.display import display, Javascript
#from google.colab.output import eval_js
from base64 import b64decode


from PIL import Image, ImageDraw, ImageFont

MQTT_SERVER2 = "test.mosquitto.org"
MQTT_PATH2 = "testing045"
MQTT_SERVER = "test.mosquitto.org"
MQTT_PATH = "ef37917e08872c2f2a16d233ec4925ce"

#def imageProcessing(image_name):


# The callback for when the client receives a connect response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # on_connect() means that if we lose the connection and reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    f = open('output.jpg', 'wb')
    f.write(msg.payload)
    print('Image recevied')
    f.close()
    #print(msg.topic+" "+str(msg.payload))
    # more callbacks, etc

    image = cv2.imread('output.jpg')

    # resize it to have a maximum width of 400 pixels
    image = imutils.resize(image, width=400)
    (h, w) = image.shape[:2]
    
    prototxt = wget.download('https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt')
    model = wget.download('https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel')
    net = cv2.dnn.readNetFromCaffe(prototxt, model)
    
    image = imutils.resize(image, width=400)
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0)) 

    net.setInput(blob)
    detections = net.forward()

    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
		# compute the (x, y)-coordinates of the bounding box for the object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
		# draw the bounding box of the face along with the associated probability
            text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
            cv2.putText(image, text, (startX, y),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

    cv2.imwrite('processedpic.jpg',image)
    
    #Include deletion of models
    os.remove('res10_300x300_ssd_iter_140000.caffemodel')
    os.remove('deploy.prototxt')

    #Sending updated picture back to client
    f=open("processedpic.jpg", "rb") #3.7kiB in same folder
    fileContent = f.read()
    byteArr = bytearray(fileContent)

    publish.single(MQTT_PATH2, byteArr, hostname=MQTT_SERVER2)
    print('\nRetransmission of processed pic complete\n')
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever() 