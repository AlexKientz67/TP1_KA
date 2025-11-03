t = int(input("Entrer le nombre total de minutes écoulées depuis le début du mois : "))

jours = t // (24 * 60)
reste = t % (24 * 60)
heures = reste // 60
minutes = reste % 60

print("{} jour(s), {} heure(s) et {} minutes.".format(jours, heures, minutes))