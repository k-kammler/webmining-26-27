# Eine Textdatei im Lesemodus öffnen und den Inhalt lesen
with open("beispiel.txt", "r", encoding="utf-8") as datei:
    inhalt = datei.read()

lines = inhalt.split('\n')

print(lines)


# # Zeilenweise aus einer Textdatei lesen
# with open("beispiel.txt", "r", encoding="utf-8") as datei:
#     zeilen = datei.readlines()

# for zeile in zeilen:
#     print(zeile.strip())  # strip() entfernt Zeilenumbrüche


# # Datei öffnen und Fehler abfangen, falls die Datei nicht existiert
try:
    with open("nicht_existiert.txt", "r") as datei:
        print(datei.read())
except FileNotFoundError:
    print("Die Datei wurde nicht gefunden.")