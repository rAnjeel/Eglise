import pyodbc

from SqlConnection import SqlConnection

class Fiangonana:
    def __init__(self, idFiangonana, Argent_Actuelle, ListeMpino, ListePret, ListeCaisse):
        self.idFiangonana = idFiangonana
        self.Argent_Actuelle = Argent_Actuelle
        self.ListeCroyant = ListeMpino
        self.ListePret = ListePret
        self.ListeCaisse = ListeCaisse

    @staticmethod
    def insert(nom):
        try:
            connection = SqlConnection('DESKTOP-RCL8G7D\SQLEXPRESS', 'Eglise', 'sa', 'rabearison')
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("INSERT INTO Fiangonana (nom) VALUES (?)", (nom))
            connection.connection.commit()
            print("Nouveau Fiangonana inséré avec succès.")
        except pyodbc.Error as e:
            print(f"Erreur lors de l'insertion du Fiangonana: {e}")
        finally:
            connection.close()

    @staticmethod
    def get_liste_croyants(idFiangonana):
        try:
            connection = SqlConnection('DESKTOP-RCL8G7D\SQLEXPRESS', 'Eglise', 'sa', 'rabearison')
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("SELECT * FROM Mpiangona WHERE idFiangonana=?", (idFiangonana,))
            rows = cursor.fetchall()
            croyants = []
            for row in rows:
                croyants.append(row)
            return croyants
        except pyodbc.Error as e:
            print(f"Erreur lors de la récupération de la liste des croyants: {e}")
        finally:
            connection.close()


 # Exemple d'utilisation :
# Création d'un nouveau Mpiangona
liste = Fiangonana.get_liste_croyants(1)
print(liste)