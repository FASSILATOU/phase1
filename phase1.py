"""Importation des modules necessaires"""
import argparse
from datetime import date
import json
import requests


def analyser_commande():
    """Etude avec le module argparse"""
    parser = argparse.ArgumentParser(
        description ='Recuperation des données historiques de titres boursiers')
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

def produire_historique(symbole_2,debut_2,fin_2,valeur_2):
    """Definition d'une nouvelle fonction utile"""
    url = f'https://pax.ulaval.ca/action/{symbole_2}/historique/'
    params = {"début":debut_2,"fin":fin_2}
    réponse = requests.get(url = url , params = params)
    réponse = json.loads(réponse.text)
    résultat = []
    for dating in sorted(réponse['historique'].keys()):
        résultat.append((date.fromisoformat(dating),réponse['historique'][dating][valeur_2]))  
    return résultat

if __name__=="__main__":
    args = analyser_commande()
    print(f"titre = {args.Symbole}: valeur = {args.valeur}, début ={args.début}, fin = {args.fin}")
    print(produire_historique(symbole_2,debut_2,fin_2,valeur_2))