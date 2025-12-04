
heures = float(input("Heures travaillées : "))
taux = float(input("Salaire horaire : "))

salaire = 0

if heures <= 160:
    salaire = heures * taux
elif heures <= 200:
    salaire = 160 * taux + (heures - 160) * taux * 1.25
else:
    salaire = 160 * taux + 40 * taux * 1.25 + (heures - 200) * taux * 1.5

print(f"Salaire total : {salaire:.2f} euros")
