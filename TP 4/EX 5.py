N=input("saisir un entier positif: ")
S=0
for i in N:
    S+=int(i)**3

if S==int(N):
    print(f"{N} est un nombre d'armstrong", end="\n\n")      
else:
    print(f"{N} n'est pas un nombre d'armstrong", end="\n\n") 

print(f"les nombres d'armstrong entre 1 et {N} sont :")
for i in range(1, int(N)):
    S=0
    for j in str(i):
        S+=int(j)**3
    if S==i:
        print(S, end="\t")