nom1 = input("Nom de la première personne : ")
prenom1 = input("Prénom de la première personne : ")

nom2 = input("Nom de la deuxième personne : ")
prenom2 = input("Prénom de la deuxième personne : ")

p1_nom = nom1.upper()
p1_prenom = prenom1.capitalize()

p2_nom = nom2.upper()
p2_prenom = prenom2.capitalize()

personnes = [
    (p1_nom, p1_prenom),
    (p2_nom, p2_prenom)
]

personnes.sort()

for nom, prenom in personnes:
    print(prenom, nom)
