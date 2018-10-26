import random
import math

times = [ "Vasco", "Flamengo", "Botafogo", "Fluminense",
          "Sao Paulo", "Corinthians", "Palmeiras", "Santos", "Ponte Preta",
          "Coritiba", "Atletico PR", "Atletico MG", "Cruzeiro", "Gremio",
          "Vitoria", "Bahia", "Sport", "Avai", "Chapecoense", "Atletico GO" ]

times2 = [ "1", "2", "3", "4", "6", "7", "8", "9", "10",
         "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]

short6 = [ "Vasco", "Flamengo", "Corinthians", "Palmeiras", "Atletico MG", "Cruzeiro" ]

def berger( lista ):
    tabela = {}
    for rodada in range(len(lista)-1):
        tabela[rodada+1] = []                   
    print(tabela)

    n = len(lista)
    i = 1

    while i < n:
        j = i+1
        while j <= n:
            if j != n and i != n:
                if i+j-1 < n:
                    r = i+j-1
                else:
                    r = i+j-n
                if (i+j)%2 == 0:
                    casa = i
                    fora = j
                else:
                    fora = i
                    casa = j
            if j == len(lista):
                if 2*i <= n:
                    r = 2*i-1
                    casa = i
                    fora = j
                else:
                    r = 2*i-n
                    casa = j
                    fora = i
            
            #print ("i: ",i,"\tj: ",j,"\tr", r)
            tabela[r].append((lista[casa-1], lista[fora-1]))
            j = j+1
        i = i+1
    print(tabela)
    return tabela
                


berger(short6)
        
        
tab = berger(times2)
for i in tab:
    for a in tab[i]:
        print(a)
        



'''Cas où i≠n et j≠n
r=i+j-1 si i+j-1 < n 
ou 
r=i+j-n si i+j-1 ≥ n 

Choix des couleurs 
Si i+j est impair, i aura les blancs si i<j
Si i+j est pair, i aura les blancs si i>j

Cas où j=n 
r = 2×i-1 si 2i ≤ n et j a les Noirs
r = 2×i-n si 2i > n et j a les Blancs'''


    
