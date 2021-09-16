import paho.mqtt.client as mqttClient
import time

def on_connect(client, userdata, flags, rc):

    if rc == 0:

        print("Connected to broker")

        global Connected                
        Connected = True                

    else:

        print("Connection failed")

def on_message(client, userdata, message):
    print (message.payload.decode("utf-8"))
    with open('./results.txt','a+') as f:
         f.write(str(message.payload.decode("utf-8")) + "\n")

Connected = False   

broker_address= "104.210.87.145"  


client = mqttClient.Client("Python")              
client.on_connect= on_connect                  
client.on_message= on_message                      
client.connect(broker_address)
client.subscribe("data") 
client.loop_forever() 