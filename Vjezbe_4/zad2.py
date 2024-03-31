import particle as prt
import numpy as np
import math
import matplotlib.pyplot as plt

ndomet=[]
adomet=[]

def andomet(v0,kut1,x0,y0):
    kut2=np.radians(kut1)
    ay=-9.81 
    vx=v0*math.cos(kut2) 
    vy=v0*math.sin(kut2)
    d=x0+(vx*(-2*vy/ay))
    return d
analitickid=andomet(10,60,0,0)

#do 0.1 na x osi je primjer grafa u prezentaciji
t1=0.0001
while t1<=0.1:
    adomet.append(analitickid)
    t1=t1+0.0001


t2=0.0001
while t2<=0.1:
    t2=t2+0.0001
    p1=prt.Particle(10,60,0,0)
    numerickid=p1.range(t2)
    ndomet.append(numerickid)
  
err=((abs(np.array(adomet)-np.array(ndomet)))/(np.array(adomet)))*100

t=[]
t3=0.0001
while t3<=0.1:
    t.append(t3)
    t3=t3+0.0001

plt.plot(t,err,color='orange')
plt.xlabel("dt [s]")
plt.ylabel("Absolute relative error [%]")
plt.title("Absolute relative error for range of projectile")
plt.show()