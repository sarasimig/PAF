import matplotlib.pyplot as plt
import seminar as s

#ovisnost o Cd 
projektil1=s.Projectile(45,20,1,0.1,0.03)
x1,y1=projektil1.Rungekutta()
projektil2=s.Projectile(45,20,1,0.1,0.47)
x2,y2=projektil2.Rungekutta()
projektil3=s.Projectile(45,20,1,0.1,0.8)
x3,y3=projektil3.Rungekutta()
projektil4=s.Projectile(45,20,1,0.1,1.05)
x4,y4=projektil4.Rungekutta()

plt.plot(x1,y1,c='pink',label ='Cd=0.47')
plt.plot(x2,y2,c='blue',label='Cd=1.05')
plt.plot(x3,y3,c='green',label ='Cd=0.03')
plt.plot(x4,y4,c='orange',label ='Cd=0.8')
plt.xlabel("x[m]")
plt.ylabel("y[m]")
plt.legend()
plt.show()