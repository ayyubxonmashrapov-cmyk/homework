from PyQt5.QtWidgets import*
import sys
from PyQt5.QtCore import Qt

def chiz():
    s=int(son1.text())
    result = ""
    for i in range(s):
        result+=" * "*s
        result+="\n"
    lbl.setText(result)

app=QApplication(sys.argv)
w=QWidget()

son1 = QLineEdit("", w)
son1.move(100,100)

knopka=QPushButton("Chizing",w)
knopka.move(200,100)
knopka.clicked.connect(chiz)

lbl=QLabel("saafja", w)
lbl.move(250,300)
lbl.resize(300,300)

w.resize(1000,800)
w.show()
sys.exit(app.exec_())