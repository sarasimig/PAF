def iteracija(N):
    broj=5
    
    for i in range(N):
        broj+=1/3
        
    for j in range(N):
        broj-=1/3

    print(broj)

iteracija(200)
iteracija(2000)
iteracija(20000)

#očekivano je kada dodamo i oduzmemo 1/3 broju 5 N puta da trebamo dobiti 5 jer se 1/3 ponište N puta
#zbog objašnjenja iz prvog zadatka rezultat može pokazivati male odstupanja od 5
#možemo primjetiti da se s povećanjem N rezultat približava petici pa prijeđe broj 5 za ta vrlo malena odstupanja