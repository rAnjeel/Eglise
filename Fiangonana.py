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

    @staticmethod
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

    def get_sum_montants(date_inserer):
        try:
            connection = SqlConnection('DESKTOP-RCL8G7D\SQLEXPRESS', 'Eglise', 'sa', 'rabearison')
            connection.connect()
            cursor = connection.connection.cursor()

            cursor.execute("""
                SELECT 
                    SUM(Montant) AS Somme_Montants
                FROM 
                    Vue_Caisse
                WHERE 
                    Annee = YEAR(?)
                    AND Numero_Dimanche_Annee >= DATEPART(WEEK, CAST(CONCAT(YEAR(?), '-01-01') AS DATE)) 
                    AND Numero_Dimanche_Annee < DATEPART(WEEK, ?);
            """, (date_inserer, date_inserer, date_inserer))

            somme_montants = cursor.fetchone()[0]
            return somme_montants
        except pyodbc.Error as e:
            print(f"Erreur lors de la récupération de la somme des montants : {e}")
        finally:
            connection.close()

    @staticmethod
    def get_numero_dimanche_caisse(date_to_check):
        try:
            connection = SqlConnection('DESKTOP-RCL8G7D\SQLEXPRESS', 'Eglise', 'sa', 'rabearison')
            connection.connect()
            cursor = connection.connection.cursor()

            cursor.execute("""
                SELECT 
                    Numero_Dimanche_Annee, Numero_Dimanche_Mois
                FROM 
                    Vue_Caisse
                WHERE 
                    Date = ?
            """, (date_to_check,))

            result = cursor.fetchone()

            if result:
                return result
            else:
                return None

        except pyodbc.Error as e:
            print(f"Erreur lors de la vérification de la date dans la vue_caisse : {e}")
        finally:
            connection.close()


# Exemple d'utilisation :
dimanche = Fiangonana.get_numero_dimanche_caisse('2023-10-15')
print(dimanche[0],dimanche[1])

# Création d'un nouveau Mpiangona
# liste = Fiangonana.get_liste_caisse(1)
# for caisse in liste:
#     print(caisse.idcaisse, caisse.idFiangonana, caisse.montant, caisse.date)
#     sum = Fiangonana.get_sum_montants(caisse.date)
#     print(sum)


