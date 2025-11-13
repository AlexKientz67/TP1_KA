X = int(input("Entrez X (>1) : "))

somme = 0
N = 0

while somme + N <= X:
    somme += N
    N += 1

print("Le plus grand N est :", N - 1)
