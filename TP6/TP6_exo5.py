import unicodedata

def enlever_accents(txt):
    return ''.join(
        c for c in unicodedata.normalize('NFD', txt)
        if unicodedata.category(c) != 'Mn'
    )
def nettoyer(txt):
    txt = txt.lower()
    txt = enlever_accents(txt)
    propre = ""
    for c in txt:
        if c.isalnum():
            propre += c
    return propre
def est_palindrome(txt):
    txt = nettoyer(txt)
    return txt == txt[::-1]
phrase = input("Entrez un mot ou une phrase : ")

if est_palindrome(phrase):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
