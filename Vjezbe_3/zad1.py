#zad 1 a)
a=5.0-4.935
print(a)
#očekivala sam rezultat 0.065, ali dobila sam 0.06500000000000039
#to se dogodilo zato što python samo razlomke oblika (1/2)**n može zapisati u konačnoj binarnoj formi, sve ostalo su aproksimacije
#brojevi kao što je naš rezultat se obično predstavljaju koristeći binarnu notaciju, koja može dovesti do malih grešaka u preciznosti 

#zad 1 b)
b=0.1+0.2+0.3
print(b)
#iz istog razloga očekivali bi broj 0.6 ali dobijemo 0.6000000000000001
#u aproksimaciji sa 64 bita ovi brojevi 0.6 i 0.6000000000000001 imaju identičan zapis u memoriji u binarnoj formi
#brojevi 0.1, 0.2 i 0.3 nemaju preciznan binaran zapis što može dovesti do malih pogrešaka u aritmetičkim operacijama 
#u našem slučaju nakuplanjem pogreškica dobiju se mala odstupanja od očekivanog rezultata
