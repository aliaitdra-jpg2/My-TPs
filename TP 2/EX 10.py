L = input("Saisir une lettre : ")
if len(L) == 1 and L.isalpha() and L.lower() in "aàeéèiouy":
    print("La lettre est une voyelle.")
else:
    print("La lettre est une consonne.") 