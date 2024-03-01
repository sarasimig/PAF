import matplotlib.pyplot as plt

def unos_koordinata():
    x=float(input("unesite x koordinatu:"))
    y=float(input("unesite y kootdinatu:"))
    return x,y

print("unesite koordinate prve točke:")
tocka1=unos_koordinata()

print("unesite koordinate druge točke:")
tocka2=unos_koordinata()

def jed_pravca(tocka1,tocka2):

    x1=tocka1[0]
    y1=tocka1[1]
    x2=tocka2[0]
    y2=tocka2[1]

    if x1==x2:
        print("jednadžba pravca: x={}".format(x1))
    else:
        a=(y2-y1)/(x2-x1)
        b=y1-a*x1
        print("jednadžba pravca: y={}x+{}".format(a,b))

    plt.plot([tocka1[0],tocka2[0]], [tocka1[1],tocka2[1]])
    plt.scatter([tocka1[0],tocka2[0]], [tocka1[1],tocka2[1]], c="red")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graf unesenih točaka i pravac koji prolazi kroz njih')
    plt.grid(True)
    plt.show()
    plt.savefig("graf_zad4.pdf")

jed_pravca(tocka1,tocka2)
#ovo su zadatak 4 i 5 spojeni u jedan zadatak
