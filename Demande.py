import pyodbc

from SqlConnection import SqlConnection


class Demande:
    def __init__(self, idMpino, idFiangonana, montant, date):
        self.idFiangonana = idFiangonana
        self.idMpino = idMpino
        self.montant = montant
        self.date = date

    @staticmethod
    def create(idMpino, idFiangonana, montant, date):
        try:
            connection = SqlConnection()
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("INSERT INTO Demande (idMpino, idFiangonana, montant, dateDemande) VALUES (?, ?, ?, ?)", (idMpino, idFiangonana, montant, date))
            connection.connection.commit()
            print("Nouveau demande ajouté avec succès.")
        except pyodbc.Error as e:
            print(f"Erreur lors de l'ajout du demande: {e}")
        finally:
            connection.close()

    @staticmethod
    def read(idDemande):
        try:
            connection = SqlConnection()
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("SELECT * FROM Demande WHERE idDemande=?", (idDemande,))
            row = cursor.fetchone()
            if row:
                return row
            else:
                print("Demande non trouvé.")
        except pyodbc.Error as e:
            print(f"Erreur lors de la lecture du Demande: {e}")
        finally:
            connection.close()

    @staticmethod
    def update(idDemande, idMpino, idFiangonana, montant, date):
        try:
            connection = SqlConnection()
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("UPDATE Demande SET idMpino=?, idFiangonana=?, montant=?, date=? WHERE idDemande=?", (idMpino, idFiangonana, montant, date, idDemande))
            connection.connection.commit()
            print("Détails du Demande mis à jour avec succès.")
        except pyodbc.Error as e:
            print(f"Erreur lors de la mise à jour du Demande: {e}")
        finally:
            connection.close()

    @staticmethod
    def delete(idDemande):
        try:
            connection = SqlConnection()
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("DELETE FROM Demande WHERE idDemande=?", (idDemande,))
            connection.connection.commit()
            print("Demande supprimé avec succès.")
        except pyodbc.Error as e:
            print(f"Erreur lors de la suppression du demande: {e}")
        finally:
            connection.close()
