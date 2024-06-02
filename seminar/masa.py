import matplotlib.pyplot as plt
import seminar as s

#ovisnost o masi 
projektil1=s.Projectile(45,20,0.5,0.1,0.3)
x1,y1=projektil1.Rungekutta()
projektil2=s.Projectile(45,20,5,0.1,0.3)
x2,y2=projektil2.Rungekutta()
projektil3=s.Projectile(45,20,10,0.1,0.3)
x3,y3=projektil3.Rungekutta()
projektil4=s.Projectile(45,20,500,0.1,0.3)
x4,y4=projektil3.Rungekutta()

plt.plot(x1,y1,c='pink',label ='m=0.5')
plt.plot(x2,y2,c='blue',label='m=5')
plt.plot(x3,y3,c='green',label ='m=50',lw=10)
plt.plot(x4,y4,c='orange',label ='m=500')
plt.xlabel("x[m]")
plt.ylabel("y[m]")
plt.legend()
plt.show()