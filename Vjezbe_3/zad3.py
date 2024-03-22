#zad 3 b)
import numpy as np
import math
import statistics

def aritmetickasr(listax):
    aritmeticka_sredina=np.mean(listax)
    print("ovo je aritmetička sredina: {}".format(aritmeticka_sredina))
aritmetickasr([1,2,3,4,5,6,7,8,9,10])

def devijacija(listax):
    standardna_devijacija=(statistics.stdev(listax)/math.sqrt(len(listax)))
    print("ovo je standardna devijacija: {}".format(standardna_devijacija))
devijacija([1,2,3,4,5,6,7,8,9,10])

#način uz korištenje našeg napravljenog modula
import arithm as ari
ari.arithm([1,2,3,4,5,6,7,8,9,10])


