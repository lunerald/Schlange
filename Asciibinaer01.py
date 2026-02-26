# Funktion, um eine Zeichenkette in Binärcode umzuwandeln
def string_to_binary(input_string):
    return ' '.join(format(ord(char), '08b') for char in input_string)

# Abfrage der Eingabe
user_input = input("Gib eine Zeichenkette ein: ")

# Umwandlung in Binärcode und Ausgabe
binary_output = string_to_binary(user_input)
print(f"Der Binärcode der Zeichenkette ist: {binary_output}")
