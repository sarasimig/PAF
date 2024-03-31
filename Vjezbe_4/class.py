class Particle:
    def __init__(self,mass,x_0,v):
        self.mass=mass
        self.x_0=x_0
        self.v=v

    def printinfo(self):
        print("masa čestice:", self.mass)
        print("položaj čestice:", self.x_0)
        print("brzina čestice:", self.v)

    def movetoorigin(self):
        self.x_0=0

    def speedup(self,dv):
        self.v+=dv

p1=Particle(10, -5, 5)
p1.printinfo()
p1.movetoorigin()
p1.speedup(3)
p1.printinfo()