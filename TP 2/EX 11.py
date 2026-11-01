E=int(input("Saisir un entier compris entre 0 et 6 : "))
if 0 <= E <= 6:
    if E==0:
        print("ce jour est dimanche")
    elif E==1:
        print("ce jour est lundi")
    elif E==2:
        print("ce jour est mardi")
    elif E==3:
        print("ce jour est mercredi")
    elif E==4:
        print("ce jour est jeudi")
    elif E==5:
        print("ce jour est vendredi")
    elif E==6:
        print("ce jour est samedi")
else:
    print("ERREUR : Veuillez saisir un entier compris entre 0 et 6.")