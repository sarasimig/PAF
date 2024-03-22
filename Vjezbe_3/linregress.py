#zad 4
import numpy as np
import matplotlib.pyplot as plt
import math

M=[0.052, 0.124, 0.168, 0.236, 0.284, 0.336] #vrijednosti na y osi
phi=[0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] #vrijednosti na x osi

#prvo želimo doći do koeficijenta a iz formule y=a*x+b
#za izračunati a potrebna nam je aritmetička sredina umoška x*y iz dvije liste
def arsr_xy(lista1,lista2,len1):
    listaxy=[]
    for i in range(len1):
        xy=lista1[i]*lista2[i]
        listaxy.append(xy)
    return np.mean(listaxy)

aritmeticka_sr_xy=arsr_xy(phi,M,len(M))

#potrebna nam je i aritmetička sredina kvadratnih vrijednosti liste koja sadrži vrijednosti na x osi
def arsr_kvadrat(lista,len2):
    lista_xkvadrat=[]
    for i in range(len2):
        xkvadrat=lista[i]*lista[i]
        lista_xkvadrat.append(xkvadrat)
    return np.mean(lista_xkvadrat)

aritmeticka_sr_xkvadrat=arsr_kvadrat(phi,len(phi)) 

a=aritmeticka_sr_xy/aritmeticka_sr_xkvadrat #a po formuli arsr xy/arsr x**2

aritmeticka_sr_ykvadrat=arsr_kvadrat(M,len(M)) 

deviacija=math.sqrt(1/len(M)*((aritmeticka_sr_ykvadrat/aritmeticka_sr_xkvadrat)-a*a))

osy=[]
for i in range(len(phi)):
    y_element=a*phi[i] #y=ax+b, b=0
    osy.append(y_element)

plt.title('graf linearne regresije')
plt.scatter(phi,M,color='blue')
plt.plot(phi,osy,color='orange')
plt.xlabel('\u03A6''/[rad]')
plt.ylabel('M/[Nm]')
plt.show()