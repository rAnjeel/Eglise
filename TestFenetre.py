from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled import Ui_MainWindow # Assurez-vous que le nom de la classe correspond à celui généré par pyuic5

class TestFenetre(QMainWindow, Ui_MainWindow): # Utilisez QMainWindow au lieu de QTestFenetre
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])
    window = TestFenetre()
    window.show()
    app.exec_()
