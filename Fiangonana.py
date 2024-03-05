import datetime

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
            connection = SqlConnection()
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
    def login(login_input, mdp_input):
        try:
            # Instanciation de la classe SqlConnection
            connection = SqlConnection()
            connection.connect()  # Connexion à la base de données
            cursor = connection.connection.cursor()

            # Requête pour vérifier le login et le mot de passe
            query = "SELECT is_pasitera FROM Mpiangona WHERE login = ? AND mdp = ?"
            cursor.execute(query, (login_input, mdp_input))
            result = cursor.fetchone()

            if result is None:
                raise Exception("Login ou mot de passe incorrect.")

            # Retourner 0 si is_pasitera est True, sinon 1
            if result[0] == True :
                print("PASITERA")
                return 0
            else :
                print("MPINO")
                return 1

        except Exception as e:
            print(f"Erreur lors de la connexion : {e}")
            return -1
        finally:
            if connection:
                connection.close()  # Fermeture de la connexion à la base de données

    def log(self, username ,password):
        print("username : ->", username, "password : ->", password)
        if username == "admin" and password == "admin":
            print ("OKE TAFIDITRA")
        else:
            print ("Tsy tafiditra")


    @staticmethod
    def get_liste_croyants(idFiangonana):
        try:
            connection = SqlConnection()
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
            conn = SqlConnection()
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
            connection = SqlConnection()
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
            connection = SqlConnection()
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
            connection = SqlConnection()
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
            connection = SqlConnection()
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

    @staticmethod
    def get_dimanches_suivant(date_to_check):
        try:
            connection = SqlConnection()
            connection.connect()
            cursor = connection.connection.cursor()

            cursor.execute("""
                SELECT 
                    Date 
                FROM 
                    Vue_Caisse
                WHERE 
                    Date > ?
                ORDER BY Date
            """, (date_to_check,))

            results = cursor.fetchall()

            if results:
                return results
            else:
                return None

        except pyodbc.Error as e:
            print(f"Erreur lors de la récupération des dates des dimanches après la date spécifiée : {e}")
        finally:
            connection.close()

    @staticmethod
    def get_dimanche_precedent(date_to_check):
        try:
            connection = SqlConnection()
            connection.connect()
            cursor = connection.connection.cursor()

            cursor.execute("""
                SELECT TOP 1 Date
                FROM Vue_Caisse
                WHERE Date < ?
                ORDER BY Date DESC;
            """, (date_to_check,))

            results = cursor.fetchall()

            if results:
                return results
            else:
                return None

        except pyodbc.Error as e:
            print(f"Erreur lors de la récupération des dates des dimanches après la date spécifiée : {e}")
        finally:
            connection.close()


    @staticmethod
    def get_numero_dimanche_caisse(date_to_check):
        try:
            connection = SqlConnection()
            connection.connect()
            cursor = connection.connection.cursor()

            cursor.execute("""
                DECLARE @DateToCheck DATE = ?;
                SELECT 
                    Numero_Dimanche_Annee, Numero_Dimanche_Mois
                FROM 
                    Vue_Caisse
                WHERE 
                    Date = (
                        SELECT 
                            DATEADD(day, -DATEPART(WEEKDAY, @DateToCheck), @DateToCheck) AS PreviousYearSunday
                    );
            """, (date_to_check,))

            result = cursor.fetchone()

            if result:
                return result
            else:
                return None

        except pyodbc.Error as e:
            print(f"Erreur lors de la vérification de la date dans la vue_caisse : {e}")
        finally:
            if connection:
                connection.close()

    #Fonction pour recuperer la derniere date du collecte Rakitra
    def check_date_exists(date_to_check):
        try:
            connection = SqlConnection()
            connection.connect()
            cursor = connection.connection.cursor()

            # Vérifier si la date existe dans la base de données
            cursor.execute("SELECT Date FROM Vue_Caisse WHERE Date = ?", (date_to_check))
            row = cursor.fetchone()

            # Si la date n'est pas trouvée, vérifier le dimanche précédent
            if row is None:
                previous_sunday_date = Fiangonana.get_dimanche_precedent(date_to_check)
                return Fiangonana.check_date_exists(previous_sunday_date[0])

            return row[0] if row else None

        except pyodbc.Error as e:
            print(f"Erreur lors de la vérification de la date dans la base de données : {e}")
            return False
        finally:
            if connection:
                connection.close()

    def date_annee_precedente(date_inserer_str):
        # Convertir la date insérée en format string en objet datetime
        date_inserer = datetime.datetime.strptime(date_inserer_str, '%Y-%m-%d').date()

        # Extraire l'année de la date insérée
        annee = date_inserer.year

        # Soustraire une année à l'année
        annee_precedente = annee - 1

        # Créer une nouvelle date avec l'année précédente et les mêmes mois et jours
        date_annee_precedente = datetime.date(annee_precedente, date_inserer.month, date_inserer.day)

        # Convertir la date de l'année précédente en format string
        date_annee_precedente_str = date_annee_precedente.strftime('%Y-%m-%d')

        return date_annee_precedente_str

    def get_date_obtention_pret(date_to_check):
        dateRakitraAnneeActuel = Fiangonana.check_date_exists(date_to_check)  #date du dernier rakitra de l'annee actuel
        dateRakitraAnneeAvant = Fiangonana.check_date_exists(Fiangonana.date_annee_precedente(date_to_check))

        sommeAnneeActuel = Fiangonana.get_sum_montants(dateRakitraAnneeActuel)
        sommeAnneePrecedent = Fiangonana.get_sum_montants(dateRakitraAnneeAvant)



# Exemple d'utilisation :
# num = Fiangonana.login('admin','admin')
# print(num)

# # Création d'un nouveau Mpiangona
# liste = Fiangonana.get_dimanches_suivant('2023-07-30')
# for caisse in liste:
#     print(caisse[0])
#     print(Fiangonana.get_numero_dimanche_caisse(caisse[0])[0])

# Test de la fonction
# Fiangonana.create_view_caisse(2024,2023)
date_to_check = '2024-02-28'
date_dimanche_annee_precedente = Fiangonana.date_annee_precedente(date_to_check)
print(date_dimanche_annee_precedente)
