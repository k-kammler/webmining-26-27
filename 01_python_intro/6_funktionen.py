# Eine Funktion mit einer Bedingung
def check_zahl(x):
    if x % 2 == 0:
        return "Gerade Zahl"
    else:
        return "Ungerade Zahl"

a = (check_zahl(10))  # Test mit einer geraden Zahl
b = (check_zahl(11))  # Test mit einer ungeraden Zahl

print(a)
print(b)


# Eine Funktion mit einer Schleife und Bedingung
def finde_gerade_zahlen(liste):
    gerade = []
    for zahl in liste:
        if zahl % 2 == 0:
            gerade.append(zahl)
    return gerade

gerade_zahlen = finde_gerade_zahlen([1, 2, 3, 4, 5, 6])
print(gerade_zahlen)