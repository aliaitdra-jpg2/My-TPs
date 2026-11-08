N=int(input("Entrez un nombre entier N : "))
S=0
for i in range(1, N//2+1):
   if N%i==0:
      S+=i

if S==N :
    print(N,"est un nombre parfait")
else:
    print(N,"n'est pas un nombre parfait")   

print("les nombres parfaits entre 1 et" ,N," sont :" )
print(1, end=" ; ")
for j in range(2, N):
    NP=0
    for k in range(1, j//2+1):
        if j%k==0:
            NP+=k
    if NP==j:
        print(j, end=" ; ")       
            
