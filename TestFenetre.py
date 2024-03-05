from PyQt5.QtWidgets import QApplication, QMainWindow
from Fiangonana import Fiangonana
from login import Ui_MainWindow as loginWindow
from formulairerakitra import Ui_MainWindow as formulairerakitraWindow
from client import Ui_MainWindow as clientWindow

class TestFenetre(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create instances of the windows
        self.loginWindow = loginWindow()
        self.formulairerakitraWindow = formulairerakitraWindow()
        self.clientWindow = clientWindow()

        # Set up the windows
        self.loginWindow.setupUi(self)
        self.formulairerakitraWindow.setupUi(self)
        self.clientWindow.setupUi(self)

    def ShowHide(WindowX,WindowY):
        WindowX.show()
        WindowY.hide()



if __name__ == "__main__":
    app = QApplication([])
    window = TestFenetre()
    fiangonana = Fiangonana(1, 11, 11, 11, 11)

    login = loginWindow()
    login.setupUi(window)
    formrakitra = formulairerakitraWindow()
    formrakitra.setupUi(window)
    client = clientWindow()
    client.setupUi(window)

    buttonLogin = login.pushButton
    buttonLogin.clicked.connect(lambda: fiangonana.login(login.lineEdit.text(), login.lineEdit_2.text()))
    buttonLogin.clicked.connect(window.ShowHide(login,formrakitra))
    window.show()
    app.exec_()
