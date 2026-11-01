Ch=input("Saisir une chaine de caractéres=")
A=""
E=""
for i in Ch[::-1]:
    A+=i.upper()
if  A==Ch.upper():
    print(" La chaine est un palindrome")
else:
    print(" La chaine n'est pas un palindrome")
