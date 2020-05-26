from dotenv import load_dotenv # Used for settings storage only
import os # Used for settings storage only
import paho.mqtt.client as mqtt

# Reads from .env file in current folder and loads into OS environment 
# this is opitional and just used to save defining secrets/config in code file
load_dotenv() 

# Define 'constants'
BROKER_ADDRESS=os.getenv("MQTT_BROKER") or "test.mosquitto.org" # IP or host name
BROKER_TOPIC=os.getenv("MQTT_TOPIC") or "test/testdevice"
CLIENT_ID=os.getenv("CLIENT_ID2") or "PythonTestPublish"
CLIENT_USER=os.getenv("CLIENT_USER") # set to None if not present
CLIENT_PWD=os.getenv("CLIENT_PWD") # set to None if not present

############
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
########################################

############
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connection OK")
    else:
        print(f'Bad connection, rc={rc}')
########################################

print("Creating client instance")
client = mqtt.Client(CLIENT_ID) # create new instance
 # attach function to callbacks
client.on_publish = on_publish 
client.on_connect=on_connect

# set username and password if provided
if CLIENT_USER != None and CLIENT_PWD != None:
    client.username_pw_set(CLIENT_USER, CLIENT_PWD)

print("Requesting connection to broker")
client.connect(BROKER_ADDRESS) 

print("Publishing to topic")
ret = client.publish(BROKER_TOPIC,"on",qos=1,retain=True)