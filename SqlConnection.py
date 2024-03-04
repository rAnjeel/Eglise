import pyodbc

class SqlConnection:
    def __init__(self):
        self.server = 'DESKTOP-RCL8G7D\SQLEXPRESS'
        # self.server = '192.10.147.20'
        self.database = 'Eglise'
        self.username = 'sa'
        self.password = 'rabearison'
        self.connection = None

    def connect(self):
        try:
            conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}'
            self.connection = pyodbc.connect(conn_str)
            print("Connexion à la base de données réussie.")
        except pyodbc.Error as e:
            print(f"Erreur lors de la connexion à la base de données: {e}")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connexion à la base de données fermée.")

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Requête exécutée avec succès.")
        except pyodbc.Error as e:
            print(f"Erreur lors de l'exécution de la requête: {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    server = 'DESKTOP-RCL8G7D\SQLEXPRESS'  # ou le nom de votre serveur SQL Server
    database = 'Eglise'  # Nom de votre base de données
    username = 'sa'  # Nom d'utilisateur SQL Server
    password = 'rabearison'  # Mot de passe SQL Server

    connection = SqlConnection(server, database, username, password)
    connection.connect()

    query = "SELECT * FROM Caisse"
    connection.execute_query(query)

    connection.close()


