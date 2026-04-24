from PyQt5.QtWidgets import *
from Log_in import Log_in
from Sing_in import Sign_in

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)

        grid = QGridLayout()

        btn = QPushButton("Log in")
        btn.clicked.connect(self.open_login)
        btn1 = QPushButton("Sing in")
        btn1.clicked.connect(self.open_signin)

        grid.addWidget(btn, 1, 0)
        grid.addWidget(btn1, 2, 0)

        self.setLayout(grid)
        self.show()


    def open_login(self):
        self.login = Log_in()
    

    def open_signin(self):
        self.signin = Sign_in()
        
        

        


app = QApplication([])
m = Main()
app.exec()