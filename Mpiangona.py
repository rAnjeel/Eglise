import pyodbc

from SqlConnection import SqlConnection


class Mpiangona:
    def __init__(self, idMpiangona, idFiangonana, login, mdp, is_pasitera):
        self.idMpiangona = idMpiangona
        self.idFiangonana = idFiangonana
        self.login = login
        self.mdp = mdp
        self.is_pasitera = is_pasitera

    class Mpiangona:
        def __init__(self, idMpiangona, idFiangonana, login, mdp, is_pasitera):
            self.idMpiangona = idMpiangona
            self.idFiangonana = idFiangonana
            self.login = login
            self.mdp = mdp
            self.is_pasitera = is_pasitera

        @staticmethod
        def create(idFiangonana, login, mdp, is_pasitera):
            try:
                connection = SqlConnection('DESKTOP-RCL8G7D\SQLEXPRESS', 'Eglise', 'sa', 'rabearison')
                connection.connect()
                cursor = connection.connection.cursor()
                cursor.execute("INSERT INTO Mpiangona (idFiangonana, login, mdp, is_pasitera) VALUES (?, ?, ?, ?)",
                               (idFiangonana, login, mdp, is_pasitera))
                connection.connection.commit()
                print("Nouveau Mpiangona créé avec succès.")
            except pyodbc.Error as e:
                print(f"Erreur lors de la création du Mpiangona: {e}")
            finally:
                connection.close()

        @staticmethod
        def read(idMpiangona):
            try:
                connection = SqlConnection('DESKTOP-RCL8G7D\SQLEXPRESS', 'Eglise', 'sa', 'rabearison')
                connection.connect()
                cursor = connection.connection.cursor()
                cursor.execute("SELECT * FROM Mpiangona WHERE idMpiangona=?", (idMpiangona,))
                row = cursor.fetchone()
                if row:
                    return row
                else:
                    print("Mpiangona non trouvé.")
            except pyodbc.Error as e:
                print(f"Erreur lors de la lecture du Mpiangona: {e}")
            finally:
                connection.close()

        @staticmethod
        def update(idMpiangona, idFiangonana, login, mdp, is_pasitera):
            try:
                connection = SqlConnection('DESKTOP-RCL8G7D\SQLEXPRESS', 'Eglise', 'sa', 'rabearison')
                connection.connect()
                cursor = connection.connection.cursor()
                cursor.execute("UPDATE Mpiangona SET idFiangonana=?, login=?, mdp=?, is_pasitera=? WHERE idMpiangona=?",
                               (idFiangonana, login, mdp, is_pasitera, idMpiangona))
                connection.connection.commit()
                print("Détails du Mpiangona mis à jour avec succès.")
            except pyodbc.Error as e:
                print(f"Erreur lors de la mise à jour du Mpiangona: {e}")
            finally:
                connection.close()

        @staticmethod
        def delete(idMpiangona):
            try:
                connection = SqlConnection('DESKTOP-RCL8G7D\SQLEXPRESS', 'Eglise', 'sa', 'rabearison')
                connection.connect()
                cursor = connection.connection.cursor()
                cursor.execute("DELETE FROM Mpiangona WHERE idMpiangona=?", (idMpiangona,))
                connection.connection.commit()
                print("Mpiangona supprimé avec succès.")
            except pyodbc.Error as e:
                print(f"Erreur lors de la suppression du Mpiangona: {e}")
            finally:
                connection.close()

    # Exemple d'utilisation :
    # Création d'un nouveau Mpiangona
    # Mpiangona.create(1, 'login_test', 'mdp_test', True)

    # Lecture des détails du Mpiangona
    # mpiangona_details = Mpiangona.read(2)
    # print(mpiangona_details)

    # Mise à jour des détails du Mpiangona
    # Mpiangona.update(2, 1, 'admin', 'admin', True)

    # # Suppression du Mpiangona
    # Mpiangona.delete(1)


