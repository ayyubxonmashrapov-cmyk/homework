from PyQt5.QtWidgets import *
import sys

def analiz_qil():
    harflar = 0
    belgilar = 0

    text = matn.toPlainText()  # ← исправлено

    for i in text:
        if i.isalpha():
            harflar += 1
            belgilar += 1
        elif not i.isdigit():
            belgilar += 1

    result.setText(
        f"So'zlar soni: {len(text.split())}\n"
        f"Harflar soni: {harflar}\n"
        f"Belgilar soni: {belgilar}"
    )

app = QApplication(sys.argv)
w = QMainWindow()


matn = QTextEdit(w)  
matn.resize(200, 100)
matn.setPlaceholderText("son kirit yoki ishlamaydi")


button = QPushButton("analiz", w)  
button.move(200, 200)
button.clicked.connect(analiz_qil)


result = QLabel("rgege", w)  
result.move(50, 200)
result.resize(200,200)


w.setWindowTitle("QMainWindow misol - Asosiy oynа")
w.resize(500, 500)
w.show()
sys.exit(app.exec_())
