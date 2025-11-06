moyenne = 0
nbrnote = 0

while True:
    entree = float(input("Entrez une moyenne ou -1 pour quitter : "))
    if entree == -1:
        break
    elif 0 <= entree <= 20:
        moyenne += entree
        nbrnote += 1
    else:
        print("Note invalide")

if moyenne > 0:
    print("La moyenne des notes est :", moyenne / nbrnote)
else:
    print("Aucune note saisie.")