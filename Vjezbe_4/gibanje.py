import particle as prt
import numpy as np
import math
import matplotlib.pyplot as plt

p1=prt.Particle(20,50,0,0)

ndomet=p1.range(0.01)

def adomet(v0,kut1,x0,y0):
    kut2=np.radians(kut1)
    ay=-9.81 
    vx=v0*math.cos(kut2) 
    vy=v0*math.sin(kut2)
    d=x0+(vx*(-2*vy/ay))
    return d

print(adomet(20,50,0,0),ndomet)