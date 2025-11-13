n = int(input("Entrez un entier : "))
choix = input("Choisir la boucle (for / while) : ")

fact = 1

if choix == "for":
    for i in range(1, n + 1):
        fact *= i
        print("Étape", i, "→", fact)

elif choix == "while":
    i = 1
    while i <= n:
        fact *= i
        print("Étape", i, "→", fact)
        i += 1

print("La factorielle de", n, "vaut", fact)
