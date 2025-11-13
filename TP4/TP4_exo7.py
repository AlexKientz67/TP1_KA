binome = ("login1", "login2")
print(f"L’étudiant {binome[0]} est en binome avec l’étudiant {binome[1]}")
try:
    binome[1] = input("Nouveau login : ")
except:
    print("Impossible ! Un tuplet est immuable.")

try:
    del binome[1]
except:
    print("Impossible ! On ne peut pas supprimer un élément d’un tuplet.")

binome = (binome[0], binome[1], input("Ajoutez un troisième login : "))
print("Nouveau trinôme :", binome)