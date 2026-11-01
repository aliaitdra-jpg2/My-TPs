N1=input("Saisir le premier nom : ")
N2=input("Saisir le deuxième nom : ")
N3=input("Saisir le troisième nom : ")
A1=int(input("Saisir l'age du premier nom : "))
A2=int(input("Saisir l'age du deuxième nom : "))
A3=int(input("Saisir l'age du troisième nom : "))
if A1>A2 and A1>A3:
    print("Le nom le plus âgé est : ",N1)
elif A2>A1 and A2>A3:
    print("Le nom le plus âgé est : ",N2)
else:
    print("Le nom le plus âgé est : ",N3)      