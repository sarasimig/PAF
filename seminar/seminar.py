import numpy as np
import math

class Projectile:
    def __init__(self,kut,v0,m,dt,C,A=0.1,rho=1.293,x=0,y=0):
        self.kut=kut
        self.v0=v0
        self.vx=v0*math.cos(self.kut)
        self.vy=v0*math.sin(self.kut)
        self.x=x
        self.y=y
        self.dt=dt
        self.m=m
        self.rho=rho
        self.C=C 
        self.A=A
        self.listax=[0]
        self.listay=[0]
        
    def Rungekutta(self):
        while self.y>=0:
            k1vx=-np.sign(self.vx)*((self.rho*self.C*self.A)/(2*self.m))*(self.vx*self.vx)*self.dt
            k1vy=(-9.81-np.sign(self.vy)*((self.rho*self.C*self.A)/(2*self.m))*(self.vy*self.vy))*self.dt
            k1x=self.vx*self.dt
            k1y=self.vy*self.dt

            k2vx=-np.sign(self.vx+(k1vx/2))*((self.rho*self.C*self.A)/(2*self.m))*((self.vx+(k1vx/2))*(self.vx+(k1vx/2)))*self.dt
            k2vy=(-9.81-np.sign(self.vy+(k1vy/2))*((self.rho*self.C*self.A)/(2*self.m))*((self.vy+(k1vy/2))*(self.vy+(k1vy/2))))*self.dt
            k2x=(self.vx+(k1vx/2))*self.dt 
            k2y=(self.vy+(k1vy/2))*self.dt

            k3vx=-np.sign(self.vx+(k2vx/2))*((self.rho*self.C*self.A)/(2*self.m))*((self.vx+(k2vx/2))*(self.vx+(k2vx/2)))*self.dt
            k3vy=(-9.81-np.sign(self.vy+(k2vy/2))*((self.rho*self.C*self.A)/(2*self.m))*((self.vy+(k2vy/2))*(self.vy+(k2vy/2))))*self.dt
            k3x=(self.vx+(k2vx/2))*self.dt
            k3y=(self.vy+(k2vy/2))*self.dt 

            k4vx=-np.sign(self.vx+(k3vx/2))*((self.rho*self.C*self.A)/(2*self.m))*((self.vx+(k3vx/2))*(self.vx+(k3vx/2)))*self.dt
            k4vy=(-9.81-np.sign(self.vy+(k3vy/2))*((self.rho*self.C*self.A)/(2*self.m))*((self.vy+(k3vy/2))*(self.vy+(k3vy/2))))*self.dt
            k4x=(self.vx+(k3vx/2))*self.dt
            k4y=(self.vy+(k3vy/2))*self.dt
            
            self.vx=self.vx+(k1vx+2*k2vx+2*k3vx+k4vx)/6
            self.vy=self.vy+(k1vy+2*k2vy+2*k3vy+k4vy)/6
            self.x=self.x+(k1x+2*k2x+2*k3x+k4x)/6
            self.listax.append(self.x)
            self.y=self.y+(k1y+2*k2y+2*k3y+k4y)/6
            self.listay.append(self.y)

        return self.listax,self.listay