L = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]

max_valeur = L[0]
max_freq = 0

for x in L:
    freq = 0
    for y in L:
        if x == y:
            freq += 1

    if freq > max_freq:
        max_freq = freq
        max_valeur = x

print(f"Le nombre le plus frequent dans la liste est le : {max_valeur} ({max_freq} x)")