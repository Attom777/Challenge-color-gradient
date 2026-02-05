from tkinter import *
import random
import time

F = Tk()

F.overrideredirect(True)
F.geometry("{0}x{1}+0+0".format(F.winfo_screenwidth(), F.winfo_screenheight()))
F.focus_set()
#F.geometry ('1080x720')
F.minsize(750, 400)
F.title("CoLoR")
F.config(background='black')

v = -1
global j
j = 0

def Lancer_m ():
    F.config(background='black')
    Q.pack(expand=YES)
    Simull()
    simu_menu_simulation.delete("Manuel")
    simu_menu_simulation.delete("Automatique")
    #play_butt.config(state=DISABLED, bg='gray')
    #Button.destroy(m)
    print("programme manuel lancé")
    simu_menu_simulation.add_command(label="Stop", command= Stop)

def Lancer_a ():
    global j
    j = 1
    simu_menu.delete("Manuel")
    simu_menu.delete("Automatique")
    Q.pack_forget()
    #play_butt.config(state=DISABLED, bg='gray')
    #Button.destroy(m)
    print("programme lancé")
    #Color_change(-1)
    simu_menu.add_command(label="Stop", command= Stop)

def Stop ():
    F.config(background='black')
    simu_menu_simulation.delete("Stop")
    Q.pack_forget()
    #m = Label(MB, text="Bienvenue", font=("Courrier", 30), bg='black', fg='white')
    #m.pack()
    simu_menu_simulation.add_command(label="Manuel", command = Lancer_m)
    #simu_menu.add_command(label="Automatique", command = Lancer_a)
    #play_butt.config(state=NORMAL, bg='red')

"""def boucleAuto(t):
    colors = ['red','orange','yellow','green','blue','indigo','purple']
    F.config(background=colors[t])
    #time.sleep(1)
    print(colors[t])
    #Color_change(t)
    #F.after(1000, Color_change (t))"""

def Manuel():
    global v
    print('changhu')
    print(v)
    if v == 6:
        Q.pack_forget()
        F.config(background="gray")
        v = 0
        print("Fini")
        Stop()
    else:
        v = v+1
        print(v)
        colors = ['red','orange','yellow','green','blue','indigo','purple']
        F.config(background=colors[v])
        print(colors[v])

"""def Auto (n):
    print('change')
    print(n)
    if n == 6:
        F.config(background="gray")
        F.after(1000, Stop)
        v = 0
        print("Fini")
    else:
        v = v+1
        print(v)
        boucleAuto()"""

def APPDM():
    top=Toplevel(F)

    top.overrideredirect(True)
    top.geometry("{0}x{1}+0+0".format(F.winfo_screenwidth(), F.winfo_screenheight()))
    top.focus_set()
    top.config(background='black')

    mess = Label(top, text="Programmeur : Neo", font=("Courrier", 20), bg='red', fg='white')
    mess.pack(expand=YES)

    r = Button(top, text="Retour", font=("Courrier", 20), bg='red', fg='white', command=top.destroy)
    r.pack(side=TOP)

def APPDS():
    top=Toplevel(F)

    top.overrideredirect(True)
    top.geometry("{0}x{1}+0+0".format(F.winfo_screenwidth(), F.winfo_screenheight()))
    top.focus_set()
    top.config(background='black')

    mess = Label(top, text="Le simulateur est un programme qui va afficher les couleur de l'arc en ciel en fondu", font=("Courrier", 20), bg='red', fg='white')
    mess.pack(expand=YES)
    mess1 = Label(top, text="Sois (manuellement) ou (automatiquement).\nRetournez dans l'acceuil puis aller dans : [Fichier] > [Nouvelle simulation] > [Simulation]", font=("Courrier", 20), bg='red', fg='white')
    mess1.pack(expand=YES)

    r = Button(top, text="Retour", font=("Courrier", 20), bg='red', fg='white', command=top.destroy)
    r.pack(side=TOP)

def APPDP():
    top=Toplevel(F)

    top.overrideredirect(True)
    top.geometry("{0}x{1}+0+0".format(F.winfo_screenwidth(), F.winfo_screenheight()))
    top.focus_set()
    top.config(background='black')

    mess = Label(top, text="Il y a 'X' lignes de codes", font=("Courrier", 20), bg='red', fg='white')
    mess.pack(expand=YES)
    mess1 = Label(top, text="Temps réalisation (10 min !)", font=("Courrier", 20), bg='red', fg='white')
    mess1.pack(expand=YES)

    r = Button(top, text="Retour", font=("Courrier", 20), bg='red', fg='white', command=top.destroy)
    r.pack(side=TOP)
    
def APP():
    print("a propos")

    Menu_bar_aide = Menu(F)
    file_menu_aide = Menu(Menu_bar_aide, tearoff=0)
    #file_menu_aide.add_command(label="Retour", command =###)
    file_menu_aide.add_command(label="1. Le dévellopeur", command =APPDM)#a propos de moi
    file_menu_aide.add_command(label="2. Le simulateur", command =APPDS)#a propos du simulateur
    file_menu_aide.add_command(label="3. Le logiciel", command =APPDP)#a propos du programme
    file_menu_aide.add_separator()
    file_menu_aide.add_command(label="Accueil", command =Zero)
    file_menu_aide.add_separator()
    file_menu_aide.add_command(label="Quitter vers le bureau", command =F.destroy)

    Menu_bar_aide.add_cascade(label="Sommaire", menu=file_menu_aide)
    F.config(menu=Menu_bar_aide)

