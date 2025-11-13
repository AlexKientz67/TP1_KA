nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
notes = []
moyenne = 0.0

for i in range(nombreEtudiants):
    note = float(input(f"Note etudiant {i} : "))

    while note < 0 or note > 20:
        note = float(input(f"Note invalide ! Re-saisir la note de l'etudiant {i} : "))

    notes.append(note)
    moyenne += note

moyenne = moyenne / nombreEtudiants

print(f"\nMoyenne de classe : {moyenne}\n")
print("Numéro de l’Etudiant | note | ecart a la moyenne")

for i in range(nombreEtudiants):
    print(f"{i} | {notes[i]} | {round(notes[i] - moyenne, 2)}")