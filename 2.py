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

while True:
    print(distancia())
    sleep(1)
