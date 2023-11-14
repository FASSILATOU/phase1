import argparse
from datetime import date
import json
import requests


def analyser_commande():
    parser = argparse.ArgumentParser(description = 'Recuperation des données historiques de titres boursiers')
    parser.add_argument(
        '-d','--début',
         metavar = 'Date',
        type = date.fromisoformat,dest = 'début',
        default=None,
        help = 'Date recherchée la plus ancienne (format: AAAA-MM-JJ)'
    )
    parser.add_argument(
        '-f','--fin',
        metavar = 'Date',dest= 'fin',
        type=date.fromisoformat,
        default=date.today(),
        help='Date recherchée la plus récente(format: AAAA-MM-JJ)'
    )
    parser.add_argument(
        '-v','--valeur',
        metavar = {'fermeture,ouverture,min,max,volume'},
        type = str,
        dest = 'valeur',
        choices = ['fermeture','ouverture','min','max','volume'],
        default = 'fermeture',
        help = 'la valeur désirée(par défaut:fermeture)'
    )
    parser.add_argument(
        'Symbole',metavar='symbole',
        type = str,
        nargs = '+',
        help = "Nom d'un symbole boursier"
    )
    parseur = parser.parse_args()
    if parseur.debut == None:
        parseur.debut = parseur.fin
    return parseur
analyser_commande()
def produire_historique(symbole,début,fin,valeur):
    dico1 ={}
    parser = analyser_commande()
    for symbole in parser.symboles:
       Symbole = input('Veuillez entrer un symbole:')
       url = f'https://pax.ulaval.ca/action{symbole}/historique/'
 #   params = {début,fin}
 #  réponse = requests.get(url = url,params = params)
 #   réponse = json.loads(réponse.text)
 #   dico1 = réponse['historique'][date]
 #   return(f"titre={symbole}: valeur = {valeur},début = {début},fin = {fin}"+'\n'+ (date,valeur))#
 #preciser les cas particulier 
 #utiliser un boucle pour la partie format affichage