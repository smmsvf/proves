#import de les llibreries especifiques del sensor de distància
#que fem servir com a comptapersones.
'''
import dv345
posarem a una funcio el codi del sensor
acumulem les dades cada 10 dades i les enviem
'''

from random import randrange
from time import sleep

def grafica(llista):
    #amb matplotlib.pyplot graficarem les dades
    pass

def distancia():
    #codi del sensor subgerida per Bellermann
    distancia = randrange(0,4)
    return distancia

#codi principal
#faig una crida a la funcio distancia

comptador = 0
booleana = True
llista = []

while booleana:
    llista.append(distancia())
    comptador += 1
    if comptador == 10:
        print(llista)
        grafica(llista) #llista amb 10 valors
        comptador = 0
        llista=[]
    sleep(1)
