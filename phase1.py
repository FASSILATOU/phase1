import argparse
from datetime import date
def analyser_commande():
    parser = argparse.ArgumentParser(description = 'Recuperation des donées historiques de titres boursiers')
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
        nargs = '+',type = str,
        help = "Nom d'un symbole boursier"
    )
    return parser.parse_args()
analyser_commande()
print("Dipama")
print("Ecole")
