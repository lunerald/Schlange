import sympy

# Symbol definieren
x = sympy.Symbol('x')

# Beispiel-Ausdruck: x² + 5x + 6 = 0
ausdruck = x**2 + 5*x + 6

# Gleichung lösen
loesungen = sympy.solve(ausdruck, x)
print("Lösung:", loesungen)
factorisiert = sympy.factor(ausdruck)
print("Faktorisiert:", factorisiert)
