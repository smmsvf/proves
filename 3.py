#import de les llibreries especifiques del sensor de distància
#que fem servir com a comptapersones.
'''
import dv345
posarem a una funcio el codi del sensor
'''

from random import randrange
from time import sleep


def distancia():
    #codi del sensor subgerida per Bellermann
    distancia = randrange(0,4)
    return distancia

#codi principal
#faig una crida a la funcio distancia

comptador = 0
booleana = True

while booleana:
    print(distancia())
    comptador = comptador + 1
    sleep(1)
if comptador == 10:
    booleana = False
