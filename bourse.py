"""Importation de mes modules"""
from datetime import datetime , date,timedelta
import phase1
import requests
import json
from exceptions import ErreurDate
from datetime import date
 
class Bourse:
     """Definition de ma classe"""
     def prix(self,symbole,debut):
        """Definition de ma methode"""
        self.symbole = symbole
        self.debut = debut.strftime('%Y-%m-%d')
        url = f'https://pax.ulaval.ca/action/{symbole}/historique/'
        params = debut.strftime('%Y-%m-%d')
        reponse = requests.get(url = url , params = params, timeout = 5 )
        reponse = json.loads(reponse.text)
        #ErreurDate().trouve_erreur(debut)
        if self.debut in reponse['historique']:
            return debut,reponse['historique'][debut.strftime('%Y-%m-%d')]['fermeture']
        date_etudier = debut
        while date_etudier.strftime('%Y-%m-%d') not in reponse['historique'] and date_etudier <= date.today() :
            date_etudier = date_etudier - timedelta(days = 1)
            #date_etudier = date_etudier
        return date_etudier,reponse['historique'][date_etudier.strftime('%Y-%m-%d')]['fermeture']