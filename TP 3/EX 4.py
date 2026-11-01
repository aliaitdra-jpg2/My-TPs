N=int(input("Saisir un entier positif N="))
S=0
for i in range(1,N//2+1):
   if N%i==0:
     S+=i

if S==N:
  print("Le nombre est parfait")   
else:
  print("Le nombre n'est pas parfait")