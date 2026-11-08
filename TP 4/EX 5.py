N=input("saisir un entier positif: ")
S=0
for i in N:
    S+=int(i)**3

if S==int(N):
    print(f"{N} est un nombre d'armstrong")
else:
    print(f"{N} n'est pas un nombre d'armstrong")    