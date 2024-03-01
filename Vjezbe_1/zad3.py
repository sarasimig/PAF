def unos_koordinata():
    while True:
        x=input("unesite x koordinatu:")
        y=input("unesite y kootdinatu:")

        if x.replace('.','',1).isdigit() and y.replace('.','',1).isdigit():
            xx=float(x)
            yy=float(y)
            return xx,yy
        else:
            print("Neispravan unos, unesite broj.")

print("unesite koordinate prve točke:")
tocka1=unos_koordinata()

print("unesite koordinate druge točke:")
tocka2=unos_koordinata()

x1,y1=tocka1
x2,y2=tocka2

if x1==x2:
    print("jednadžba pravca: x={}".format(x1))
else:
    a=(y2-y1)/(x2-x1)
    b=y1-a*x1
    print("jednadžba pravca: y={}x+{}".format(a,b))