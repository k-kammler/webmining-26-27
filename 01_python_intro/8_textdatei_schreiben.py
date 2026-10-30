# Eine Textdatei im Schreibmodus öffnen und Text hineinschreiben

# Der with-Block stellt sicher, dass die Datei automatisch geschlossen wird, sobald der Block beendet ist – selbst wenn ein Fehler auftritt.

with open("beispiel.txt", "w") as datei:
    datei.write("Dies ist die erste Zeile.\n")
    datei.write("Dies ist die zweite Zeile.\n")


# # Eine Datei im Anhangmodus öffnen und neuen Text hinzufügen
with open("beispiel.txt", "a") as datei:
    datei.write("Dies ist eine weitere Zeile im Anhang.")