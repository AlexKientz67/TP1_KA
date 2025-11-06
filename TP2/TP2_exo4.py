
BASE = 4
fromage = 800.0
eau = 2.0
ail = 2.0
pain = 400.0

nbConvives = int(input("Entrez le nombre de personne pour la fondue : "))

fromage = fromage * nbConvives / BASE
eau = eau * nbConvives / BASE
ail = ail * nbConvives / BASE
pain = pain * nbConvives / BASE

# 9. Affichage du résultat
print("Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")
print("{} gr de fromage".format(fromage))
print("{} dl de eau".format(eau))
print("{} gr de pain".format(pain))
print("{} gousses d'ail".format(ail))