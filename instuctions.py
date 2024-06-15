from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QRadioButton

one =("This application allows you to use the Rufier test to make an initial diagnosis of your health.")
two = ("The Rufier test is a set of physical exercises designed to assess your cardiac performance during physical exertion.") 
three = ("The subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds;")
four = ("then, within 45 seconds, the subject performs 30 squats.")
five = ("When the exercise ends, the subject lies down and their pulse is measured again for the first 15 seconds")
six = ("and then for the last 15 seconds of the first minute of the recovery period.")
seven = ("Important! If you feel unwell during the test (dizziness,")
eight = ("tinnitus, shortness of breath, etc.), stop the test and consult a physician.")



app = QApplication([])
main_window = QWidget()
main_window.show()

main_window.setWindowTitle("Health")
main_window.resize(1280, 720)
main_window.move(0,0)

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

app.exec_()