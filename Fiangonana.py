class Fiangonana:
    def __init__(self, idFiangonana, Argent_Actuelle, ListeMpino, ListePret, ListeCaisse):
        self.idFiangonana = idFiangonana
        self.Argent_Actuelle = Argent_Actuelle
        self.ListeCroyant = ListeMpino
        self.ListePret = ListePret
        self.ListeCaisse = ListeCaisse

# Exemple d'utilisation de la classe
fiangonana1 = Fiangonana(1, 10000, [], [], [])
print(fiangonana1.idFiangonana) # Affiche: 1
print(fiangonana1.Argent_Actuelle) # Affiche: 10000
print(fiangonana1.ListeCroyant) # Affiche: []
print(fiangonana1.ListePret) # Affiche: []
print(fiangonana1.ListeCaisse) # Affiche: []