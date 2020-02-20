from tkinter import *
from colour import *
m = Tk()

disp = Canvas(m, width=500, height=500)
disp.grid(columnspan=3,row=0,column=0)

circle = disp.create_oval(0,0,500,500, fill='black')

hu = 0
satur = 50
bright = 0

def update():
    global hu, satur, bright
    print("H: "+str(hu)+"; S: "+str(satur)+"; L: "+str(bright)+";")
    disp.itemconfig(circle,fill=Color(hue=hu, saturation=satur, luminance=bright))

def updH(newH):
    global hu
    hu = newH
    update()

def updS(newS):
    global satur
    satur = newS
    update()

def updB(newB):
    global bright
    bright = newB
    update()

hSc = Scale(m, command=updH, orient="vertical", from_=0, to=1, resolution=0.00001, label="Hue")
hSc.grid(row=1, column=0)

sSc = Scale(m, command=updS, orient="vertical", from_=0, to=1, resolution=0.01, label="Saturation")
sSc.grid(row=1, column=1)

bSc = Scale(m, command=updB, orient="vertical", from_=0, to=1, resolution=0.01, label="Brightness")
bSc.grid(row=1, column=2)

hSc.set(1)
sSc.set(1.0)
bSc.set(0.5)

m.bind("<Escape>",exit)
m.mainloop()

