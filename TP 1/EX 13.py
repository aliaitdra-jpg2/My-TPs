Q=float(input("saisir la quantité achetée : "))
P=float(input("saisir le prix unitaire : "))
PT=Q*P
MR=PT*0.15
PF=PT-MR
print("le prix total avant la réduction est =",PT)
print("le montant de la réduction est =",MR)
print("le prix final après la réduction est =",PF)