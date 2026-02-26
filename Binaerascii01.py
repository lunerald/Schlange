# Binäre Zeichenkette einlesen und als ASCII ausgeben
while True:
    binary_string = input("Binäre Zeichenkette eingeben (z.B. 01001001): ")

    # Leerzeichen entfernen, falls vorhanden
    binary_string = binary_string.replace(" ", "")

    # Prüfen, ob die Länge durch 8 teilbar ist
    if len(binary_string) % 8 != 0:
        print("Fehler: Die Länge der Bitfolge ist kein Vielfaches von 8.")
    else:
        text = ""
        for i in range(0, len(binary_string), 8):
            byte = binary_string[i:i+8]
            char = chr(int(byte, 2))
            text += char
        print("ASCII-Ausgabe:", text)
        
        antwort = input("Noch ein Durchlauf? ").strip().lower()

        if antwort  in ("n", "nein", "no"):
            print("Alles klar, dann Schluss für heute.")
            break

