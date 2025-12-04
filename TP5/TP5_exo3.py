chaine = input("Entrez un mot ou une phrase : ")

chaine = chaine.lower()

epuree = ""
for c in chaine:
    if c.isalpha():
        epuree += c

if epuree == epuree[::-1]:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
