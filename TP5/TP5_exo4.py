somme = int(input("Entrez une somme d'argent en euros : "))

reste = somme

b100 = reste // 100
reste %= 100

b50 = reste // 50
reste %= 50

b10 = reste // 10
reste %= 10

p2 = reste // 2
reste %= 2

p1 = reste

print(f"{somme} euros, c’est donc {b100} billets de 100, {b50} de 50, {b10} de 10, {p2} pièces de 2 et {p1} pièce 1.")
