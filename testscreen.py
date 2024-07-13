import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont

class PageTwo(QWidget):
    def __init__(self, on_start_clicked):
        super().__init__()
        self.on_start_clicked = on_start_clicked
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Test Screen")
        self.setGeometry(200, 50, 1500, 1000)

        self.layout = QVBoxLayout(self)

        self.name = QLineEdit('Name?')

        self.input_1 = QLineEdit('1')
        self.input_2 = QLineEdit('2')
        self.input_3 = QLineEdit('3')
        #self.input_4 = QLineEdit('4')

        self.age = QLineEdit('5')

        self.name.setAlignment(Qt.AlignCenter)

        self.text_1.setAlignment(Qt.AlignCenter)
        self.text_2.setAlignment(Qt.AlignCenter)
        self.text_3.setAlignment(Qt.AlignCenter)

        self.text_1.setFont(QFont('Comic Sans MS', 10))
        self.text_2.setFont(QFont('Comic Sans MS', 10))
        self.text_3.setFont(QFont('Comic Sans MS', 10))

        self.input_1.setAlignment(Qt.AlignCenter)
        self.input_2.setAlignment(Qt.AlignCenter)
        self.input_3.setAlignment(Qt.AlignCenter)

        self.age.setAlignment(Qt.AlignCenter)

        self.timer1_time = 15
        self.timer2_time = 45
        self.timer3_time = 60

        self.timer1_label = QLabel("Timer 1: 15 seconds", self)
        self.timer2_label = QLabel("Timer 2: 45 seconds", self)
        self.timer3_label = QLabel("Timer 3: 60 seconds", self)

        self.timer1_label.setAlignment(Qt.AlignCenter)
        self.timer2_label.setAlignment(Qt.AlignCenter)
        self.timer3_label.setAlignment(Qt.AlignCenter)

        self.start_button1 = QPushButton("Start test 1", self)
        self.start_button2 = QPushButton("Start test 2", self)
        self.start_button3 = QPushButton("Start test 3", self)

        self.start_button1.clicked.connect(self.start_timer1)
        self.start_button2.clicked.connect(self.start_timer2)
        self.start_button3.clicked.connect(self.start_timer3)

        self.layout.addWidget(text_1)
        self.layout.addWidget(self.timer1_label)
        self.layout.addWidget(self.start_button1)
        self.layout.addWidget(self.input_1)

        self.layout.addWidget(text_2)
        self.layout.addWidget(self.timer2_label)
        self.layout.addWidget(self.start_button2)
        self.layout.addWidget(self.input_2)

        self.layout.addWidget(text_3)
        self.layout.addWidget(self.timer3_label)
        self.layout.addWidget(self.start_button3)
        self.layout.addWidget(self.input_3)

        self.layout.addWidget(self.age)

        self.timer1 = QTimer(self)
        self.timer2 = QTimer(self)
        self.timer3 = QTimer(self)

        self.timer1.timeout.connect(self.update_timer1)
        self.timer2.timeout.connect(self.update_timer2)
        self.timer3.timeout.connect(self.update_timer3)
        
        button = QPushButton('Send results')
        button.clicked.connect(self.clicked_move)
        self.layout.addWidget(button)
        
    def clicked_move(self):
        self.pulse1 = int(self.input_1.text())
        self.pulse2 = int(self.input_2.text())
        self.pulse3 = int(self.input_3.text())
        self.on_start_clicked(self.pulse1, self.pulse2, self.pulse3)

    def start_timer1(self):
        self.timer1.start(1000)  

    def start_timer2(self):
        self.timer2.start(1000) 

    def start_timer3(self):
        self.timer3.start(1000) 

    def update_timer1(self):
        self.timer1_time -= 1
        self.timer1_label.setText(f"Timer 1: {self.timer1_time} seconds")
        if self.timer1_time <= 0:
            self.timer1.stop()
            self.timer1_label.setText("Timer 1: Time's up!")
            self.timer1_time = 15

    def update_timer2(self):
        self.timer2_time -= 1
        self.timer2_label.setText(f"Timer 2: {self.timer2_time} seconds")
        if self.timer2_time <= 0:
            self.timer2.stop()
            self.timer2_label.setText("Timer 2: Time's up!")
            self.timer2_time = 45

    def update_timer3(self):
        self.timer3_time -= 1
        self.timer3_label.setText(f"Timer 3: {self.timer3_time} seconds")
        if self.timer3_time <= 0:
            self.timer3.stop()
            self.timer3_label.setText("Timer 3: Time's up!")
            self.timer3_time = 60

def main():
    app = QApplication(sys.argv)

    def on_start_clicked():
        print("Start button clicked!")

    page_two = PageTwo(on_start_clicked)
    page_two.show()

    sys.exit(app.exec_())