def New():
    print("nouvelle simu")
    Simull()

def Simull():
    Menu_bar_simulation = Menu(F)

    file_menu_simulation = Menu(Menu_bar_simulation, tearoff=0)
    file_menu_simulation.add_command(label="Accueil", command =Mode_reset)
    file_menu_simulation.add_separator()
    file_menu_simulation.add_command(label="Quitter vers le bureau", command =F.destroy)

    Menu_bar_simulation.add_cascade(label="Fichier", menu=file_menu_simulation)

    simu_menu_simulation = Menu(Menu_bar_simulation, tearoff=0)
    simu_menu_simulation.add_command(label="Manuel", command = Lancer_m)
    simu_menu_simulation.add_command(label="Automatique", command = Lancer_a, state=DISABLED)

    Menu_bar_simulation.add_cascade(label="Simulation", menu=simu_menu_simulation)

    F.config(menu=Menu_bar_simulation)

def Mode_reset():

    Menu_bar_default = Menu(F)

    #title_menu_default = Menu(Menu_bar_default, tearoff=0)
    #Menu_bar_default.add_cascade(label="Accueil", menu=title_menu_default)

    file_menu_default = Menu(Menu_bar_default, tearoff=0)
    file_menu_default.add_command(label="Nouvelle simulation", command =New, state=NORMAL)
    file_menu_default.add_separator()
    file_menu_default.add_command(label="Quitter vers le bureau", command =F.destroy)

    Menu_bar_default.add_cascade(label="Fichier", menu=file_menu_default)
    
    aide_menu_default = Menu(Menu_bar_default, tearoff=0)
    aide_menu_default.add_command(label="A Propos", command = APP, state=NORMAL)
    
    Menu_bar_default.add_cascade(label="Aide", menu=aide_menu_default)

    Q = Frame(F)
    #MB = Frame(F)
    I = Frame(F)

    mess = Label(I, text="Programmeur : Neo", font=("Courrier", 20), bg='red', fg='white')
    mess.pack()
    #m = Label(MB, text="Bienvenue", font=("Courrier", 30), bg='black', fg='white')
    #m.pack()
    ba = Button(Q, text="Suivant", font=("Courrier", 20), bg='red', fg='white', command= Manuel)
    ba.pack()

    Q.pack_forget()
    I.pack_forget()
    #MB.pack(expand=YES)
    F.config(menu=Menu_bar_default)

def Zero():
    Mode_reset()

if j == 0:#Menu_bar_default
    Menu_bar_default = Menu(F)
    #title_menu_default = Menu(Menu_bar_default, tearoff=0)
    #Menu_bar_default.add_cascade(label="Accueil", menu=title_menu_default)

    file_menu_default = Menu(Menu_bar_default, tearoff=0)
    file_menu_default.add_command(label="Nouvelle simulation", command =New, state=NORMAL)
    file_menu_default.add_separator()
    file_menu_default.add_command(label="Quitter vers le bureau", command =F.destroy)

    Menu_bar_default.add_cascade(label="Fichier", menu=file_menu_default)
    
    aide_menu_default = Menu(Menu_bar_default, tearoff=0)
    aide_menu_default.add_command(label="A Propos", command = APP, state=NORMAL)
    
    Menu_bar_default.add_cascade(label="Aide", menu=aide_menu_default)

    Q = Frame(F)
    #MB = Frame(F)
    I = Frame(F)

    mess = Label(I, text="Programmeur : Neo", font=("Courrier", 20), bg='red', fg='white')
    mess.pack()
    #m = Label(MB, text="Bienvenue", font=("Courrier", 30), bg='black', fg='white')
    #m.pack()
    ba = Button(Q, text="Suivant", font=("Courrier", 20), bg='red', fg='white', command= Manuel)
    ba.pack()

    Q.pack_forget()
    I.pack_forget()
    #MB.pack(expand=YES)
    F.config(menu=Menu_bar_default)
elif j == 1:
    Menu_bar_simulation = Menu(F)

    file_menu_simulation = Menu(Menu_bar_simulation, tearoff=0)
    file_menu_simulation.add_command(label="Accueil", command =Mode_reset)
    file_menu_simulation.add_separator()
    file_menu_simulation.add_command(label="Quitter vers le bureau", command =F.destroy)

    Menu_bar_simulation.add_cascade(label="Fichier", menu=file_menu_simulation)

    simu_menu_simulation = Menu(Menu_bar_simulation, tearoff=0)
    simu_menu_simulation.add_command(label="Manuel", command = Lancer_m)
    simu_menu_simulation.add_command(label="Automatique", command = Lancer_a, state=DISABLED)

    Menu_bar_simulation.add_cascade(label="Simulation", menu=simu_menu_simulation)

    F.config(menu=Menu_bar_simulation)
elif j == 2:
    prin("e")
    
F.mainloop()
