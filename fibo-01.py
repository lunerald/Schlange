# Ein Programm, das eine Fibonacci-Folge bis zu einer bestimmten Zahl erzeugt
# Die Fibonacci-Folge ist eine Folge von Zahlen, bei der jede Zahl die Summe der beiden vorherigen ist
# Die ersten zwei Zahlen sind 1 und 1
# Zum Beispiel: 1, 1, 2, 3, 5, 8, 13, 21, ...

# Eine Funktion, die eine Fibonacci-Folge bis zu einer bestimmten Zahl erzeugt
def fibonacci(n):
# Eine Liste, die die Fibonacci-Folge speichert
	fib_list = []
# Die ersten zwei Zahlen sind 1 und 1
	a = 1
	b = 1
# Füge die ersten zwei Zahlen zur Liste hinzu
	fib_list.append(a)
	fib_list.append(b)
# Erzeuge die restlichen Zahlen der Folge, bis die Zahl n erreicht oder überschritten wird
	while a + b <= n:
# Die nächste Zahl ist die Summe der beiden vorherigen
		c = a + b
# Füge die nächste Zahl zur Liste hinzu
		fib_list.append(c)
# Aktualisiere die Werte von a und b
		a = b
		b = c
# Gib die Liste zurück
	return fib_list

# Eine Zahl, bis zu der die Fibonacci-Folge erzeugt werden soll
n = 100
# Rufe die Funktion auf und speichere das Ergebnis in einer Variablen
fib_result = fibonacci(n)
# Gib das Ergebnis aus
print("Die Fibonacci-Folge bis zu", n, "ist:")
print(fib_result)
