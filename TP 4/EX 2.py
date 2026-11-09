N=int(input("Entrez un nombre entier N : "))
for i in range(1, N+1):
    print("Tableau de multiplication de :", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i*j, end=" | ")
    print("\n")