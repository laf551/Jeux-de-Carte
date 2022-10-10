
from random import *
import random 
from tkinter import *
import tkinter as tk
from turtle import width
from PIL import Image,ImageTk
import numpy as np


#perso = Image.load('hulk.jpg')
#IL y a 52 images
root= tk.Tk()
#cr = display.set_mode((500,500))
class Carte(): 
    '''Creation de la carte'''
    def __init__(self):
        self.nom=[2,3,4,5,6,7,8,9,10,"A","J","Q","R"] 
        self.couleur=["trefle", "carreau", "coeur" , "pique"]
        self.jeuxDeCarte =[]
        self.lienImage=[
            "asset/2c.gif","asset/2d.gif","asset/2h.gif","asset/2s.gif",
            "asset/3c.gif","asset/3d.gif","asset/3h.gif","asset/3s.gif",
            "asset/4c.gif","asset/4d.gif","asset/4h.gif","asset/4s.gif",
            "asset/5c.gif","asset/5d.gif","asset/5h.gif","asset/5s.gif",
            "asset/6c.gif","asset/6d.gif","asset/6h.gif","asset/6s.gif",
            "asset/7c.gif","asset/7d.gif","asset/7h.gif","asset/7s.gif",
            "asset/8c.gif","asset/8d.gif","asset/8h.gif","asset/8s.gif",
            "asset/9c.gif","asset/9d.gif","asset/9h.gif","asset/9s.gif",
            "asset/10c.gif","asset/10d.gif","asset/10h.gif","asset/10s.gif",
            "asset/Ac.gif","asset/Ad.gif","asset/Ah.gif","asset/As.gif",
            "asset/Jc.gif","asset/Jd.gif","asset/Jh.gif","asset/Js.gif",
            "asset/Qc.gif","asset/Qd.gif","asset/Qh.gif","asset/Qs.gif",
            "asset/Kc.gif","asset/Kd.gif","asset/Kh.gif","asset/Ks.gif"
        ]
        
        #declaration dict'''
        self.mesImages={}
        self.face= False
        self.labelSave = []
        #self.image=self.nomImage
        '''clé dictionnaire'''
        for i in self.nom: 
            for j in self.couleur:
                self.jeuxDeCarte.append((i,j))

        '''creation Image'''
        for i in self.lienImage:
            ppphoto = Image.open(r"C:/Dev/Mes_projets/".__add__(i))
            ppphoto = ppphoto.resize((60,80),Image.Resampling.LANCZOS)      
            img3= ImageTk.PhotoImage(ppphoto)
            self.labelSave.append(img3) # Objet recuperation image ordonné
            #print("222222222222222",self.labelSave)

        '''construction Dictionnaire avec valeur image'''    
        k=0
        for j in self.jeuxDeCarte:
            self.mesImages[j] = self.labelSave[k]
            k+=1
                
    '''Affiche tous les cartes:'''
    def Affiche(self):          
        #print(self.jeuxDeCarte)
        return self.jeuxDeCarte

    
        
       
    def tirer(self): 
        #bloc_carte.forget()
        bloc_carte.grid_forget()

        self.une_carte=random.choice(self.jeuxDeCarte)
        print("carte choisi : ",self.une_carte)
        print("son image est: ", self.mesImages[self.une_carte])
        Label(frame_une_carte, image=self.mesImages[self.une_carte]).grid(row=30, column=12,padx=10, pady=5)

    place=[]
    def ajouterImage(self,place):
        ln=0 
        col=0
        print("place        ",len(place))
        for index,i in enumerate(place):
            #print("label:::",index,i)
            #print("nombre d image : ", len(labelSave))
            if index >0 and index<9:
                col=col+1
            elif index==0 or index ==9 or index==18 or index==27 or index==36 or index==45: 
                col=0
                ln=ln+1
                
            elif index>9 :
                col= col+1
               
            self.labelCarte = Button(bloc_carte, image=i,command= lambda : self.functionClickCarte(i)).grid(row=ln, column=col,padx=10, pady=5)
            print("dooooooooooooooo            ",i)
        
        #mesImages === Grand liste
        '''for i in self.mesImages:
            print("i= ",i)   ; print("i[0]:" , i[0]); print("i[1]",i[1])
            print("essai",self.mesImages[i])

        fiche = {"nom":"Wayne", "prenom":"Bruce"}
        for cle in fiche.keys(): #nom -prenom
              print cle'''

    def afficheImage(self):  
        print("LEN",len(self.jeuxDeCarte))
        placementImg=[]
        #print("kkkkkkkkk",self.mesImages)
        print("########",self.jeuxDeCarte)
        for i in self.jeuxDeCarte: 
            '''prendre son image correspondant'''
            #print("VALLLLLLL",self.mesImages[i])
            placementImg.append(self.mesImages[i]) #values dico
        #print("PPPPP",placementImg)
        
        self.ajouterImage(placementImg)

    '''fait une mélange derriere sans afficher '''
    def melanger(self):
            #print("Bien mélanger hahahaha")
            print("AVANT             ",self.jeuxDeCarte)
            #melange_img = list(self.mesImages.items())
            random.shuffle(self.jeuxDeCarte)
            print("APRES           ",self.jeuxDeCarte)
            
    '''Mélanger tout et puis afficher'''
    def affiche_melange( self):
       c.melanger()
       c.afficheImage()

    def initialiser(self): 
        self.jeuxDeCarte=[]
        for i in self.nom: 
            for j in self.couleur:
                self.jeuxDeCarte.append((i,j))
        self.afficheImage()

    def getKey(self, val): 
        '''prendre le clé à partir de values'''
        for i in self.jeuxDeCarte:
            
            if self.mesImages[i] == i: 
                print("QQQQQQ",self.mesImages[i],i)
                print("cest ",i)
            
                return i
    def functionClickCarte(self,i)    : 
        
            
            """utiliser values du dico"""
            print("jeux de CARTE : ", i )
        #   Label(frameBouton , text= f"vous avez cliquer le  ").pack(pady=10, padx = 10, side=LEFT)
            






