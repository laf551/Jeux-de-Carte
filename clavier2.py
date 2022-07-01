from tkinter import *
from  tkinter import ttk
import string

col = 0 ; ln = 0 ; x=""
#amande : mot trouvé aleatoirement 
mot_aleatoire=['amande']
mot_decomposer =[]
mot_decomposer[:0] = mot_aleatoire[0] #reçoit le mot et le decompose
result= []
indexlist=[] #tableau qui recoit tous les index des lettres trouvé
n = len(mot_decomposer) #longueur du mot
nbr_chance = 5
print(mot_decomposer)
alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)
res = False

fenetre = Tk()

menu_frame = Frame(fenetre, background="blue")
menu_frame.pack()
#menu_frame.grid( column = 1)
#menu_frame.grid_rowconfigure(0,weight=1)
#menu_frame.grid_columnconfigure(0, weight=1)
menu_frame.place(width=250,bordermode=OUTSIDE)

container = Frame(fenetre , background="red")
container.pack()

frame_clavier = Frame(container )
frame_clavier.pack()

frame_chance = Frame(container)
frame_chance.pack()

frame_affichX = Frame(container)
frame_affichX.pack()

#ttk.Label(fenetre, text="Jeu du pendu").grid( row=1)
ttk.Button(menu_frame, text = "PLAY", command = lambda: creation_clavier()).pack()
ttk.Button(menu_frame, text = "LEVEL", command =fenetre.destroy).pack()
ttk.Button(menu_frame, text = "RULES", command = lambda: regle_du_jeu()).pack()
ttk.Button(menu_frame, text = "QUIT", command =fenetre.destroy).pack()

def regle_du_jeu():
    lorem= ""
    #txt_rules =Text (container , wrap = "word" , height = 7 , width = 25 ).pack(side ="right")

    lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Nunc sed ante vitae urna porttitor dictum. Integer rutrum libero
  sed augue hendrerit, sed laoreet nisi cursus. Aenean et accumsan
  metus, a porta leo. Mauris consequat lectus sed enim rutrum porta."""

    txt_rules =ttk.Label(container, text=lorem).pack(side ="right")
    #print(lorem)

def creation_clavier():

    global x
    ln = 0 ; col = 0

    for i in range(len(alphabet_list )):

        if i<6 :

            col = col+1

        elif i==6 or i == 12 or i ==18  or  i ==24  :
            col =1
            ln = ln+1

        elif i>6:
            col = col+1

        ttk.Button(frame_clavier, text=alphabet_list[i],command= lambda x = alphabet_list[i]: jouer(x)).grid(column=col, row=ln)
        print("alphabet",len(alphabet_list[i]))
        ttk.Label(frame_chance, text='Vous avez'+str(nbr_chance)+' Chances:').grid( row=8, column=1)
    creation_X()
#Saisi_user
def jouer(a2):
    global res
    global nbr_chance
    print("on est ici : ", a2)
    #while nbr_chance > 0 and nbr_chance <6:

     #   nbr_chance=test_appartenance(a2)
    if nbr_chance >0 and nbr_chance <6:
        nbr_chance= test_appartenance(a2)
        print("nmbre de chance",nbr_chance)

def creation_X():
        for i in range(n):
            ttk.Label(frame_affichX, text="X").grid( row=11, column=i)
            result.append("X")

def win_or_lost():
    var = ""
    if res == True:
        var = "Felicitation, vous avez gagner"
    elif nbr_chance == 0:
         var="Désolée, vous avez perdu"

    ttk.Label(frame_chance, text= var).grid( row=12)
#def clavier_click(a2,nbr_chance): #x = [A ou M... Z]


def test_appartenance(lettre):
    global nbr_chance, res
    if lettre in mot_decomposer:
        indexlist=[]
        for i in range(len(mot_decomposer)) :
           #print("test d'appartenance: lettre correct",lettre)
           if lettre  == mot_decomposer[i]:
                indexlist.append(i)
        for j in indexlist:
            print("result",result)
            result[j]=lettre



        for i in range(n):
            ttk.Label(frame_affichX, text=result[i]).grid( row=11, column=i)


    else:
        print(nbr_chance)
        nbr_chance = nbr_chance - 1
        aff=ttk.Label(fenetre, text='Vous avez '+str(nbr_chance)+' Chances:').grid( row=8, column=1)

    if nbr_chance ==0 :
        res = False
    elif (result == mot_decomposer):
        res = True
    win_or_lost()


    return nbr_chance

#def Image_affiche():
 #   Label(container, text='Setting', font=('Verdana', 15)).pack(side=BOTTOM, pady=10)

    # Créer un objet photoimage pour utiliser l'image
  #  photo = PhotoImage(file = r"C:\Users\WTLX\Desktop\icon.png")
    # Ajouter l'image dans le bouton
   # Button(gui, image=photo).pack(side=TOP)


    #creation_clavier()
    #jouer()

fenetre.title("Jeu du pendu")
fenetre.geometry("800x600") 
fenetre.minsize(480,360)
fenetre.iconbitmap("C:\Dev\Mes_projets\pendu.ico")
fenetre.config(background="#F2B33D")

fenetre.mainloop()
