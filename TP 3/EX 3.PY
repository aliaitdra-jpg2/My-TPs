N=int(input("Saisir un entier N="))
N = abs(N)
S=0
if N == 0:
    S += 1
else:
    while N > 0:
      S += 1
      N = N // 10
print("le nombre des chiffres est",S)