if __name__ =="__main__":
    c = Carte()
    
    root.geometry ( "1500x1500" )
    root.configure(background ="#deaea1")
    #f3cdc3
    frameBouton = Frame(root, bg='#a2628f')
    frameBouton.pack(side= TOP, pady = 10)
    Label(frameBouton,text="JEUX DE CARTE",background="white",fg='grey').pack(side=TOP, fill=X)
    
    frame1 = Frame(root,background="#5daea1")
    frame1.pack()  

    bloc_carte= Frame(frame1,background="#5daea1")
    bloc_carte.pack(side=LEFT,expand=True)

    frame_une_carte = Frame(frame1,background="#5daea1")
    frame_une_carte.pack(side=LEFT,expand=True)

    #listeFrame = Frame(frame1,background="#d9d9d9")
    listeFrame = Frame(frame1)
    listeFrame.pack(side=RIGHT)

    frameCarte = Frame(bloc_carte,background="pink")
    frameCarte.grid()

    ''' Label à droite LISTE'''
    liste=c.Affiche()
    liste_ligne = '\n'.join(str(i) for i in liste)
    Label(listeFrame,text=liste_ligne).pack()
  
    
    '''Affichage tout caracteristique carte en print'''
    for i in c.mesImages.items(): 
        print("DICTIONNNAIRE = ",i)
        
   

    #liste_ligne = '\n'.join(str(i) for i in liste)

     

       




    #print("*******************",liste_ligne)
    
# Dans la frameBouton (celle du haut), création des boutons
    x=[]
    boutonAfficher = Button(frameBouton, text = 'Afficher',  bg = 'grey',command=lambda:c.afficheImage() )
    boutonAfficher.pack(pady=10, padx = 10, side=LEFT)

    boutonMelanger = Button(frameBouton, text = 'Mélanger',  bg = 'grey',command= lambda:  c.melanger() )
    boutonMelanger.pack(pady=10, padx = 10, side=LEFT)

    boutonMélangerEtAfficher = Button(frameBouton, text = 'Afficher et mélanger',  bg = 'grey',command= lambda: c.affiche_melange())
    boutonMélangerEtAfficher.pack(pady=10, padx = 10, side=LEFT)

    boutonTirer = Button(frameBouton, text = 'Tirer',  bg = 'grey',command= lambda : c.tirer())
    boutonTirer.pack(pady=10, padx = 10, side=LEFT)

    boutonRAZ = Button(frameBouton, text = 'Initialisation et affichage',  bg = 'grey',command= lambda:c.initialiser())
    boutonRAZ.pack(pady=10, padx = 10, side=LEFT)

    Button(frameBouton, text = 'Quitter',  bg = 'grey',command= lambda:root.destroy()).pack(pady=10, padx = 10, side=LEFT)
    
    root.mainloop()


    
