c_inf_10 = 0
c_10_15 = 0
c_sup_15 = 0

for i in range(10):
    val = float(input(f"Entrez une valeur comprise entre 0 et 20 : "))
    while val < 0 or val > 20:
        val = float(input("Erreur ! Entrez une valeur entre 0 et 20 : "))

    if val < 10:
        c_inf_10 += 1
    elif val < 15:
        c_10_15 += 1
    else:
        c_sup_15 += 1

print("Nombre < 10 :", c_inf_10)
print("10 ≤ valeur < 15 :", c_10_15)
print("valeur ≥ 15 :", c_sup_15)
