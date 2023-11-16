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
def produire_historique(symbole,début,fin,valeur):
    parseur = analyser_commande()
    début = parseur.début
    fin = parseur.fin
    valeur = parseur.valeur
    symbole = parseur.symbole
    url = f'https://pax.ulaval.ca/action{symbole}/historique/'
    params = {"début":début,"fin":fin}
    réponse = requests.get(url=url,params=params)
    réponse_1 = json.loads(réponse.text)
    réponse_2 = [(repr(date),date["valeur"])for date in réponse_1["historique"].keys()]
    return(réponse_2)
if __name__=="__main__":
    parseur = analyser_commande()
    for symbole in parseur.symboles:
        historique = produire_historique(symbole,parseur.début,parseur.fin,parseur.valeur)
    print(historique)