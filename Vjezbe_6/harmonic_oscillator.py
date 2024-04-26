import numpy as np
import matplotlib.pyplot as plt

#zad1
class HarmonicOscillator:
    def __init__(self, m, k, x0, v0, dt=0.01):
        self.m=m
        self.k=k
        self.x0=x0
        self.v0=v0
        self.dt=dt
        self.akceleracija=[]
        self.polozaj=[]
        self.brzina=[]
        self.t=[]

    def eulerova_metoda(self, t): 
        time=np.arange(0, t, self.dt)
        for t0 in time:
            a=-(self.k/self.m)*self.x0
            self.akceleracija.append(a)
            self.v0=self.v0+a*self.dt
            self.brzina.append(self.v0)
            self.x0=self.x0+self.v0*self.dt
            self.polozaj.append(self.x0)
            self.t.append(t0)
        return self.akceleracija, self.brzina, self.polozaj, self.t 
        
    def plot_graf(self): 
        plt.subplot(1,3,1)
        plt.title("x-t")
        plt.xlabel('t[s]')
        plt.ylabel('x[m]')
        plt.plot(self.t,self.polozaj)
        plt.subplot(1,3,2)
        plt.title("v-t")
        plt.xlabel('t[s]')
        plt.ylabel('v[m/s]')
        plt.plot(self.t,self.brzina)
        plt.subplot(1,3,3)
        plt.title("a-t")
        plt.xlabel('t[s]')
        plt.ylabel('a[$\mathrm{m/s^2}$]')
        plt.plot(self.t,self.akceleracija)
        plt.tight_layout()
        plt.show()
    
#zad2
    def period1(self):
        self.T=2*np.pi*np.sqrt(self.m/self.k)
        print(self.T)
        return self.T
    
    def period2(self):
        initial_position=self.x0
        period=0
        while True:
            a=-(self.k/self.m)*self.x0
            self.akceleracija.append(a)
            self.v0=self.v0+a*self.dt
            self.brzina.append(self.v0)
            self.x0=self.x0+self.v0*self.dt
            period+=self.dt
            if self.x0>=initial_position:
               if period==self.dt:
                   continue  
               else:
                   break
        print(period)
        return period