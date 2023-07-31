# Etape 0 : Installer la librairie PyQt6
# 1- pip install PyQt6
# 2- Settings -> Interpreter -> +

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel
def action1():
    print("faire qqchose .. ")
    lbl1.setText("faire qqchose .. ")
def action2():
    print("Faire autre chose ... ")
    lbl1.setText("Faire autre chose ... ")
#-1 Étape : créer (instancier) un objet app de type QApplication qui provient de la librairie PyQt6
app = QApplication([])
#-2 Étape 2 : créer une objet fenetre QWidget
fen = QWidget()
fen.setGeometry(150, 150, 350, 200)
fen.setWindowTitle("--- Exemple 2 ---")

#-5 Étape : ajout de Qlabel
lbl1 = QLabel(fen)
lbl1.setText("Bonjour à tous ... ")

#-6 Étape : ajout
btn1 = QPushButton(fen)
btn1.setText("Faire qqchose")
btn1.setGeometry(50, 50, 100, 40)
btn1.clicked.connect(action1)


btn2 = QPushButton(fen)
btn2.setText("Faire autrechose")
btn2.setGeometry(200, 50, 120, 40)
btn2.clicked.connect(action2)



#-3 Rentre la fentre visible
fen.show()
#-4 Execute l'applcation
app.exec()