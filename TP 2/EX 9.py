C = input("Entrez un caractère : ")

if len(C) == 1 and C.isalpha() and C.isupper():
    print("La lettre est majuscule")
elif len(C) == 1 and C.isalpha() and C.islower():
    print("La lettre minuscule")
else:
    print("C'est un autre caractère")
