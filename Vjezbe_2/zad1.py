import matplotlib.pyplot as plt
import numpy as np

F=20
m=2
t=10
dt=0.01

a = float(F / m)

t_lista = []
x_lista = []
v_lista = []
a_lista = []

x=0
v=0

for t in np.arange(0, t, dt):
    t_lista.append(t)
    x_lista.append(x)
    v_lista.append(v)
    a = F / m
    x += v * dt
    v += a * dt
    a_lista.append(a)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(t_lista, x_lista)
plt.xlabel('vrijeme (s)')
plt.ylabel('položaj (m)')
plt.title('x-t graf')

plt.subplot(1, 3, 2)
plt.plot(t_lista, v_lista)
plt.xlabel('vrijeme (s)')
plt.ylabel('brzina (m/s)')
plt.title('v-t graf')

plt.subplot(1, 3, 3)
plt.plot(t_lista, a_lista)
plt.xlabel('vrijeme (s)')
plt.ylabel('ubrzanje (m/s^2)')
plt.title('a-t graf')

plt.tight_layout()
plt.show()
