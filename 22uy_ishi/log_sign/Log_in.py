from PyQt5.QtWidgets import *
import json

class Log_in(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,200)
        

        grid = QGridLayout()

        lbl_login = QLabel("Login:")
        self.edit_login = QLineEdit()
        self.edit_login.setPlaceholderText("login kiriting")

        lbl_parol = QLabel("Parol:")
        self.edit_parol = QLineEdit()
        self.edit_parol.setPlaceholderText("parol kiriting")

        btn = QPushButton("Kirish")
        btn.clicked.connect(self.check_user)


        grid.addWidget(lbl_login)
        grid.addWidget(self.edit_login)
        grid.addWidget(lbl_parol)
        grid.addWidget(self.edit_parol)
        grid.addWidget(btn)


        self.setLayout(grid)
        self.show()    

    def __read(self):
        try:
            with open("logins.json", "r") as fayl:
                return json.load(fayl)
        except:
            with open("logins.json", "w") as fayl:
                json.dump({}, fayl)
            return {}
    
    def check_user(self):
        logins = self.__read()
        login = self.edit_login.text()
        parol = self.edit_parol.text()
        if login in logins:
            if logins[login] == parol:
                QMessageBox.information(None, "Habar", "Siz to'g'ri parol login kiritingiz")
                self.close()
            else:
                QMessageBox.warning(None, "Ogohlantirish", "Noto'g'ri parol")
                return
        else:
            QMessageBox.warning(None, "Ogohlantirish", "Noto'g'ri login")
            return

    
    

