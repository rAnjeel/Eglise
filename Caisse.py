import pyodbc

from SqlConnection import SqlConnection


class Caisse:
    def __init__(self, idcaisse, idFiangonana, montant, date):
        self.idcaisse = idcaisse
        self.idFiangonana = idFiangonana
        self.montant = montant
        self.date = date

    class Caisse:
        def __init__(self, idcaisse, idFiangonana, montant, date):
            self.idcaisse = idcaisse
            self.idFiangonana = idFiangonana
            self.montant = montant
            self.date = date

        @staticmethod
        def create(idFiangonana, montant, date):
            try:
                connection = SqlConnection()
                connection.connect()
                cursor = connection.connection.cursor()
                cursor.execute("INSERT INTO Caisse (idFiangonana, montant, date) VALUES (?, ?, ?)",
                               (idFiangonana, montant, date))
                connection.connection.commit()
                print("Nouvelle caisse créée avec succès.")
            except pyodbc.Error as e:
                print(f"Erreur lors de la création de la caisse: {e}")
            finally:
                connection.close()

        @staticmethod
        def read(idcaisse):
            try:
                connection = SqlConnection()
                connection.connect()
                cursor = connection.connection.cursor()
                cursor.execute("SELECT * FROM Caisse WHERE idcaisse=?", (idcaisse,))
                row = cursor.fetchone()
                if row:
                    return row
                else:
                    print("Caisse non trouvée.")
            except pyodbc.Error as e:
                print(f"Erreur lors de la lecture de la caisse: {e}")
            finally:
                connection.close()

        @staticmethod
        def update(idcaisse, idFiangonana, montant, date):
            try:
                connection = SqlConnection()
                connection.connect()
                cursor = connection.connection.cursor()
                cursor.execute("UPDATE Caisse SET idFiangonana=?, montant=?, date=? WHERE idcaisse=?",
                               (idFiangonana, montant, date, idcaisse))
                connection.connection.commit()
                print("Détails de la caisse mis à jour avec succès.")
            except pyodbc.Error as e:
                print(f"Erreur lors de la mise à jour de la caisse: {e}")
            finally:
                connection.close()

        @staticmethod
        def delete(idcaisse):
            try:
                connection = SqlConnection()
                connection.connect()
                cursor = connection.connection.cursor()
                cursor.execute("DELETE FROM Caisse WHERE idcaisse=?", (idcaisse,))
                connection.connection.commit()
                print("Caisse supprimée avec succès.")
            except pyodbc.Error as e:
                print(f"Erreur lors de la suppression de la caisse: {e}")
            finally:
                connection.close()

