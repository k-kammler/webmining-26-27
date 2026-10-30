import pandas as pd

df = pd.read_csv('gehalt.csv')


#print(df.head())  # Zeigt die ersten 5 Zeilen


#print(df.describe())  # Zeigt grundlegende Statistik für numerische Spalten


# print(df['Name'])  # Spalte auswählen
# print(list(df['Name']))  # Spalte zu Liste konvertieren

# Zeilen auswählen, in denen Alter größer als 25 ist:
# filtered_df = df[df['Alter'] > 25]
# print(filtered_df)


# Hinzufügen einer Spalte
df['Hobby'] = ['Lesen'] * len(df)
print(df)

# Statistik einer Spalte:
# print(df['Alter'].mean())  


# Gruppieren und Aggregieren:
# grouped = df.groupby('Stadt')['Alter'].mean()
# print(grouped)


# # Neue Inhalte abspeichern:
df.to_csv('neue_daten.csv', index=False)
