Ch=input("Saisir une chaine de caractéres=")
C=input("Saisir un caractére=")
N=0
for i in Ch:
    if i==C:
       N+=1
print(f"Le caractére {C} apparaît {N} fois dans la chaine {Ch}")