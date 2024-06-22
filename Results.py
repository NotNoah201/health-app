from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QRadioButton
from testscreen import *

app = QApplication([])
main_window = QWidget()
main_window.show()

main_window.setWindowTitle("RESULTS")
main_window.resize(1920, 1080)
main_window.move(0,0)

text1 = QLabel('HEEEELO HOW IS THY')

vertical = QVBoxLayout() 

vertical.addWidget(text1, alignment = Qt.AlignCenter)
main_window.setLayout(vertical)

app.exec_()