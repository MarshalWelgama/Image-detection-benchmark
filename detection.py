# Author: Marshal Welgama
import cvlib as cv
import cv2
import urllib.request
import numpy as np
import time
import _thread
import paho.mqtt.client as mqtt #import the client1
broker_address="104.210.87.145" 
client = mqtt.Client("P1") #create new instance
print("connecting to broker")
client.connect(broker_address) #connect to broker
print("connected")
client.subscribe("data")


def detect_face(threadName):
    global num_threads
    try:
 
        start = time.process_time()
        req = urllib.request.urlopen('https://100k-faces.glitch.me/random-image')
        
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        image = cv2.imdecode(arr, -1) 
        faces, confidences = cv.detect_face(image)
        for face,conf in zip(faces,confidences):
            (startX,startY) = int(face[0]),int(face[1])
            (endX,endY) = int(face[2]),int(face[3])
            cv2.rectangle(image, (startX,startY), (endX,endY), (0,255,0), 2)    

        cv2.imwrite("{}.jpg".format(threadName), image)
        end = time.process_time()  
        elapsed = end - start
        print(elapsed, "done")
        client.publish("data","{}".format(elapsed))
        cv2.destroyAllWindows()
  
    except:
        print('ERROR OCCURED: life goes on..')
 

while 1:
    detect_face("single")