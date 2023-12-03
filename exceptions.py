from datetime import date
class ErreurDate(RuntimeError):
    """Definition d'une fonction"""
    def trouve_erreur(self,debut):
        """Definition d'une fonction"""
        if debut > date.today():
            raise ErreurDate("La date specifiée est posterieure à la date du jour")
class ErreurQuantité(RuntimeError):
    """Definition d'une fonction"""
    def trouve_erreur_2(self):
        """Definition d'une fonction"""
        raise ErreurQuantité("Votre portefeuille ne possede pas suffisemment d'actions ")
class LiquiditéInsuffisante(RuntimeError):
    """Definition d'une fonction"""
    def trouve_erreur_3(self):
        """Definition d'une fonction"""
        raise LiquiditéInsuffisante("Votreportefeuille ne possede pas suffisemment de liquidité")

