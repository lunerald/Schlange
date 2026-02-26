import tkinter
import subprocess
fenster = tkinter.Tk()

fenster.title("Drucken ?")

blatt = {'017': 'm8gegeL017','019': 'm8hypL019','015': 'm9nopL015','016': 'm9aparL016','021': 'm10potiL021','018': 'm10efuL018', '014': 'm10sifuL014','022': 'm11efunL022','020': 'm11elleL020','023': 'm11lnfuL023'}
anz = {'017': 0,'019': 0,'015': 0,'016': 0,'021': 0,'018': 0,'014': 0,'022': 0,'020': 0,'023': 0}
i = 0
zahl={}
plusknopf ={}
minusknopf={}

def zahl_plus(nu):
    
    anz[nu] += 1
    zahl[nu].config(text=anz[nu])

def zahl_minus(nu):
   
    anz[nu] -= 1
    if anz[nu] < 0:
       anz[nu] = 0
       
    zahl[nu].config(text=anz[nu])

def druck_los():
    for n, z in blatt.items():
        if anz[n] > 0:
 		for k=1,n
           subprocess.Popen(['lpr', '-#' + str(anz[n]),'home/arno/Scheune/Schule/mazlbackup/' + z + '/aa'+ n +'.pdf'])

# Label und Buttons erstellen.
for num, datei in blatt.items():

    zahl[num] = tkinter.Label(fenster, text=anz[num])
    zahl[num].grid(row=i, column=3)

    dat = tkinter.Label(fenster, text=datei)
    dat.grid(row=i, column=0)

    plusknopf[i] = tkinter.Button(fenster, text="+", command=lambda num=num: zahl_plus(num))
    plusknopf[i].grid(row=i, column=1)

    minusknopf[i] = tkinter.Button(fenster, text="-", command=lambda num=num: zahl_minus(num))
    minusknopf[i].grid(row=i, column=2)
    
    i += 1

druckenknopf = tkinter.Button(fenster, text="Drucken", command=lambda: druck_los())
druckenknopf.grid(row=i, column=0)

fenster.mainloop()



# In der Ereignisschleife auf Eingabe des Benutzers warten.

