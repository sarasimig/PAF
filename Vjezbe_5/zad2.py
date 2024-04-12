import calculus as calc
import matplotlib.pyplot as plt
import math
import numpy as np

def f1(x):
    return 5*x**3-2*x**2+2*x-3


fig, axs = plt.subplots(2, 1, figsize=(10, 8))


x_donja = 0
x_gornja = 10

for n in range(10,1000,10):
    x1, y1 = calc.integral_pravokutna_aproksimacija2(f1, x_gornja, x_donja, n)
    axs[0].plot(n, y1, marker='o', markersize=2, linestyle='--', linewidth=1)
    axs[0].plot(n, x1, marker='o', markersize=2, linestyle='--', linewidth=1)

axs[0].legend()
axs[0].set_xlabel('broj koraka')
axs[0].set_ylabel('integral f1(x)')


x_donja = 0
x_gornja = 10

for n in range(10,1000,10):
    y2, x2 = calc.integral_trapezna_formula(f1, x_gornja, x_donja, n)
    axs[1].plot(n, y2, marker='o', markersize=2, linestyle='--', linewidth=1)

axs[1].legend()
axs[1].set_xlabel('broj koraka')
axs[1].set_ylabel('integral f1(x)')

plt.tight_layout()
plt.show()