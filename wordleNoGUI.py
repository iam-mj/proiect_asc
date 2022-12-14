"""
        wordleNoGUI alege un cuvant random si primeste de la terminal
    incercarile jucatorului, afisand, pana la ghicirea cuvantului, un 
    feedback construit la fel ca cel furnizat de functia feed din fisierul
    "feedback.py":
        0 = litera de pe pozitia respectiva este intoarsa cu un fundal 
            alb / gri
        1 = litera de pe pozitia respectiva este intoarsa cu un fundal
            galben
        2 = litera de pe pozitia respectiva este intoarsa cu un fundal 
            verde
"""
import random

f = open("cuvinte.txt", "r")
L = []
N = 11454 #numarul de cuvinte din baza de date

#adaugam cuvintele intr-o lista
for x in f:
    L.append(x.strip(" \n"))#eliminam ENTER-ul de la finalul sirurilor de caractere
f.close()

#alegem un cuvant random
n = random.randint(0, N - 1)
cuv = L[n]

D = {k:cuv.count(k) for k in cuv}

user_sol = "00000"
ok = 0

while user_sol != "22222":
    
    D1 = {}
    D1 = D.copy()
    
    if ok == 0:
        sol = input("Dati prima incercare: ")
        ok = 1
    else:
        sol = input("Dati urmatoarea incercare: ")

    D2 = {k : sol.count(k) for k in sol}

    if sol in L and len(sol) == 5: 

        for i in range(5):
            if sol[i] == cuv[i]:
                user_sol = user_sol[:i] + "2" + user_sol[i + 1:]
                D1[sol[i]] -= 1
                D2[sol[i]] -= 1
            elif sol[i] not in cuv:
                user_sol = user_sol[:i] + "0" + user_sol[i + 1:]
            else:
                user_sol = user_sol[:i] + "-" + user_sol[i + 1:]
        
        for i in range(5):
            if user_sol[i] == "-" and D1[sol[i]] != 0:
                user_sol = user_sol[:i] + "1" + user_sol[i + 1:]
                D1[sol[i]] -= 1
            elif user_sol[i] == "-":
                user_sol = user_sol[:i] + "0" + user_sol[i + 1:]
    
        #dam feedback guesser-ului
        print(user_sol)

    else:
        print("ERROR!")

