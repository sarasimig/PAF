import matplotlib.pyplot as plt
import seminar as s

# Ovisnost o Cd
projektil1=s.Projectile(45,20,1,0.1,0.03)
x1,y1=projektil1.Rungekutta()
projektil2=s.Projectile(45,20,1,0.1,0.47)
x2,y2=projektil2.Rungekutta()
projektil3=s.Projectile(45,20,1,0.1,0.8)
x3,y3=projektil3.Rungekutta()
projektil4=s.Projectile(45,20,1,0.1,1.05)
x4,y4=projektil4.Rungekutta()

domet1=x1[-1]
domet2=x2[-1]
domet3=x3[-1]
domet4=x4[-1]

fig,axs=plt.subplots(2,2,figsize=(10,10))

axs[0,0].plot(x1,y1,c='pink',label=f'Domet: {domet1:.2f} m')
axs[0,0].set_title('Cd=0.03 (Strelica)')
axs[0,0].set_xlabel('x[m]')
axs[0,0].set_ylabel('y[m]')
axs[0,0].legend()

axs[0,1].plot(x2,y2,c='blue',label=f'Domet: {domet2:.2f} m')
axs[0,1].set_title('Cd=0.47 (Sfera)')
axs[0,1].set_xlabel('x[m]')
axs[0,1].set_ylabel('y[m]')
axs[0,1].legend()

axs[1, 0].plot(x3, y3, c='green', label=f'Domet: {domet3:.2f} m')
axs[1, 0].set_title('Cd=0.8 (Padobran)')
axs[1, 0].set_xlabel('x [m]')
axs[1, 0].set_ylabel('y [m]')
axs[1, 0].legend()

axs[1, 1].plot(x4, y4, c='orange', label=f'Domet: {domet4:.2f} m')
axs[1, 1].set_title('Cd=1.05 (Cilindar)')
axs[1, 1].set_xlabel('x [m]')
axs[1, 1].set_ylabel('y [m]')
axs[1, 1].legend()

plt.tight_layout()
plt.show()