print("saisir les coefficients de l'équation du second degré : ax² + bx + c = 0")
a = float(input("Saisir le coefficient a = "))
b = float(input("Saisir le coefficient b = "))
c = float(input("Saisir le coefficient c = "))
if a == 0:
    if b == 0 and c == 0:
        print("L'équation a une infinité de solutions.")
    elif b == 0 and c != 0:
        print("L'équation n'a pas de solution.")
    else:
        x = -c / b
        print("L'équation a une solution : x =", x)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("L'équation n'a pas de solution réelle.")
    elif delta == 0:
        x = -b / (2*a)
        print("L'équation a une solution double : x =", x)
    else:
        X1 = (-b + delta**0.5) / (2*a)
        X2 = (-b - delta**0.5) / (2*a)
        print("L'équation a deux solutions réelles : x1 =", X1, "et x2 =", X2)