moyenne_classe = 0
nb_eleves = 0

while True:
    entre = input("Appuyez sur entrée pour ajouter un élève ou tapez -1 pour quitter : ")
    if entre == "-1":
        break

    somme_notes = 0
    somme_coef = 0

    while True:
        note = float(input("Entrez une note ou -1 pour passer à l'élève suivant : "))
        if note == -1:
            break
        elif 0 <= note <= 20:
            coef = float(input("Entrez le coefficient de cette note : "))
            somme_notes += note * coef
            somme_coef += coef
        else:
            print("Note invalide, entrez une valeur entre 0 et 20.")

    if somme_coef > 0:
        moyenne_eleve = somme_notes / somme_coef
        print("Moyenne : {:.2f}".format(moyenne_eleve))
        moyenne_classe += moyenne_eleve
        nb_eleves += 1
    else:
        print("Aucune note saisie.")

if nb_eleves > 0:
    print("Moyenne classe : {:.2f}".format(moyenne_classe / nb_eleves))