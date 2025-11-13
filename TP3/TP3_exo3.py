import random

x = random.randint(0, 100)
tentatives = 0
val = -1

while val != x:
    val = int(input("Devinez le nombre (0-100) : "))
    tentatives += 1

    if val < x:
        print("Trop petit")
    elif val > x:
        print("Trop grand")

print("Le nombre était", x)
print("Nombre de tentatives :", tentatives)
