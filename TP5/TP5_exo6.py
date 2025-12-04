T = input("Entrez une chaîne de caractères : ")

# 1. Taille
taille = 0
for _ in T:
    taille += 1

print("Taille de la chaîne :", taille)

# 2. Pourcentage de voyelles
voyelles = "aeiouyAEIOUY"
nb_voyelles = 0

for c in T:
    if c in voyelles:
        nb_voyelles += 1

pourcentage = (nb_voyelles / taille) * 100
print(f"Pourcentage de voyelles : {pourcentage:.2f} %")

# 3. Test sous-chaîne "wagon"
mot = "wagon"
len_mot = 5

def commence_a(T, pos, mot):
    for i in range(len_mot):
        if pos + i >= taille or T[pos + i].lower() != mot[i]:
            return False
    return True

premiere_occ = -1

for i in range(taille):
    if commence_a(T, i, mot):
        premiere_occ = i
        break

if premiere_occ != -1:
    print("La chaîne 'wagon' commence à l'indice :", premiere_occ)
else:
    print("La chaîne 'wagon' n'apparaît pas.")

# 4. Nombre d'occurrences
nb_occ = 0

for i in range(taille):
    if commence_a(T, i, mot):
        nb_occ += 1

print("Nombre d'occurrences de 'wagon' :", nb_occ)
