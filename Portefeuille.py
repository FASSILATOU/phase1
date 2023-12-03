"""Importation du module Bourse.py"""
from datetime import datetime,date,timedelta
import datetime
from bourse import Bourse
from exceptions import ErreurDate,ErreurQuantité,LiquiditéInsuffisante 
import copy

class Portefeuille():
    """Definition de ma classe Portefeuille"""
    def __init__(self):
        self.bourse_2 = Bourse()
        self.revenu = 0
        self.dico = {}
        self.symbole = 'goog'
        self.dico_2 = {}
        self.dico_0 = {}
        self.dico_principale = {}
        self.dico_valeur_totale = {}
        self.dico_val = {}
        self.dic_3 = {}
        self.dico_valtotal = {}
        self.somme = 0
        self.som = 0
        self.som1 = 0
        self.valeur_2 = 0
        self.valeur_projeter1=0
        self.valeur=0
        self.valeur_titre = 0
        self.valeur_projeter=0
        self.valeur_projeter2=0
        self.val = 0
    def déposer(self,montant, date_2= date.today()):
        """Definition de la methode déposer"""
        ErreurDate().trouve_erreur(date_2)
        if date_2 in self.dico_2:
            self.dico_2[date_2] = self.dico_2.get(date_2)+montant
        else:
            self.dico[date_2] = montant
        self.revenu += montant
        print(self.dico)
        return self.dico
    def solde(self, date_2= date.today()):
        """definition d'une autre methode solde"""
        ErreurDate().trouve_erreur(date_2)
        for dating, vall in self.dico.items():
            if  dating <= date_2:
                self.somme += vall
        print(self.somme)
        return self.somme
    def acheter(self,symbole,quantite,date_2= date.today()):
        """Definition d'une autre methode acheter"""
        ErreurDate().trouve_erreur(date_2)
        if self.bourse_2.prix(self.symbole,date_2)[1]*quantite > self.somme:
            LiquiditéInsuffisante().trouve_erreur_3()
        else :
            if symbole in self.dico_2:
                self.dico_2[symbole] = self.dico_2.get(symbole) + quantite
            else:
                self.dico_2[symbole] = quantite
            self.revenu -=self.bourse_2.prix(self.symbole,date_2)[1]*quantite
            self.somme -= self.bourse_2.prix(self.symbole,date_2)[1]*quantite
        print(self.dico_2)
        return self.dico_2
    def vendre(self,symbole,quantite,date_2= date.today()):
        """defifintion d'une autre methode vendre"""
        if date_2 > date.today():
            ErreurDate().trouve_erreur(date_2)
        elif self.dico_2[symbole] < quantite:
            ErreurQuantité().trouve_erreur_2()
        else:
            dicto_2 = copy.deepcopy(self.dico_2)
            dicto_2[symbole] -= quantite
            #self.dico_2[symbole] = dicto_2[symbole]
            self.revenu += self.bourse_2.prix(self.symbole,date_2)[1]*quantite
            self.somme += self.bourse_2.prix(self.symbole,date_2)[1]*quantite
            #self.dico_2[symbole] = self.dico_2[symbole]-quantite
            self.dico_principale[date_2] = (self.somme,dicto_2)
        print(self.dico_principale)
    
        return self.dico_principale
    def valeur_totale(self,date_2= date.today()):
        """Définition de la méthode valeur totale"""
        for tk, tks in self.dico_2.items():
            self.dic_3[tk] = tks*self.bourse_2.prix(tk,date_2)[1]
        self.dico_valtotal[date_2] = (self.somme,self.dic_3)
        print(self.dico_valtotal)
        return self.dico_valtotal
    def valeur_des_titres(self,*symboles, date_2=date.today()):
        """Définition de la méthode valeur des titres"""
        for tk, tks in self.dico_2.items():
            self.dic_3[tk] = tks*self.bourse_2.prix(tk,date_2)[1]
        for qte in symboles:
            self.som += self.dic_3[qte]
        print(self.som)
        return self.som
    def titres(self, date_2 = date.today()):
        """Nouvellefonctiondefinit"""
        print(self.dico_principale[date_2][1])
        return self.dico_principale[date_2][1]
    def valeur_projetée(self,date_2, rendement):
        """Définition de la méthode valeur projétée"""
        for qte, cte in self.dic_3.items():
            self.som1 += cte
        date_diff = date.fromisoformat(date_2) - date.today()
        date_year = date_diff.days//365
        date_diff = date_diff.days%365
        if isinstance(rendement,float):
            self.valeur_projeter1 = self.som1*(1+rendement/100)**date_year
            self.valeur_projeter2 = self.valeur_projeter1 + self.som1*(
                (rendement/100)*(date_diff/365))
        else:
            for titre, tle in self.dic_3.items():
                if titre in rendement:
                    val_projeter1 = tle*(1 + rendement[titre]/100)**date_year
                    self.valeur_projeter2 += val_projeter1 + tle*(
                        (rendement[titre]/100)*(date_diff/365))
        print(self.valeur_projeter2)
        return self.valeur_projeter2
 
 
 
 
A = Portefeuille()
#A.déposer(513,'2022-11-02')
A.déposer(513, datetime.date(2022, 11, 2))
A.déposer(213,datetime.date(2022, 11, 4))
A.déposer(25335,datetime.date(2022, 11, 5))
A.déposer(352225,datetime.date(2022, 11, 5))
A.déposer(2000,datetime.date(2023, 12, 2))
A.solde(datetime.date(2022, 12, 2)) 
A.acheter('Goog',6,datetime.date(2023, 11, 30))
A.acheter('msft', 1)
A.acheter('Goog',2)
#A.acheter('Goog',2, datetime.date(2023, 12, 2))
A.vendre('Goog',1,datetime.date(2023, 11, 30))
A.vendre('Goog',1,datetime.date(2023, 12, 2))
#A.vendre('Goog',1,datetime.date(2023, 11, 30))
A.valeur_totale(datetime.date(2023, 11,30 ))
A.valeur_totale(datetime.date(2022, 12, 2))
print(A.valeur_totale())
A.valeur_des_titres('msft')
print(A.valeur_des_titres('Goog','msft'))
A.titres()
A.valeur_projetée('2034-12-02', {'msft': 0.5, 'Goog': 0.5})