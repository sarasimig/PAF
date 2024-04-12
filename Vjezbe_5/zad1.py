import calculus as calc
import matplotlib.pyplot as plt
import math
import numpy as np

def f1(x):
    return 5*x**3-2*x**2+2*x-3

def f1_analiticka_der(x):
    return 5*3*x**2-4*x+2

def f2(x):
    return np.sin(x)

def f2_analiticka_der(x):
    return np.cos(x)


fig, axs = plt.subplots(2, 1, figsize=(10, 8))

#f1
x_donja = 0
x_gornja = 4

x = np.linspace(x_donja, x_gornja, 100)
dy_a = f1_analiticka_der(x)
axs[0].plot(x, dy_a, label='Analitička derivacija f1(x)', color='orange')

for h in [1, 0.5, 0.1, 0.05]:
    x1, y1 = calc.derivacije_funkcije_u_tockama(f1, x_gornja, x_donja, h)
    axs[0].plot(x1, y1, marker='o', markersize=2, linestyle='--', linewidth=1, label=f'Numerička derivacija f1(x), h={h}')

axs[0].legend()
axs[0].set_title('Grafovi funkcije f1 i njezinih derivacija')
axs[0].set_xlabel('x')
axs[0].set_ylabel('f1(x)')

# f2
x_donja = 0
x_gornja = 4

x = np.linspace(x_donja, x_gornja, 100)
dy_a = f2_analiticka_der(x)
axs[1].plot(x, dy_a, label='Analitička derivacija f2(x)', color='green')

for h in [1, 0.5, 0.1, 0.05]:
    x2, y2 = calc.derivacije_funkcije_u_tockama(f2, x_gornja, x_donja, h)
    axs[1].plot(x2, y2, marker='o', markersize=2, linestyle='--', linewidth=1, label=f'Numerička derivacija f2(x), h={h}')

axs[1].legend()
axs[1].set_xlabel('x')
axs[1].set_ylabel('f2(x)')

plt.tight_layout()
plt.show()