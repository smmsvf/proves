#import de les llibreries especifiques del sensor de distància
#que fem servir com a comptapersones.
'''
import dv12
posarem a una funcio el codi del sensor
acumulem les dades cada 10 dades i les enviem
adaptacio a un sensor de temperatura i humitat
'''

from random import randrange
from time import sleep

def grafica(llista1,llista2):
    #amb matplotlib.pyplot graficarem les dades
    pass

def lectura():
    #codi del sensor dv12 per Bellermann temperatura i humitat
    temperatura = randrange(10,35)
    humitat = randrange(50,100)
    return temperatura,humitat

#codi principal
#faig una crida a la funcio distancia

comptador = 0
temperatura = []
humitat = []
valors = 0

while True:
    valors=lectura()
    temperatura.append(valors[0])
    humitat.append(valors[1])
    print(valors,temperatura,humitat)
    comptador += 1
    if comptador == 10:
        grafica(temperatura,humitat) #llista amb 10 valors
        comptador = 0
        temperatura=[]
        humitat = []
    sleep(1)
