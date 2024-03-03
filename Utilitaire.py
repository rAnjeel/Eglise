class Utilitaire:
    @staticmethod
    def calculer_pourcentage_diminution(somme_dons_2023, somme_dons_2024):
        # Calcul de la différence absolue
        difference_absolue = abs(somme_dons_2024 - somme_dons_2023)

        # Calcul du pourcentage de diminution
        if somme_dons_2023 != 0:
            pourcentage_diminution = (difference_absolue / somme_dons_2023) * 100
        else:
            pourcentage_diminution = 0

        return pourcentage_diminution

    @staticmethod
    def arrondir_chiffre(nombre, nb_chiffres_apres_virgule):
        return round(nombre, nb_chiffres_apres_virgule)




# Exemple d'utilisation
somme_dons_2023 = 1203600
somme_dons_2024 = 15000
pourcentage = Utilitaire.calculer_pourcentage_diminution(somme_dons_2023, somme_dons_2024)
print(f"Pourcentage de diminution : {pourcentage}%")
print(f"Pourcentage de diminution : {Utilitaire.arrondir_chiffre(pourcentage,3)}%")
