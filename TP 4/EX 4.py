chaine = input("Saisir la chaîne principale : ")
motif = input("Saisir le motif à rechercher : ")
chaine = chaine.lower()
motif = motif.lower()
MT = 0
while len(motif) < len(chaine):
    if motif ==" ":
        print("Le motif ne peut pas être vide.")
        chaine = input("Saisir une chaîne principale : ")
        motif = input("Saisir le motif à rechercher : ")
        continue
    else:
        for i in range(len(chaine)-len(motif)+1):
            if chaine[i:i + len(motif)] == motif:
               print(f"Motif trouvé à la position : {i+1} , {i + len(motif)}")
               MT+=1              
        if MT == 0:
                  print("\"Motif non trouvé.\"")
               
    print("Recherche terminée.")
    break

 