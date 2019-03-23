import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

# SQL-Abfrage
sql = "SELECT * FROM personen"

# Kontrollausgabe der SQL Abfrage
print(sql+'\n')

# Absenden der SQL Abfrage
# Empfang des Ergebnisses
cursor.execute(sql)
print(cursor)
print()
# Ausgabe des Ergebnisses
for dsatz in cursor:
    # Datensatz ist ein Array aus den Spalten
    # Datensatz an der Stelle k ist eine Spalte
    print(dsatz[0], dsatz[1], dsatz[2],
          dsatz[3], dsatz[4], sep=' | ')
    print('only dataset: ', sep='', end=' ')
    print(dsatz)

# Verbindung beenden
connection.close()
