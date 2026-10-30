# Erstellen einer Liste und Zugreifen auf Elemente

zahlen = [1, 2, 3, 4, 5]
# print(zahlen[0])  # Erstes Element
# print(zahlen[-1])  # Letztes Element
# print(zahlen[4]) 


# # Listenlänge mit len() bestimmen
laenge = len(zahlen)
print(f"Die Länge der Liste ist: {laenge}")


# # Ein Element zu einer Liste hinzufügen mit append()
zahlen.append(6)
print(zahlen)


# # Mehrere Elemente zu einer Liste hinzufügen mit extend()
zahlen.extend([7, 8, 9])
print(zahlen)


# # Ein bestimmtes Element mit remove() löschen
zahlen.remove(5)
print(zahlen)


zahlen = [8, 3, 5, 2, 5, 1]
print(zahlen)

# # Eine Liste sortieren mit sort()
zahlen.sort()
print(f"Sortierte Liste: {zahlen}")


# # Liste umdrehen (reverse order) mit reverse()
zahlen.reverse()
print(f"Umgekehrte Liste: {zahlen}")


# # Andere Werte als Zahlen in Listen:
fruechte = ["Apfel", "Banane", "Kirsche"]
fruechte.append("Orange")  # Element hinzufügen
for frucht in fruechte:
    print(frucht)
