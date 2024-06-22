from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout

<<<<<<< HEAD
class PageOne(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Health")
        self.resize(1280, 720)
        self.move(0, 0)

        button = QPushButton('Start')
        text1 = QLabel('Welcome to the Health status detection program!')
        text2 = QLabel("This application allows you to use the Rufier test to make an initial diagnosis of your health.\nThe Rufier test is a set of physical exercises designed to assess your cardiac performance during physical exertion.\nThe subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds;\nthen, within 45 seconds, the subject performs 30 squats.\nWhen the exercise ends, the subject lies down and their pulse is measured again for the first 15 seconds\nand then for the last 15 seconds of the first minute of the recovery period.\nImportant! If you feel unwell during the test (dizziness,\ntinnitus, shortness of breath, etc.), stop the test and consult a physician.")
=======
>>>>>>> 12e3ba8d1e7df9adf8de706311c81d694946d099

        vertical = QVBoxLayout()
        horizontal = QHBoxLayout()

        vertical.addWidget(text1)
        horizontal.addWidget(text1, alignment=Qt.AlignLeft)
        vertical.addWidget(text2, alignment=Qt.AlignTop)
        horizontal.addWidget(text2, alignment=Qt.AlignTop)
        horizontal.addWidget(button, alignment=Qt.AlignCenter)
        vertical.addWidget(button, alignment=Qt.AlignCenter)

<<<<<<< HEAD
        self.setLayout(vertical)
        self.setLayout(horizontal)
=======
button = QPushButton('Start')
text1 = QLabel('Welcome to the Health status detection program!')
text2 = QLabel("This application allows you to use the Rufier test to make an initial diagnosis of your health.\nThe Rufier test is a set of physical exercises designed to assess your cardiac performance during physical exertion.\nThe subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds;\nthen, within 45 seconds, the subject performs 30 squats.\nWhen the exercise ends, the subject lies down and their pulse is measured again for the first 15 seconds\nand then for the last 15 seconds of the first minute of the recovery period.\nImportant! If you feel unwell during the test (dizziness,\ntinnitus, shortness of breath, etc.), stop the test and consult a physician.")

vertical = QVBoxLayout() 
horizontal = QHBoxLayout()

vertical.addWidget(text1)
horizontal.addWidget(text1, alignment = Qt.AlignLeft)
vertical.addWidget(text2, alignment = Qt.AlignTop)
horizontal.addWidget(text2, alignment = Qt.AlignTop)
horizontal.addWidget(button, alignment = Qt.AlignCenter)
vertical.addWidget(button, alignment = Qt.AlignCenter)

main_window.setLayout(vertical)
main_window.setLayout(horizontal)

button.clicked.connect(show_winner)
app.exec_()
>>>>>>> 12e3ba8d1e7df9adf8de706311c81d694946d099
