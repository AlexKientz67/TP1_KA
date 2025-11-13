dic = {
    "firstname": input("Votre prénom : "),
    "name": input("Votre nom : "),
    "promo": input("Votre promo : "),
    "group": input("Votre groupe : ")
}

print(f"Votre nom est '{dic['name']}', prénom est '{dic['firstname']}', "
      f"vous faites partie de la promo '{dic['promo']}' et votre groupe est '{dic['group']}'")

print("\nLes clés du dictionnaire sont :")
for k in dic.keys():
    print("-", k)

print("\nLes valeurs du dictionnaire sont :")
for v in dic.values():
    print("-", v)

print("\nLes tuplets du dictionnaire sont :")
for item in dic.items():
    print("-", item)

# Binôme
autre = {
    "firstname": "tata",
    "name": "tutu",
    "promo": "2022",
    "group": "102"
}

binome = {
    "id1": dic,
    "id2": autre
}

print("\nLes étudiants formants le binôme sont :")
for etu in binome.values():
    print(f"- L'étudiant {etu['name']} {etu['firstname']} du groupe {etu['group']}")