#može se i na malo lakši način
import numpy as np
import matplotlib.pyplot as plt

class Sustav:
    def __init__(self, m1, m2, x1=(0,0), x2=(0,0), v1=(0,0), v2=(0,0), dt=1):
        self.m1=m1
        self.m2=m2
        self.x1=np.array(x1)
        self.x2=np.array(x2)
        self.v1=np.array(v1)
        self.v2=np.array(v2)
        self.dt=dt*24*60*60 
        self.listx1=[]
        self.listx2=[]
        self.g=-9.81
        self.G=6.67408*(10**(-11)) 
        
    def Euler(self, trajanje):
        trajanje=trajanje*24*60*60
        broj_koraka=int(trajanje/self.dt)

        for i in range(broj_koraka):
            a1=(-self.G*self.m2/(np.linalg.norm(self.x1-self.x2)**3))*(self.x1-self.x2)
            self.v1=self.v1+a1*self.dt
            self.x1=self.x1+self.v1*self.dt
            self.listx1.append(self.x1)
            
            a2=(-self.G*self.m1/(np.linalg.norm(self.x2-self.x1)**3))*(self.x2-self.x1)
            self.v2=self.v2+a2*self.dt
            self.x2=self.x2+self.v2*self.dt
            self.listx2.append(self.x2)
        
        return np.array(self.listx1), np.array(self.listx2)

t=365.242
mZ=5.9742*10**24
rZ=(1.486*10**11,0) 
vZ=(0,29783) 
mS=1.989*10**30 
rS=(0,0) 
vS=(0,0)
S1=Sustav(mZ,mS,rZ,rS,vZ,vS,1)

Z,S=S1.Euler(t)
for i in range(len(Z)):
    x_zemlja=Z[i,0]  
    y_zemlja=Z[i,1]  
    plt.plot(x_zemlja, y_zemlja, color='blue', marker='.')

for i in range(len(S)):
    x_sunce=S[i,0]  
    y_sunce=S[i,1]  
    plt.plot(x_sunce, y_sunce, color='yellow', marker='o')

plt.xlabel('X')
plt.ylabel('Y')
plt.show()