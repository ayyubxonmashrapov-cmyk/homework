from PyQt5.QtWidgets import *
import json
def load_films():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except:
        with open("data.json", "w") as file:
            json.dump([],file, indent=4)
            return []

def dump_films(films):
    with open("data.json", "w") as file:
        json.dump(films, file, indent=4)


class Film(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(458, 500)
        grid = QGridLayout()

        lbl_name = QLabel("Film nomi")
        self.edit_name = QLineEdit()

        lbl_rej = QLabel("Rejissor")
        self.edit_rej = QLineEdit()

        lbl_year = QLabel("Yili")
        self.edit_year = QLineEdit()

        lbl_janr = QLabel("Janr")
        self.edit_janr = QLineEdit()

        self.btn_qosh = QPushButton("Qo'shish")
        self.btn_tah = QPushButton("tahrirlash")
        self.btn_ochir = QPushButton("O'chirish")

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Nomi", "Rejissor", "Yili", "Janr"])


        grid.addWidget(lbl_name, 0,0)
        grid.addWidget(self.edit_name, 1,0,1,3)
        grid.addWidget(lbl_rej, 2,0)
        grid.addWidget(self.edit_rej, 3,0,1,3)
        grid.addWidget(lbl_year, 4,0)
        grid.addWidget(self.edit_year, 5,0,1,3)
        grid.addWidget(lbl_janr, 6,0)
        grid.addWidget(self.edit_janr, 7,0,1,3)
        grid.addWidget(self.btn_qosh, 8,0)
        grid.addWidget(self.btn_tah, 8,1)
        grid.addWidget(self.btn_ochir, 8,2)
        grid.addWidget(self.table, 9,0,1,3)
        
        #events
        self.btn_qosh.clicked.connect(self.qosh)
        self.btn_ochir.clicked.connect(self.ochir)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)

        self.chiqaz()

        self.setLayout(grid)
        self.show()
    
    def tekshir(self):
        if not self.edit_name.text():
            QMessageBox.warning(None, "nomalum film nomi", "film nomi kiritilmadi")
            return True
        if not self.edit_rej.text():
            QMessageBox.warning(None, "nomalum rejissor", "rejissor kiritilmadi")
            return True
        if not self.edit_year.text():
            QMessageBox.warning(None, "nomalum yil", "yil kiritilmadi")
            return True
        if not self.edit_janr.text():
            QMessageBox.warning(None, "nomalum janr", "janr kiritilmadi")
            return True
    
    def chiqaz(self):

        films = load_films()
        if self.edit_name.text():
            films.append([self.edit_name.text(), self.edit_rej.text(), self.edit_year.text(), self.edit_janr.text()])
        dump_films(films)

        self.table.setRowCount(len(films))
        

        for i, film in enumerate(films):
            self.table.setItem(i, 0, QTableWidgetItem(film[0]))
            self.table.setItem(i, 1, QTableWidgetItem(film[1]))
            self.table.setItem(i, 2, QTableWidgetItem(film[2]))
            self.table.setItem(i, 3, QTableWidgetItem(film[3]))

    def qosh(self):
        if self.tekshir():
            return
        self.chiqaz()

    def ochir(self):
        if not self.table.currentItem():
            QMessageBox.information(None, "habar", "ochiriladigan narsa tanlanmadi, tanlang")
            return
        else: 
            result = QMessageBox.warning(None, "ogohlantirish", f"{self.table.currentItem().row()+1}-chi qatorni aniq o'chirishni istaysizmi", QMessageBox.Yes | QMessageBox.No)
            if result == QMessageBox.No:
                return
        films = load_films()
        films.pop(self.table.currentItem().row())
        dump_films(films)

        self.chiqaz()

    
app = QApplication([])
f = Film()
app.exec()