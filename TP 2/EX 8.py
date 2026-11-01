x = int(input("Entrez le 1er entier : "))
y = int(input("Entrez le 2e entier : "))
if y > x:
    x = y

y = int(input("Entrez le 3e entier : "))
if y > x:
    x = y

y = int(input("Entrez le 4e entier : "))
if y > x:
    x = y


print(" Le plus grand entier est :", x)