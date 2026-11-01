E=int(input("Saisir un entier positif E="))
S=0
for i in str(E):
    F=1
    for j in range(1,int(i)+1):
        F*=j
    S+=F
print("La somme des factoriels des chiffres de l'entier E est=",S)
if S==E:
    print("ce nombre est fort")
else:
    print("ce nombre n'est pas fort")