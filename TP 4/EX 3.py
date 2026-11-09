CH=input("saisir une chaine de caractere: ")
E=""
i=0

while i<len(CH):
    N=0
    for j in CH[i::]:
        if CH[i]!=j:
            break
        else:
            N+=1
    E+=CH[i]+str(N)
    i=(i+N)
        
print(E)   




    
    
