date = input("Donnez une date sous la forme jjmmaaaa : ")

if len(date) != 8 or not date.isdigit():
    print("Format incorrect !")
else:
    j = int(date[0:2])
    m = int(date[2:4])
    a = int(date[4:8])

    # Vérification du mois
    if m < 1 or m > 12:
        print("Date incorrecte : mois invalide.")
    else:
        # Jours max selon mois
        if m in [1, 3, 5, 7, 8, 10, 12]:
            maxj = 31
        elif m in [4, 6, 9, 11]:
            maxj = 30
        else:  # Février
            # Année bissextile ?
            if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
                maxj = 29
            else:
                maxj = 28

        if j < 1 or j > maxj:
            print("Date incorrecte : jour invalide.")
        else:
            print("Date correcte !")