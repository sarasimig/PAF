def jednoliko_gibanje(F,m,t,dt=0.01):
    import matplotlib.pyplot as plt
    import numpy as np

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

def kosi_hitac(v0, kut1, t, dt=0.01):
    import numpy as np
    import matplotlib.pyplot as plt

    kut2 = np.radians(kut1)
    vx = v0 * np.cos(kut2)
    vy = v0 * np.sin(kut2)

    ax=0
    ay=-9.81

    x=0
    y=0

    x_lista=[]
    y_lista=[]
    t_lista=[]
    vx_lista=[]
    vy_lista=[]

    for t in np.arange(0, t, dt):
        t_lista.append(t)
        vx_lista.append(vx)
        vy_lista.append(vy)
        vx=vx+ax*dt
        vy=vy+ay*dt
        x=x+vx*dt
        x_lista.append(x)
        y=y+vy*dt
        y_lista.append(y)

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.plot(x_lista, y_lista)
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('x - y graf')

    plt.subplot(1, 3, 2)
    plt.plot(t_lista, x_lista)
    plt.xlabel('t (s)')
    plt.ylabel('x (m)')
    plt.title('x - t graf')

    plt.subplot(1, 3, 3)
    plt.plot(t_lista, y_lista)
    plt.xlabel('t (s)')
    plt.ylabel('y (m)')
    plt.title('y - t graf')

    plt.tight_layout()
    plt.show()

