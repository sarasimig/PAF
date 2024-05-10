import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, m, q, v0, x0, E, B, dt=0.01):
        self.m=m
        self.q=q
        self.v0=np.array(v0)
        self.x0=np.array(x0,dtype=float)
        self.E=np.array(E)
        self.B=np.array(B)
        self.dt=dt

    def trajectory(self, t):
        tlista=np.arange(0.0,t+self.dt,self.dt)
        n=len(tlista)
        x=[]
        y=[]
        z=[]

        for i in range(n):
            a=(self.q/self.m)*(self.E+np.cross(self.v0,self.B))
            self.v0=self.v0+a*self.dt
            self.x0=self.x0+self.v0*self.dt
            x.append(self.x0[0])
            y.append(self.x0[1])
            z.append(self.x0[2])
        return x, y, z

E=(0,0,0)
B=(0,0,1)
v0=(1.0,1.0,1.0)
x0=(0,0,0)

p1=Particle(0.5,1,v0,x0,E,B) #proton
p2=Particle(0.5,-1,v0,x0,E,B) #elektron

x1,y1,z1=p1.trajectory(33)
x2,y2,z2=p2.trajectory(33)

graf=plt.axes(projection="3d")
graf.view_init(20,20)
graf.plot(x1,y1,z1,label='p+',color='red')
graf.plot(x2,y2,z2,label='e-',color='blue')
graf.legend()
graf.set_xlabel('x')
graf.set_ylabel('y')
graf.set_zlabel('z')
plt.show()