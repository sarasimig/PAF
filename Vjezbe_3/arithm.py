#zad 3 a)
import math

def arithm(listax):

    arsr=sum(listax)/len(listax)
    print("ovo je aritmetička sredina: {}".format(arsr))

    y=0
    for z in range(len(listax)):
        y=y+(listax[z]-arsr)**2
        
    devijacija=math.sqrt(y/(len(listax)*(len(listax)-1)))
    print("ovo je standardna devijacija: {}".format(devijacija))
