# Erhöhen der Iterationen für eine genauere Berechnung des Potenzturms
def potenzturm_bessere_approx(x, iterations=200):
    y = x
    for _ in range(iterations):
        y = x**y
    return y

# Berechnen der Potenzturm-Werte für jedes x mit mehr Iterationen
y_values_bessere_approx = [potenzturm_bessere_approx(x) for x in x_values]

# Finden des maximalen y-Werts
max_y = max(y_values_bessere_approx)
max_y_gerundet = round(max_y, 3)

# Plotten der Potenzturm-Funktion mit mehr Iterationen
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values_bessere_approx, label=r'$x^{x^{x^{x^{\cdots}}}}$', color='orange')
plt.title("Potenzturm-Funktion mit mehr Iterationen $x^{x^{x^{x^{\cdots}}}}$")
plt.xlabel("$x$")
plt.ylabel("Funktionswert")
plt.grid(True)
plt.legend()
plt.show()

max_y_gerundet
