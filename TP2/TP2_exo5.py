inp = int(input("Entrer un nombre :"))

if inp < 0 and inp % 2 == 0:
    print("Nombre négatif et pair")
elif inp > 0 and inp % 2 == 0:
    print("Nombre positif et pair")
elif inp < 0 and inp % 2 != 0:
    print("Nombre négatif et impair")
elif inp > 0 and inp % 2 != 0:
    print("Nombre positif et impair")
elif inp == 0:
    print("Le nombre est zéro (et il est pair)")