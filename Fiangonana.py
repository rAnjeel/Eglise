import pyodbc

from Caisse import Caisse
from Pret import Pret
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

    @staticmethod
    def create_view_caisse(year1, year2):
        try:
            conn = SqlConnection('DESKTOP-RCL8G7D\SQLEXPRESS', 'Eglise', 'sa', 'rabearison')
            conn.connect()
            cursor = conn.connection.cursor()

            cursor.execute(
                "IF EXISTS (SELECT * FROM sys.views WHERE name = 'Vue_Caisse') BEGIN DROP VIEW Vue_Caisse; END")

            cursor.execute(f"""
                    CREATE VIEW Vue_Caisse AS
                    SELECT
                        dateInsertion AS Date,
                        YEAR(dateInsertion) AS Annee,
                        DENSE_RANK() OVER (ORDER BY DATEPART(WEEK, dateInsertion)) AS Numero_Dimanche_Annee,
                        DENSE_RANK() OVER (PARTITION BY YEAR(dateInsertion), MONTH(dateInsertion) ORDER BY DATEPART(WEEK, dateInsertion)) AS Numero_Dimanche_Mois,
                        montant AS Montant
                    FROM caisse
                    WHERE YEAR(dateInsertion) = {year1} OR YEAR(dateInsertion) = {year2}
                """)

            conn.connection.commit()
            print("La vue a été créée ou remplacée avec succès.")

        except pyodbc.Error as e:
            print(f"Erreur lors de la création ou du remplacement de la vue : {e}")

        finally:
            if conn:
                conn.close()

    def get_liste_caisse(idFiangonana):
        try:
            connection = SqlConnection('DESKTOP-RCL8G7D\SQLEXPRESS', 'Eglise', 'sa', 'rabearison')
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("SELECT * FROM caisse WHERE idFiangonana=?", (idFiangonana,))
            rows = cursor.fetchall()
            caisses = []
            for row in rows:
                caisses.append(Caisse(*row))
            return caisses
        except pyodbc.Error as e:
            print(f"Erreur lors de la récupération de la liste des caisses : {e}")
        finally:
            connection.close()

    @staticmethod
    def get_liste_prets(idFiangonana):
        try:
            connection = SqlConnection('DESKTOP-RCL8G7D\SQLEXPRESS', 'Eglise', 'sa', 'rabearison')
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("SELECT * FROM Pret WHERE idFiangonana=?", (idFiangonana,))
            rows = cursor.fetchall()
            prets = []
            for row in rows:
                prets.append(Pret(*row))
            return prets
        except pyodbc.Error as e:
            print(f"Erreur lors de la récupération de la liste des prêts : {e}")
        finally:
            connection.close()

# Exemple d'utilisation :
# Création d'un nouveau Mpiangona
liste = Fiangonana.get_liste_caisse(1)
for caisse in liste:
    print(caisse.idcaisse, caisse.idFiangonana, caisse.montant, caisse.date)
