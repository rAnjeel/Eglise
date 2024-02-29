class Caisse:
    def __init__(self, idcaisse, idFiangonana, montant, date):
        self.idcaisse = idcaisse
        self.idFiangonana = idFiangonana
        self.montant = montant
        self.date = date

    # Fonction pour créer une nouvelle caisse
    def create(self, idcaisse, idFiangonana, montant, date):
        self.idcaisse = idcaisse
        self.idFiangonana = idFiangonana
        self.montant = montant
        self.date = date

    # Fonction pour lire les détails de la caisse
    def read(self):
        return f"ID Caisse: {self.idcaisse}, ID Fiagonana: {self.idFiangonana}, Montant: {self.montant}, Date: {self.date}"

    # Fonction pour mettre à jour les détails de la caisse
    def update(self, idFiangonana, montant, date):
        self.idFiangonana = idFiangonana
        self.montant = montant
        self.date = date

    # Fonction pour supprimer la caisse
    def delete(self):
        self.idcaisse = None
        self.idFiangonana = None
        self.montant = None
        self.date = None

# Exemple d'utilisation
caisse = Caisse(1, 101, 500, '2024-02-28')

# Création d'une nouvelle caisse
caisse.create(2, 102, 700, '2024-02-28')

# Lecture des détails de la caisse
print(caisse.read())

# Mise à jour des détails de la caisse
caisse.update(103, 800, '2024-02-28')

# Lecture des détails de la caisse mis à jour
print(caisse.read())

# Suppression de la caisse
caisse.delete()

# Lecture des détails de la caisse après suppression
print(caisse.read())  # Cela devrait afficher les attributs comme None car la caisse a été supprimée
