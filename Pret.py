import pyodbc

from SqlConnection import SqlConnection


class Pret:
    def __init__(self, idPret, idMpino, idFiangonana, montant, date):
        self.idPret = idPret
        self.idFiangonana = idFiangonana
        self.idMpino = idMpino
        self.montant = montant
        self.date = date

    @staticmethod
    def create(idMpino, idFiangonana, montant, date):
        try:
            connection = SqlConnection('DESKTOP-RCL8G7D\SQLEXPRESS', 'Eglise', 'sa', 'rabearison')
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("INSERT INTO Pret (idMpino, idFiangonana, montant, date) VALUES (?, ?, ?, ?)", (idMpino, idFiangonana, montant, date))
            connection.connection.commit()
            print("Nouveau prêt ajouté avec succès.")
        except pyodbc.Error as e:
            print(f"Erreur lors de l'ajout du prêt: {e}")
        finally:
            connection.close()

    @staticmethod
    def read(idPret):
        try:
            connection = SqlConnection('DESKTOP-RCL8G7D\SQLEXPRESS', 'Eglise', 'sa', 'rabearison')
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("SELECT * FROM Pret WHERE idPret=?", (idPret,))
            row = cursor.fetchone()
            if row:
                return row
            else:
                print("Prêt non trouvé.")
        except pyodbc.Error as e:
            print(f"Erreur lors de la lecture du prêt: {e}")
        finally:
            connection.close()

    @staticmethod
    def update(idPret, idMpino, idFiangonana, montant, date):
        try:
            connection = SqlConnection('DESKTOP-RCL8G7D\SQLEXPRESS', 'Eglise', 'sa', 'rabearison')
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("UPDATE Pret SET idMpino=?, idFiangonana=?, montant=?, date=? WHERE idPret=?", (idMpino, idFiangonana, montant, date, idPret))
            connection.connection.commit()
            print("Détails du prêt mis à jour avec succès.")
        except pyodbc.Error as e:
            print(f"Erreur lors de la mise à jour du prêt: {e}")
        finally:
            connection.close()

    @staticmethod
    def delete(idPret):
        try:
            connection = SqlConnection('DESKTOP-RCL8G7D\SQLEXPRESS', 'Eglise', 'sa', 'rabearison')
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("DELETE FROM Pret WHERE idPret=?", (idPret,))
            connection.connection.commit()
            print("Prêt supprimé avec succès.")
        except pyodbc.Error as e:
            print(f"Erreur lors de la suppression du prêt: {e}")
        finally:
            connection.close()

# Exemple d'utilisation :
# Création d'un nouveau prêt
Pret.create(1, 1, 500, '2024-02-29')

# Lecture des détails du prêt
pret_details = Pret.read(1)
print(pret_details)

# Mise à jour des détails du prêt
Pret.update(1, 2, 2, 700, '2024-03-01')

# Suppression du prêt
Pret.delete(1)