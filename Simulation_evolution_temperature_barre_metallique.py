import numpy as np
import scipy.integrate as sp
import matplotlib.pyplot as plt



try:
    t_init= float(input("Quelle sera la température initiale de ta barre métallique (en degrés C°) ?  "))
except ValueError:
    print("Erreur : la température doit être un nombre (ex: 8.314)")
 
while True:
    try:
        repos_s =int(input("Combien de temps souhaites-tu laisser reposer le métal (en s) ?  "))
        if repos_s < 0:
            raise ValueError
        break
    except ValueError:
        print("Erreur : le temps doit être entier et positif (ex: 1.618")
        exit()
    
    
try:
    t_ambiant=float(input("Quelle sera la température ambiante où le métal se reposera (en C°) ?  "))
except ValueError:
    print("Erreur : la température ambiante doit être un nombre ! (ex: -273.15)")
        
    
    
n_points = 100
T = np.full(n_points, t_init) # La barre commence avec une température uniforme
T[0] = T[-1] = t_ambiant

alpha=0.1

def dT_dt(T,t):
    dT= np.zeros_like(T)
    for i in range(1,len(T)-1):
        dT[i]=alpha *(T[i+1]-2*T[i]+T[i-1])
    return dT

t_inter= np.linspace(0,repos_s,100)

sol= sp.odeint(dT_dt, T, t_inter) 


plt.figure(figsize=(8,8))
plt.title("Evolution de la température dans la barre métallique")
plt.grid()

for i in range(len(t_inter)):
    plt.plot(np.linspace(0,1,n_points),sol[i],"-",color="r")

plt.xlabel("Position le long de la barre métallique (échelle normalisée)")
plt.ylabel("Température $C°$")
plt.show()
