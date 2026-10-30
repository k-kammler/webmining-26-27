# Dictionary erstellen und auf Werte zugreifen
student = {"name": "Anna", 
           "alter": 22, 
           "kurs": "Mathematik"}
print(student["name"])  # Zugriff auf den Wert des Schlüssels 'name'


# # Ein Element hinzufügen oder ändern
student["adresse"] = "Berlin"
print(student)


# # Über die Schlüssel eines Dictionaries iterieren
# for key in student:
#     print(f"Schlüssel: {key}")


# # Über Werte eines Dictionaries iterieren
# for value in student.values():
#     print(f"Wert: {value}")


# # Über Schlüssel-Wert-Paare eines Dictionaries iterieren

# for key, value in student.items():
#     print(f"{key}: {value}")


# # Prüfen ob Schlüssel vorhanden ist
# print("name2" in student)   # True


# # Prüfen ob Wert vorhanden ist
# print("Anna" in student.values())   # True