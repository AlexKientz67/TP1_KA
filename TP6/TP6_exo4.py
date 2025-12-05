import random

def generer(nbr, vmin, vmax):
    tab = []
    for i in range(nbr):
        tab.append(random.randint(vmin, vmax))
    return tab

def combienInferieur(table, vseuil):
    cpt = 0
    for v in table:
        if v < vseuil:
            cpt += 1
    return cpt

nbr = int(input("Nombre de valeurs à générer ? "))
vmin = int(input("Valeur minimale ? "))
vmax = int(input("Valeur maximale ? "))

tab = generer(nbr, vmin, vmax)
tab.sort()

rep = input("Vous voulez préciser le seuil ? (O/N) : ").lower()
if rep == "o" or rep == "oui":
    seuil = int(input("Entrez le seuil : "))
else:
    seuil = 30

total = combienInferieur(tab, seuil)
print(f"Il y en a {total} inférieurs à {seuil}")
