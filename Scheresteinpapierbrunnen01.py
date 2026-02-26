import random

# Die Optionen für das Spiel
optionen = ['Schere', 'Stein', 'Papier', 'Brunnen']

# Die Spiellogik
def spiel_logik(spieler_wahl, computer_wahl):
    if spieler_wahl == computer_wahl:
        return 'Unentschieden!'
    elif (spieler_wahl == 'Schere' and computer_wahl == 'Papier') or \
        (spieler_wahl == 'Papier' and (computer_wahl == 'Stein' or computer_wahl == 'Brunnen')) or \
        (spieler_wahl == 'Stein' and computer_wahl == 'Schere') or \
        (spieler_wahl == 'Brunnen' and (computer_wahl == 'Stein' or computer_wahl == 'Schere')):
        return 'Du gewinnst!'
    else:
        return 'Du verlierst!'

# Das Spiel
def spiel():
    while True:
# Der Spieler wählt seine Option
        spieler_wahl = input("Wähle Schere, Stein, Papier oder Brunnen: ")
        if spieler_wahl not in optionen:
            print("Ungültige Eingabe. Bitte versuche es erneut.")
            continue

# Der Computer wählt seine Option
        computer_wahl = random.choice(optionen)
        print(f"Computer hat {computer_wahl} gewählt.")

# Das Ergebnis des Spiels
        ergebnis = spiel_logik(spieler_wahl, computer_wahl)
        print(ergebnis)

# Frage, ob der Spieler weiterspielen möchte
        weiterspielen = input("Möchtest du nochmal spielen? (ja/nein): ")
        if weiterspielen.lower() != 'ja':
            break

# Starte das Spiel
spiel()
