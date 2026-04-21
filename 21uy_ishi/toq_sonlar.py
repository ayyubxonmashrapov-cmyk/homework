from PyQt5.QtWidgets import*
import sys
from PyQt5.QtCore import Qt

def sonmi(x):
    try:
        int(x)
        return True
    except:
        return False

def chiqaz():
    lst = vrode_sonlar.text().split()
    result = ""
    for i in lst:
        if sonmi(i) and int(i) % 2 == 0:
            result += f"{i} "
    lbl.setText(result)

app=QApplication(sys.argv)
w=QWidget()

vrode_sonlar = QLineEdit("", w)
vrode_sonlar.move(100,100)

knopka=QPushButton("Chizing",w)
knopka.move(300,100)
knopka.clicked.connect(chiqaz)

lbl=QLabel("saafja", w)
lbl.move(250,300)
lbl.resize(300,300)

w.resize(1000,800)
w.show()
sys.exit(app.exec_())