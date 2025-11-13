debut = int(input("Donnez l’heure de début : "))
fin = int(input("Donnez l’heure de fin : "))

# --- Vérification des erreurs ---
if debut < 0 or debut > 24 or fin < 0 or fin > 24:
    print("Les heures doivent être entre 0 et 24")

elif debut == fin:
    print("l’heure de fin est identique à l’heure de début.")

elif debut > fin:
    print("le début de la location est après la fin ...")

else:
    total = 0
    heures_tarif_1 = 0
    heures_tarif_2 = 0

    for h in range(debut, fin):
        if 0 <= h < 7 or 17 <= h < 24:
            heures_tarif_1 += 1
        else:
            heures_tarif_2 += 1

    total = heures_tarif_1 * 1 + heures_tarif_2 * 2

    print("Vous avez loué le vélo pendant")
    if heures_tarif_1 > 0:
        print(f"{heures_tarif_1} heure(s) au tarif horaire de 1.0 euro(s)")
    if heures_tarif_2 > 0:
        print(f"{heures_tarif_2} heure(s) au tarif horaire de 2.0 euro(s)")

    print(f"Le montant total à payer est de {float(total)} euro(s).")
