from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import Qt

def sonmi(x):
    try:
        int(x)
        return True
    except:
        return False

def plus_s():
    if sonmi(line1.text()) and sonmi(line2.text()):
        javob.setText(str(int(line1.text())+int(line2.text())))
def minus_s():
    if sonmi(line1.text()) and sonmi(line2.text()):
        javob.setText(str(int(line1.text())-int(line2.text())))
def kopaytir_s():
    if sonmi(line1.text()) and sonmi(line2.text()):
        javob.setText(str(int(line1.text())*int(line2.text())))
def chop_s():
    if sonmi(line1.text()) and sonmi(line2.text()):
        javob.setText(str(int(line1.text())/int(line2.text())))
 
app = QApplication(sys.argv)
w = QMainWindow()
w.resize(500, 500)


line1 = QLineEdit(w)  # Highlight: QLineEdit
line1.move(20, 20)
line1.resize(150, 20)
line1.setPlaceholderText("son kirit yoki ishlamaydi")


line2 = QLineEdit(w)  # Highlight: QLineEdit
line2.move(190, 20)
line2.resize(150, 20)
line2.setPlaceholderText("son kirit yoki ishlamaydi")

plus = QPushButton("+", w)  # Highlight: QPushButton
plus.move(50, 50)
plus.clicked.connect(plus_s)

minus = QPushButton("-", w)  # Highlight: QPushButton
minus.move(120, 50)
minus.clicked.connect(minus_s)

koop = QPushButton("*", w)  # Highlight: QPushButton
koop.move(190, 50)
koop.clicked.connect(kopaytir_s)

bol = QPushButton("/", w)  # Highlight: QPushButton
bol.move(260, 50)
bol.clicked.connect(chop_s)
 
javob = QLabel("🌟 Salom USER!", w)  # Highlight: QLabel
javob.move(50, 100)


w.setWindowTitle("QMainWindow misol - Asosiy oynа")

w.show()
sys.exit(app.exec_())