from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class PageThree(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("RESULTS")
        self.resize(1920, 1080)
        self.move(0, 0)

        text1 = QLabel('HEEEELO HOW IS THY', self)
        text1.setAlignment(Qt.AlignCenter)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(text1, alignment=Qt.AlignCenter)

        self.setLayout(vertical_layout)
