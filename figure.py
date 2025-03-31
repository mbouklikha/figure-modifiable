#Programme réalisé par BOUKLIKHA Mohamed-Amine
from tkinter import*

# Base de la fenetre
fenetre=Tk()
fenetre.config(width=500, height=500, bg="lightgrey")
fenetre.title("Rectangle réglable")

# Création du Canvas
canevas=Canvas(fenetre)
canevas.config(width=500, height=300, bg="beige")
canevas.place(x=0, y=0)

# On crée les deux points(rouge et bleu)
PointRouge=canevas.create_text(255, 155, text="+",fill="red", font=(20))
PointBleu=canevas.create_text(265, 165, text="+", fill="blue", font=(20))

#Texte qui indique la fonction des boutons
Texte1=Label(fenetre, text='Point Rouge :', bg="lightgrey")
Texte1.place(x=30, y=324)
Texte2=Label(fenetre, text='Point Bleu : ', bg="lightgrey")
Texte2.place(x=30, y=374)
Couleur=Label(fenetre, text='Couleur :', bg="lightgrey")
Couleur.place(x=30, y=424)

#Creation du Rectangle
Rectangle=canevas.create_rectangle(255, 155, 265, 165,fill='limegreen')

x = canevas.coords(PointRouge)[0]
y = canevas.coords(PointRouge)[1]
x2 = canevas.coords(PointBleu)[0]
y2 = canevas.coords(PointBleu)[1]

# Déplacement de la croix rouge
def PointRougeDroite():
    x = canevas.coords(PointRouge)[0]
    y = canevas.coords(PointRouge)[1]
    canevas.coords(PointRouge, x+10,y)
    x2 = canevas.coords(PointBleu)[0]
    y2 = canevas.coords(PointBleu)[1]
    canevas.coords(Rectangle,x+10, y, x2, y2)


BouttonD = Button(text = 'Droite', command = PointRougeDroite)
BouttonD.place(x=230, y=320)

def PointRougeGauche():
    x = canevas.coords(PointRouge)[0]
    y = canevas.coords(PointRouge)[1]
    canevas.coords(PointRouge, x-10, y)
    x2 = canevas.coords(PointBleu)[0]
    y2 = canevas.coords(PointBleu)[1]
    canevas.coords(Rectangle, x-10, y, x2, y2)

BouttonG = Button(text='Gauche', command=PointRougeGauche)
BouttonG.place(x=130, y=320)

def PointRougeHaut():
    x = canevas.coords(PointRouge)[0]
    y = canevas.coords(PointRouge)[1]
    canevas.coords(PointRouge, x, y-10)
    x2 = canevas.coords(PointBleu)[0]
    y2 = canevas.coords(PointBleu)[1]
    canevas.coords(Rectangle, x, y-10, x2, y2)

BouttonH = Button(text='Haut', command= PointRougeHaut)
BouttonH.place(x=330, y=320)

def PointRougeBas():
    x = canevas.coords(PointRouge)[0]
    y = canevas.coords(PointRouge)[1]
    canevas.coords(PointRouge, x, y+10)
    x2 = canevas.coords(PointBleu)[0]
    y2 = canevas.coords(PointBleu)[1]
    canevas.coords(Rectangle, x, y+10, x2, y2)

BouttonB = Button(text='Bas', command= PointRougeBas)
BouttonB.place(x=430, y=320)

#Déplacement de la croix bleu
def PointBleuDroite():
    x2 = canevas.coords(PointBleu)[0]
    y2 = canevas.coords(PointBleu)[1]
    canevas.coords(PointBleu, x2+10, y2)
    x = canevas.coords(PointRouge)[0]
    y = canevas.coords(PointRouge)[1]
    canevas.coords(Rectangle, x2+10, y2, x, y)

BouttonD = Button(text='Droite', command= PointBleuDroite)
BouttonD.place(x=230, y=370)

def PointBleuGauche():
    x2 = canevas.coords(PointBleu)[0]
    y2 = canevas.coords(PointBleu)[1]
    canevas.coords(PointBleu, x2-10, y2)
    x = canevas.coords(PointRouge)[0]
    y = canevas.coords(PointRouge)[1]
    canevas.coords(Rectangle, x2-10, y2, x, y)

BouttonG = Button(text='Gauche', command= PointBleuGauche)
BouttonG.place(x=130, y=370)

def PointBleuHaut():
    x2 = canevas.coords(PointBleu)[0]
    y2 = canevas.coords(PointBleu)[1]
    canevas.coords(PointBleu, x2, y2-10)
    x = canevas.coords(PointRouge)[0]
    y = canevas.coords(PointRouge)[1]
    canevas.coords(Rectangle, x2, y2-10, x, y)

BouttonH = Button(text='Haut', command= PointBleuHaut)
BouttonH.place(x=330, y=370)

def PointBleuBas():
    x2 = canevas.coords(PointBleu)[0]
    y2 = canevas.coords(PointBleu)[1]
    canevas.coords(PointBleu, x2, y2+10)
    x = canevas.coords(PointRouge)[0]
    y = canevas.coords(PointRouge)[1]
    canevas.coords(Rectangle, x2, y2+10, x, y)

BouttonB = Button(text='Bas', command= PointBleuBas)
BouttonB.place(x=430, y=370)

#Couleur de la figure
def Vert():
    canevas.itemconfig(Rectangle,fill='limegreen')
BouttonVt = Button(text='Vert', command=Vert)
BouttonVt.place(x=130, y=420)

def Rouge():
    canevas.itemconfig(Rectangle,fill='red')
BouttonRd = Button(text='Rouge', command = Rouge)
BouttonRd.place(x=200, y=420)

def Bleu():
    canevas.itemconfig(Rectangle,fill='blue')
BouttonBu = Button(text='Bleu', command = Bleu)
BouttonBu.place(x=280, y=420)

def Jaune():
    canevas.itemconfig(Rectangle, fill='yellow')
BouttonOe = Button(text='Jaune', command = Jaune)
BouttonOe.place(x=350, y=420)

def Blanc():
    canevas.itemconfig(Rectangle,fill='white')
BouttonBc = Button(text='Blanc', command = Blanc)
BouttonBc.place(x=430, y=420)

fenetre.mainloop()









