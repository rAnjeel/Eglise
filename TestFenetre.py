from PyQt5.QtWidgets import QApplication, QMainWindow
from login import Ui_MainWindow # Assurez-vous que le nom de la classe correspond à celui généré par pyuic5
#from misyCalendrier import Ui_MainWindow
#from formulairerakitra import Ui_MainWindow
class TestFenetre(QMainWindow, Ui_MainWindow): # Utilisez QMainWindow au lieu de QTestFenetre
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])
    window = TestFenetre()
    window.show()
    app.exec_()
