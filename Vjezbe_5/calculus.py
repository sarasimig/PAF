import numpy as np

#prva metoda(funkcija), zad1
def derivacija_funkcije_T(funkcija,x,h,metoda=3): 
    if metoda==3:
        d=((funkcija(x+h)-funkcija(x-h))/(2*h))
        return d
    elif metoda==2:
        d=((funkcija(x+h)-funkcija(x))/(h))
        return d

#druga metoda(funkcija), zad1
def derivacije_funkcije_u_tockama(funkcija,gornja_granica,donja_granica,h,metoda=3): 
    tocke=np.arange(donja_granica,gornja_granica,h)
    tocke = np.arange(donja_granica, gornja_granica, h)
    rezultat = derivacija_funkcije_T(funkcija, tocke, h, metoda)
    return tocke, rezultat

#treca metoda(funkcija), zad2
def integral_pravokutna_aproksimacija2(funkcija, gornja_granica, donja_granica, n):
    x = np.linspace(donja_granica, gornja_granica, n+1)
    y = funkcija(x)
    dx = (gornja_granica - donja_granica) / n
    print(dx)
    f_u = sum( y[1:] * dx )
    f_l = sum( y[:-1] * dx )
    return f_u, f_l

#cetvrta metoda(funkcija), zad2
def integral_trapezna_formula(funkcija,gornja_granica,donja_granica,N):
    listax=np.linspace(donja_granica,gornja_granica,N+1)
    dx=(gornja_granica-donja_granica)/N
    integral=0
    for i in range(N+1):
        if i<N:
            integral+=dx*(funkcija(listax[i])+funkcija(listax[i+1]))/2
    return integral, listax