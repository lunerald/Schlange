import tkinter as tk

# Dateninitialisierung
Jahr = {"2017a", "2017b", "2018a", "2018b", "2019a", "2019b", "2020a", "2020b", "2021a", "2021b", "2022a", "2022b", "2023a", "2023b"}
jahre = sorted(list(Jahr))
Thema = {"Analysis", "Stochastik", "Analytische Geometrie"}
an_st = {"Änderungsrate", "e-Funktion", "Extrempunkt", "Funktionsterm ermitteln", "Ganzrationale Funktion", "Gebrochen rationale Funktion", "Integral, bestimmtes", "Integralfunktion", "ln-Funktion", "Newton-Verfahren", "Sinus/Kosinus Funktion", "Tangente", "Umkehrfunktion", "Wendepunkt", "Wurzelfunktion"}
st_st = {"Bernoulli", "Baumdiagramm", "Drei mal Mindestens", "Ereignisalgebra", "Erwartungswert", "Hypothesentest", "Kombinatorik", "Standardabweichung", "Stochastische Unabhängigkeit", "Vierfeldertafel", "Zufallsgröße"}
ag_st = {"Abstand Punkt-Gerade", "Abstand Punkt-Ebene", "Betrag Vektor", "Dreieck / Viereck", "Ebene", "Flächeninhalt, Volumen", "Gerade", "Kegel", "Kugel", "Lot auf Gerade", "Lot auf Ebene", "Punkt in Fläche", "Prisma", "Pyramide", "Schnittgerade", "Spezial 11 AG", "Winkel", "Würfel", "Zylinder"}
index_jahr = 0  # Startindex für Jahre
index_seite = 1  # Startindex für Seiten
num = int(input("Nummer? ")) #934

# Hauptfunktion zur Erstellung der Benutzeroberfläche
def create_widgets():
    global label_jahr, label_seite

    root = tk.Tk()
    root.title("Stichwörter Abi")

# Label für die Anzeige des aktuellen Jahres
    label_jahr = tk.Label(root, text=jahre[index_jahr])
    label_jahr.pack()

# Label für die Anzeige der aktuellen Seite
    label_seite = tk.Label(root, text=str(index_seite))
    label_seite.pack()

# Variable, um die ausgewählte Option zu speichern
    var = tk.StringVar(root)
    var.set("Analysis")  # Setzen der Standardoption

# Buttons für die Navigation
    btn_zurueck_jahr = tk.Button(root, text="Zurück Jahr", command=lambda: zurueck_jahr(label_jahr))
    btn_zurueck_jahr.pack(side=tk.LEFT)

    btn_vor_jahr = tk.Button(root, text="Vor Jahr", command=lambda: vor_jahr(label_jahr))
    btn_vor_jahr.pack(side=tk.RIGHT)

    btn_zurueck_seite = tk.Button(root, text="Zurück Seite", command=lambda: zurueck_seite(label_seite))
    btn_zurueck_seite.pack(side=tk.LEFT)

    btn_vor_seite = tk.Button(root, text="Vor Seite", command=lambda: vor_seite(label_seite))
    btn_vor_seite.pack(side=tk.RIGHT)

# Radiobuttons
    rb1 = tk.Radiobutton(root, text="Analysis", variable=var, value="Analysis", command=lambda: ausgewaehlte_option(var, root, label_jahr, btn_zurueck_jahr, btn_vor_jahr, btn_zurueck_seite, btn_vor_seite,))
    rb1.pack(anchor=tk.W)

    rb2 = tk.Radiobutton(root, text="Stochastik", variable=var, value="Stochastik", command=lambda: ausgewaehlte_option(var, root, label_jahr, btn_zurueck_jahr, btn_vor_jahr, btn_zurueck_seite, btn_vor_seite))
    rb2.pack(anchor=tk.W)

    rb3 = tk.Radiobutton(root, text="Analytische Geometrie", variable=var, value="Analytische Geometrie", command=lambda: ausgewaehlte_option(var, root, label_jahr, btn_zurueck_jahr, btn_vor_jahr,  btn_zurueck_seite, btn_vor_seite))
    rb3.pack(anchor=tk.W)

    root.mainloop()

# Funktionen zur Aktualisierung der Labels
def update_label_jahr(label_jahr):
    label_jahr.config(text=jahre[index_jahr])

def update_label_seite(label_seite):
    label_seite.config(text=str(index_seite))

# Funktionen für die Navigation
def vor_jahr(label_jahr):
    global index_jahr
    if index_jahr < len(jahre) - 1:
        index_jahr += 1
        update_label_jahr(label_jahr)

def zurueck_jahr(label_jahr):
    global index_jahr
    if index_jahr > 0:
        index_jahr -= 1
        update_label_jahr(label_jahr)

def vor_seite(label_seite):
    global index_seite
    if index_seite < 20:  # Angenommene maximale Seitenzahl
        index_seite += 1
        update_label_seite(label_seite)

def zurueck_seite(label_seite):
    global index_seite
    if index_seite > 0:
        index_seite -= 1
        update_label_seite(label_seite)

# Funktion, um die Checkboxen basierend auf der Auswahl zu aktualisieren
def ausgewaehlte_option(var, root, label_jahr, btn_zurueck_jahr, btn_vor_jahr, btn_zurueck_seite, btn_vor_seite):
# Entfernen aller vorhandenen Checkboxen
    for widget in root.pack_slaves():
        if isinstance(widget, tk.Checkbutton) or isinstance(widget, tk.Button) and widget not in [btn_zurueck_jahr, btn_vor_jahr, btn_zurueck_seite, btn_vor_seite]:
             widget.destroy()

# Erstellen der neuen Checkboxen basierend auf der Auswahl
        checkboxes = []
        thema_auswahl = var.get()
        stichwoerter = an_st if thema_auswahl == "Analysis" else st_st if thema_auswahl == "Stochastik" else ag_st
    for stiwo in sorted(stichwoerter):
       var_cb = tk.BooleanVar(root)
       chk = tk.Checkbutton(root, text=stiwo, variable=var_cb)
       chk.pack(anchor=tk.W)
       checkboxes.append((chk, var_cb))

# Button, um die Auswahl abzuschicken
    btn_auswahl = tk.Button(root, text='Auswahl Abschicken', command=lambda: toggle(checkboxes, thema_auswahl))
    btn_auswahl.pack()

# Funktion, um die Auswahl der Checkboxen auszugeben
def toggle(checkboxes, thema_auswahl):
    global num
    for chk, var_cb in checkboxes:
        if var_cb.get():
            print(f"({num}, '{jahre[index_jahr]}:{index_seite}', '{chk.cget('text')}', '{thema_auswahl}'),")
            var_cb.set(False)  # Zurücksetzen der Checkbox
            num += 1
    vor_seite(label_seite);
# Aufruf der Funktion zum Erstellen der Widgets
create_widgets()
