N=int(input("Saisir un entier N="))         
for i in range(2,N+1):
    if i%1==0 and i%i==0:  
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=",")