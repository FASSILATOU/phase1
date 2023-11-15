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
    if parseur.début is None:
        parseur.début = parseur.fin
    return parseur
analyser_commande()
def produire_historique(symbole,début,fin,valeur):
    parseur = analyser_commande()
    symbole = parseur.symbole
    début = parseur.début
    fin = parseur.fin
    valeur = parseur.valeur
    for date in [début,fin]:
       return(date,valeur)
produire_historique()
#def afficher_historique():
 #   parseur = analyser_commande()
#    url = f'https://pax.ulaval.ca/action{parseur.symbole}/historique/'
#    params = {f"début:{parseur.début},fin:{parseur.fin}"}
#    réponse = requests.get(url = url,params = params)
#    réponse = json.loads(réponse.text)
#    dico1 = réponse['historique'][date]
 #   print(f"titre={parseur.symbole}: valeur = {parseur.valeur},début = {repr(parseur.début)},fin = {repr(parseur.fin)}")
 #   print(produire_historique(repr(date),parseur.valeur))