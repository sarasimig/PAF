import math
import matplotlib.pyplot as plt
import numpy as np

class Particle:
    def __init__(self,v0,kut,x,y):
        self.v0=v0
        self.kut=kut
        self.x=x
        self.y=y
        self.vx=self.v0*math.cos(np.radians(self.kut))
        self.vy=self.v0*math.sin(np.radians(self.kut))
        self.xpocetna=x
        self.ypocetna=y
        self.vpocetna=v0
        self.vxpocetna=self.vx
        self.vypocetna=self.vy
        self.listax=[self.x]
        self.listay=[self.y]
       
    def printinfo(self):
        print('brzina čestice:',self.v0)
        print('kut oklona čestice:',self.kut)
        print('položaj čestice:',self.x,self.y)
        
    def reset(self):
        self.v0=self.vpocetna
        self.vx=self.vxpocetna
        self.vy=self.vypocetna
        self.x=self.xpocetna
        self.y=self.ypocetna

    def __move(self,dt):
        ax=0
        ay=-9.81
        self.vx=self.vx+ax*dt
        self.x=self.x+self.vx*dt
        self.vy=self.vy+ay*dt
        self.y=self.y+self.vy*dt
        return self.x,self.y

    def range(self,dt):
        while self.y>=0:
            self.__move(dt)
        return self.x
    
    def plot_trajectory(self,dt):
        self.reset()
        while self.y>=0:
            self.__move(dt)
            self.listax.append(self.x)
            self.listay.append(self.y)
        plt.plot(self.listax,self.listay)
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
        plt.title('x-y graf')
        plt.show()


        

        
    