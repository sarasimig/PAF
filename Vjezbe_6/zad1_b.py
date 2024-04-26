import numpy as np
import matplotlib.pyplot as plt
import harmonic_oscillator as hs

h1=hs.HarmonicOscillator(1,7,4,10,0.01)
a1, v1, x1, t1 = h1.eulerova_metoda(10)
plt.scatter(t1,x1,color="blue")

h2=hs.HarmonicOscillator(1,7,4,10,0.02)
a2, v2, x2, t2 = h2.eulerova_metoda(10)
plt.scatter(t2,x2,color="orange")

h3=hs.HarmonicOscillator(1,7,4,10,0.05)
a3, v3, x3, t3= h3.eulerova_metoda(10)
plt.scatter(t3,x3,color="green")

plt.title("x-t")
plt.xlabel('t[s]')
plt.ylabel('x[m]')
plt.show()