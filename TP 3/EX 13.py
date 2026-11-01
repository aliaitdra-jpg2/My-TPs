ch = input("Saisir une chaîne de caractères : ")
R=""
for c in ch.lower():
    if c not in R:
        R+=c
    else:
        R=R    
print("la chaine sans les caractères répétés est :", R)