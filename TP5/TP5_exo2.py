notes = []
coeffs = []

for i in range(1, 6):
    entree = input(f"Veuillez entrer la note du module {i} et le coefficient correspondant : ")
    n, c = entree.split(" ")
    notes.append(float(n))
    coeffs.append(int(c))

somme = 0
somme_coeff = 0

for i in range(5):
    somme += notes[i] * coeffs[i]
    somme_coeff += coeffs[i]

moyenne = somme / somme_coeff

admis = moyenne >= 10 and all(note >= 8 for note in notes)

print(f"Moyenne générale : {moyenne:.2f}")
if admis:
    print("L'étudiant est admis.")
else:
    print("L'étudiant n'est pas admis.")
