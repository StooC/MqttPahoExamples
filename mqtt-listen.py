from dotenv import load_dotenv # Used for settings storage only
import os # Used for settings storage only
import paho.mqtt.client as mqtt

# Reads from .env file in current folder and loads into OS environment 
# this is opitional and just used to save defining secrets/config in code file
load_dotenv() 

# Define 'constants'
BROKER_ADDRESS=os.getenv("MQTT_BROKER") or "test.mosquitto.org" # IP or host name
MQTT_TOPIC=os.getenv("MQTT_TOPIC") or "test/testdevice"
CLIENT_ID=os.getenv("CLIENT_ID1") or "PythonTestListen"
CLIENT_USER=os.getenv("CLIENT_USER") # set to None if not present
CLIENT_PWD=os.getenv("CLIENT_PWD") # set to None if not present

############
def on_message(client, userdata, message):
    print("----------------------------------------------------------------")
    print("| - message received: " ,str(message.payload.decode("utf-8")))
    print("| - message topic: ",message.topic)
    print("| - message qos: ",message.qos)
    print("| - message retain flag: ",message.retain)
    print("----------------------------------------------------------------")
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
client.on_message=on_message
client.on_connect=on_connect

# set username and password if provided
if CLIENT_USER != None and CLIENT_PWD != None:
    client.username_pw_set(CLIENT_USER, CLIENT_PWD)

print("Requesting connection to broker")
client.connect(BROKER_ADDRESS)

print("Subscribing to topic",MQTT_TOPIC)
client.subscribe(MQTT_TOPIC)

print("Waiting for connections and messages. (Ctrl-C to terminate)")
client.loop_forever()