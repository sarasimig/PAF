import matplotlib.pyplot as plt
import Projectile as pro

p1=pro.Projectile(45,20,1,0.1,0.3)
x1,y1=p1.Euler()
p2=pro.Projectile(45,20,1,0.01,0.3)
x2,y2=p2.Euler()
p3=pro.Projectile(45,20,1,0.001,0.3)
x3,y3=p3.Euler()

plt.plot(x1,y1,label='dt=0.1')
plt.plot(x2,y2,label='dt=0.01')
plt.plot(x3,y3,label='dt=0.001')
plt.title("x-y graf")
plt.xlabel("x[m]")
plt.ylabel("y[m]")
plt.legend()
plt.show()