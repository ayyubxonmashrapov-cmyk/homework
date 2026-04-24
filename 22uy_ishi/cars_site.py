from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)

        grid = QGridLayout()

        lbl_model = QLabel("Model")
        self.edit_model = QLineEdit()
        
        lbl_yili = QLabel("Yili")
        self.edit_yili = QLineEdit()

        lbl_rabgi = QLabel("Rangi")
        self.edit_rangi = QLineEdit()

        self.chb_avtomat = QCheckBox("Avtomat")

        lbl_turi = QLabel("Turi")
        self.rdb_sedan = QRadioButton("Sadan")
        self.rdb_suv = QRadioButton("SUV")

        self.btn_qoshish = QPushButton("Qo'shish")
        self.btn_tahrirlash = QPushButton("Tahrirlash")
        self.btn_ochirish = QPushButton("O'chirish")

        self.edit_text = QTextEdit()
        
        grid.addWidget(lbl_model,0,0)
        grid.addWidget(self.edit_model,1,0,1,3)
        grid.addWidget(lbl_yili,2,0)
        grid.addWidget(self.edit_yili,3,0,1,3)
        grid.addWidget(lbl_rabgi,4,0)
        grid.addWidget(self.edit_rangi,5,0,1,3)
        grid.addWidget(self.chb_avtomat,6,0)
        grid.addWidget(lbl_turi,7,0)
        grid.addWidget(self.rdb_sedan,8,0,1,1.5)
        grid.addWidget(self.rdb_suv,8,1,1,1.5)
        grid.addWidget(self.btn_qoshish,9,0)
        grid.addWidget(self.btn_tahrirlash,9,1)
        grid.addWidget(self.btn_ochirish,9,2)
        grid.addWidget(self.edit_text,10,0,1,3)

        self.setLayout(grid)
        self.show()


app = QApplication([])
w = Window()
app.exec()