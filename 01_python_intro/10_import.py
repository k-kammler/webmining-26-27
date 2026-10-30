import numpy as np
import os

# daten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# mittelwert = np.mean(daten)
# print(f"Mittelwert: {mittelwert}")

# median = np.median(daten)
# print(f"Median: {median}")

# summe = np.sum(daten)
# print(f"Summe: {summe}")


if os.path.exists("beispiel.txt"):
    print("Die Datei existiert.")
else:
    print("Die Datei existiert nicht.")