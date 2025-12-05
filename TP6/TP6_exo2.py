def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst

# a
lst1 = [0, 1, 2]

# b
lst2 = ajouter_elt(lst1, len(lst1))

# c
print("lst1 :", lst1, "type :", type(lst1))
print("lst2 :", lst2, "type :", type(lst2))
