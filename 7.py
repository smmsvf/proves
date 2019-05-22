#import de les llibreries especifiques del sensor de distància
#que fem servir com a comptapersones.
'''
import dv12
posarem a una funcio el codi del sensor
acumulem les dades cada 10 dades i les enviem
adaptacio a un sensor de temperatura i humitat
'''
import time
import cayenne.client
from random import randint
from time import sleep


def cayene(valors):
    temperatura = valors[0]
    humitat = valors[1]
    client.virtualWrite(1,temperatura,"temp","C")
    client.virtualWrite(2,humitat)
    
def lectura():
    #codi del sensor dv12 per Bellermann temperatura i humitat
    temperatura = randint(10,35)
    humitat = randint(50,100)
    return temperatura,humitat

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME = "cabb3650-7c77-11e9-beb3-736c9e4bf7d0"
MQTT_PASSWORD = "0abe0b568fd0ba4a0648c59c7d5a3a71ec534e7d"
MQTT_CLIENT_ID = "e42233f0-7c77-11e9-beb3-736c9e4bf7d0"

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

#codi principal

while True:
    client.loop()
    valors=lectura()
    if valors[0] > 30 and valors[1] > 80:
        print(valors)
        cayene(valors)
    sleep(1)
