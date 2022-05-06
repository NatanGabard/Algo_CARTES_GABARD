import random
from re import I

Main=[]

class Carte:
    def __init__(self,Nom,CoutMana,Descrition):
        self.Nom=Nom
        self.CoutMana=CoutMana
        self.Descrition=Descrition

    def getcarte() :
        Nom = random.randint(1, 3)
        if Nom == 1:
            Main.append("CarteEffect1")
        elif Nom == 2:
            Main.append("CarteEffect2")
        elif Nom == 3:
            Main.append("CarteEffect3")
        return Nom

    def getName(self) :
        return (self.Nom)
        
class Cristal(Carte):
    def __init__(self,Valeur):
        self.Valeur=Valeur
        Carte.__init__(self,"Cristal",0,"Quand un-e Mage joue un Cristal, il reste dans sa zone de jeu, et son mana maximum augmente de sa valeur")


class Blast(Carte):
    def __init__(self,Valeur):
        self.Valeur=5
        Carte.__init__(self,"Blast",5,"r. Un Blast peut être lancé contre une Creature ou un Mage, ce qui lui enlève un nombre depoints de vie égal à sa valeur. Un Blast est défaussé une fois qu’il a été joué")

class Créature(Carte):
    def __init__(self,Nom,CoutMana,PDV,Attaque):
        self.PDV=PDV
        self.Attaque=Attaque
        Carte.__init__(self,Nom,CoutMana,"Une Creature en jeu peut attaquer un-e Mage ou une autre Creature, auquel cas cette dernièrel’attaque ensuite en retour. Une Creature peut perdre des points de vie, et même mourir : elle passealors de la zone de jeu à la défausse")


class Mage:
    def __init__(self,Nom,PointDeVie,Mana):
        self.Nom=Nom
        self.PointDeVie=PointDeVie
        self.Mana=Mana

    def getMana(self):
        return self.Mana

    def getNom(self):
        return self.Nom

    def getPointDeVie(self):
        return self.PointDeVie



CarteEffect1 = Carte("CarteEffect1",2,"donne 2")
CarteEffect2 = Carte("CarteEffect2",3,"donne 3")
CarteEffect3 = Carte("CarteEffect3",4,"donne 4")

Joueur= Mage("MageBleu",100,10)

for i in range (5):
    print(Joueur.getNom(),"a :",Joueur.getPointDeVie(),"/100   ",Joueur.getMana(),"/10" )
    print("tu as piocher ",Carte.getcarte())
    print("tu as dans ta main",Main)
    tour = int(input("Que veut tu faire ?\n 1 : jouer une carte 2 : voir ma main 3 : passe ton tour \n"))
    if tour == 1 :
        print("tu as dans ta main",Main)
        choixcarte = int(input("Quelle carte veux tu jouer ?"))
        print(" tu joue ", Main[choixcarte])
        del Main[choixcarte]
    elif tour == 2 :
        print("tu as dans ta main",Main)
    else :
        print("tu passe ton tour")

    print("fin de tour\n")