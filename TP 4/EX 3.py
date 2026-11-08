CH=input("saisir une chaine de caractere: ")
CH=CH.lower()
E=""
for i in CH:
    N=0
    if i in E:
        continue
    for j in CH:
        if i==j:
            N+=1 
    E+=i+str(N)
print(E)                    


    
    
