from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel

X = 0

def action1():
    global X
    X = X + 1
    lbl1.setText("  X = " + str(X))

def action2():
    global X
    X = X - 1
    lbl1.setText("  X = " + str(X))

app = QApplication([])

fen = QWidget()
fen.setGeometry(150, 150, 350, 200)
fen.setWindowTitle("--- Exemple 2 ---")

lbl1 = QLabel(fen)
lbl1.setText("  X = " + str(X))

btn1 = QPushButton(fen)
btn1.setText("Plus")
btn1.setGeometry(50, 50, 100, 40)
btn1.clicked.connect(action1)

btn2 = QPushButton(fen)
btn2.setText("Moins")
btn2.setGeometry(200, 50, 100, 40)
btn2.clicked.connect(action2)

fen.show()
app.exec()
