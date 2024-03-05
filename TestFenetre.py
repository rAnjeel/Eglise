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

    def ShowHide(self, WindowX,WindowY):
        WindowX.show()
        WindowY.hide()



if __name__ == "__main__":
    app = QApplication([])
    window = TestFenetre()
    fiangonana = Fiangonana(1, 11, 11, 11, 11)

    login = loginWindow()

    formrakitra = formulairerakitraWindow()

    client = clientWindow()


    buttonLogin = login.pushButton
    login_result = buttonLogin.clicked.connect(lambda: fiangonana.login(login.lineEdit.text(), login.lineEdit_2.text()))
    if login_result == 0:
        buttonLogin.clicked.connect(lambda: window.ShowHide(login,formrakitra))
    elif login_result == 1:
        buttonLogin.clicked.connect(lambda: window.ShowHide(login,client))
    window.show()
    app.exec_()
