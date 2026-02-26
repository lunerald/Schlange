import random

# Die Optionen für das Spiel
optionen = ['Schere', 'Stein', 'Papier', 'Brunnen']

# Die Spiellogik
def spiel_logik(spieler_wahl, computer_wahl):
    if spieler_wahl == computer_wahl:
        return 'Unentschieden'
    elif (spieler_wahl == 'Schere' and computer_wahl == 'Papier') or \
        (spieler_wahl == 'Papier' and (computer_wahl == 'Stein' or computer_wahl == 'Brunnen')) or \
        (spieler_wahl == 'Stein' and computer_wahl == 'Schere') or \
        (spieler_wahl == 'Brunnen' and (computer_wahl == 'Stein' or computer_wahl == 'Schere')):
        return 'Spieler gewinnt'
    else:
        return 'Computer gewinnt'

# Statistik für Gewinne initialisieren
gewinn_statistik = {
'Schere': 0,
'Stein': 0,
'Papier': 0,
'Brunnen': 0
}

# Statistik für Gesamtspiele initialisieren
gesamt_statistik = {
'Spieler gewinnt': 0,
'Computer gewinnt': 0,
'Unentschieden': 0
}

# Simulation von 100 Spielen
for _ in range(1000):
      spieler_wahl = random.choice(optionen)
      computer_wahl = random.choice(optionen)
      ergebnis = spiel_logik(spieler_wahl, computer_wahl)
      gesamt_statistik[ergebnis] += 1
      if ergebnis == 'Spieler gewinnt':
        gewinn_statistik[spieler_wahl] += 1

# Ergebnisse ausgeben
print("Gesamtergebnisse:")
for ergebnis, anzahl in gesamt_statistik.items():
     print(f"{ergebnis}: {anzahl} mal")

# Absolute Häufigkeiten für die Gewinne der einzelnen Optionen ausgeben
print("\nAbsolute Häufigkeiten für die Gewinne der einzelnen Optionen:")
for option, anzahl in gewinn_statistik.items():
     print(f"{option}: {anzahl} mal")

