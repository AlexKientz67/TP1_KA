L = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]

max_valeur = L[0]
max_freq = L.count(L[0])

for x in L:
    if L.count(x) > max_freq:
        max_valeur = x
        max_freq = L.count(x)

print(f"Le nombre le plus frequent dans la liste est le : {max_valeur} ({max_freq} x)")