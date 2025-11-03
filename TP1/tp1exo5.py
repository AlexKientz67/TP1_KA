jour = int(input("Entrer le nombre de jour :"))
heure = int(input("Entrer le nombre de heure :"))
minute = int(input("Entrer le nombre de minute :"))
t=0
t=int(t)
t = ((jour * 24) * 60) + (heure * 60) + minute
print("Depuis le début du mois, {} minutes se sont écoulés.".format(t))


