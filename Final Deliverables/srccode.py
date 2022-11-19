import wiotp.sdk.device
import time
import random

myConfig = { 
    "identity": {
        "orgId": "ml1dq0",
        "typeId": "NodeMCU",
        "deviceId":"12345"
    },
    "auth": {
        "token": "12345678987654321"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IOT platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    if(m=="motoron"):
        print("Motor is switched on")
    elif(m=="motoroff"):
        print("Motor is switched off")
    print(" ")

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(-20,125)
    hum=random.randint(0,100)
    moist=random.randint(0,100)
    myData={'Temperature':temp, 'Humidity':hum, 'Moisture':moist }
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
