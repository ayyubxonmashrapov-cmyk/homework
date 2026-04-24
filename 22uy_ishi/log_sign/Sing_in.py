import json
from PyQt5.QtWidgets import *

class Sign_in(QWidget):

    def __init__(self, ):
        super().__init__()
        
        
        self.setStyleSheet("font-size: 18px;")
        self.resize(500,500)

        grid = QGridLayout()
        grid.setContentsMargins(40,40,40,40)


        
        lbl_ism = QLabel("Ism:")
        self.edit_ism = QLineEdit("")
        self.edit_ism.setPlaceholderText("Ism")

        lbl_login = QLabel("Login:")
        self.edit_login = QLineEdit("")
        self.edit_login.setPlaceholderText("Login")

        lbl_parol = QLabel("Parol:")
        self.edit_parol = QLineEdit("")
        self.edit_parol.setPlaceholderText("Parol")

        self.rdb_erkak = QRadioButton("Erkak")
        self.rdb_ayol = QRadioButton("Ayol")

        lbl_kasb = QLabel("Kasb:")
        self.cmb_kasb = QComboBox()
        self.cmb_kasb.addItems(["Dasturchi", "Talaba", "Ustoz"])

        self.chb1 = QCheckBox("Python")
        self.chb2 = QCheckBox("Javascript")
        self.chb3 = QCheckBox("Design")


        self.btn = QPushButton("Ro'yxatdan o'tish")
        self.btn.clicked.connect(self.register)

        grid.addWidget(lbl_ism,0,0,1,2)
        grid.addWidget(self.edit_ism,1,0,1,2)

        grid.addWidget(lbl_login,2,0,1,2)
        grid.addWidget(self.edit_login,3,0,1,2)

        grid.addWidget(lbl_parol,4,0,1,2)
        grid.addWidget(self.edit_parol,5,0,1,2)

        grid.addWidget(self.rdb_erkak,6,0)
        grid.addWidget(self.rdb_ayol,6,1)

        grid.addWidget(lbl_kasb,7,0,1,2)
        grid.addWidget(self.cmb_kasb,8,0,1,2)

        grid.addWidget(self.chb1,9,0,1,2)
        grid.addWidget(self.chb2,10,0,1,2)
        grid.addWidget(self.chb3,11,0,1,2)

        grid.addWidget(self.btn,12,0,1,2)


        self.setLayout(grid)
        self.show()


    def __write(self, data, fayl):
        with open(fayl, "w") as file:
            json.dump(data, file, indent=4)

    def __readlist(self, fayl):
        try:
            with open(fayl, "r") as file:
                return json.load(file)
        except:
            with open(fayl, "w") as file:
                json.dump([], file, indent=4)
                return []

    def __readDict(self, fayl):
        try:
            with open(fayl, "r") as file:
                return json.load(file)
        except:
            with open(fayl, "w") as file:
                json.dump({}, file, indent=4)
                return {}

    def register(self):
        if not self.edit_ism.text():
            QMessageBox.warning(None, "Ogohlantirish", "Ism kiritilmadi")
            return
        if not self.edit_login.text():
            QMessageBox.warning(None, "Ogohlantirish", "Login kiritilmadi")
            return
        if self.edit_login.text() in self.__readDict("logins.json"):
            QMessageBox.warning(None, "Ogohlantirish", "Bu login band qilingan. Qayta kiriting")
            return
        if not self.edit_parol.text():
            QMessageBox.warning(None, "Ogohlantirish", "Parol kiritilmadi")
            return
        if not self.rdb_erkak.isChecked() and not self.rdb_ayol.isChecked():
            QMessageBox.warning(None, "Ogohlantirish", "Jins tanlanmadi")
            return
        
         

        users = self.__readlist("data.json")
        lst = []
        if self.chb1.isChecked():
            lst.append(self.chb1.text())
        if self.chb2.isChecked():
            lst.append(self.chb2.text())
        if self.chb3.isChecked():
            lst.append(self.chb3.text())
        data = {
            "ismi": self.edit_ism.text(),
            "login": self.edit_login.text(),
            "parol": self.edit_parol.text(),
            "kasbi": self.cmb_kasb.currentText(),
            "jinsi": "erkak" if self.rdb_erkak.isChecked() else "ayol",
            "qiziqish": lst
        }

        logins = self.__readDict("logins.json")
        logins[self.edit_login.text()] = self.edit_parol.text()
        self.__write(logins, "logins.json")

        users.append(data)
        self.__write(users, "data.json")
        QMessageBox.information(None, "Habar", "Siz muvaffaqiyatli ro'yxatdan o'tdingiz")
        self.close()
        



    