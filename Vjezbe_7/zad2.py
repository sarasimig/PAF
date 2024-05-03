import matplotlib.pyplot as plt
import Projectile as pro

p1=pro.Projectile(45,20,1,0.01,0.3)
x1,y1=p1.Euler()
p2=pro.Projectile(45,20,1,0.01,0.3)
x2,y2=p2.Rungekutta()

plt.plot(x1,y1,label ='dt=0.01 Euler')
plt.plot(x2,y2,label ='dt=0.01 Runge-Kutta')
plt.title("x-y graf")
plt.xlabel("x[m]")
plt.ylabel("y[m]")
plt.legend()
plt.show()