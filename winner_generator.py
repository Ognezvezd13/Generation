from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from random import randint
app = QApplication([])
my_win = QWidget()
my_win.resize(400,200)
label =QLabel('Победитель')
label_win =QLabel('?')
button = QPushButton('Сгенерировать')
line = QVBoxLayout()
line.addWidget(label,alignment=Qt.AlignCenter)
line.addWidget(label_win,alignment=Qt.AlignCenter)
line.addWidget(button,alignment=Qt.AlignCenter)
def show_winner():
    number = randint(1,100)
    label_win.setText(str(number))
button.clicked.connect(show_winner)
my_win.setLayout(line)
my_win.show()
app.exec_()