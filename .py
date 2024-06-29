import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QTimer, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Three 15-Second Timers with Background Image")
        self.setGeometry(100, 100, 800, 600)

        # Set up the central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a QHBoxLayout for the main layout
        self.main_layout = QHBoxLayout(self.central_widget)

        # Create a QVBoxLayout for the timers on the left
        self.timer_layout = QVBoxLayout()
        
        # Create a QLabel to display the background image
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 800, 600)
        
        # Load the image using QPixmap
        self.pixmap = QPixmap("background.jpg")
        
        # Scale the image to fit the window
        self.pixmap = self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        
        # Set the QPixmap as the QLabel's background
        self.background_label.setPixmap(self.pixmap)
        
        # Ensure the label is behind all other widgets
        self.background_label.lower()

        # Define the font size
        font = QFont()
        font.setPointSize(16)

        # Timer variables
        self.timer1_time = 15
        self.timer2_time = 15
        self.timer3_time = 15

        # Create labels for timers
        self.timer1_label = QLabel("Timer 1: 15 seconds", self)
        self.timer2_label = QLabel("Timer 2: 15 seconds", self)
        self.timer3_label = QLabel("Timer 3: 15 seconds", self)

        # Apply the font to the labels
        self.timer1_label.setFont(font)
        self.timer2_label.setFont(font)
        self.timer3_label.setFont(font)

        # Create buttons to start timers
        self.start_button1 = QPushButton("Start Timer 1", self)
        self.start_button2 = QPushButton("Start Timer 2", self)
        self.start_button3 = QPushButton("Start Timer 3", self)

        # Apply the font to the buttons
        self.start_button1.setFont(font)
        self.start_button2.setFont(font)
        self.start_button3.setFont(font)

        # Connect buttons to their respective slots
        self.start_button1.clicked.connect(self.start_timer1)
        self.start_button2.clicked.connect(self.start_timer2)
        self.start_button3.clicked.connect(self.start_timer3)

        # Add widgets to the timer layout
        self.timer_layout.addWidget(self.timer1_label)
        self.timer_layout.addWidget(self.start_button1)
        self.timer_layout.addWidget(self.timer2_label)
        self.timer_layout.addWidget(self.start_button2)
        self.timer_layout.addWidget(self.timer3_label)
        self.timer_layout.addWidget(self.start_button3)

        # Add the timer layout to the main layout
        self.main_layout.addLayout(self.timer_layout)

        # Create QTimer objects for each timer
        self.timer1 = QTimer(self)
        self.timer2 = QTimer(self)
        self.timer3 = QTimer(self)

        # Connect timers to their respective slots
        self.timer1.timeout.connect(self.update_timer1)
        self.timer2.timeout.connect(self.update_timer2)
        self.timer3.timeout.connect(self.update_timer3)

    def start_timer1(self):
        self.timer1.start(1000)  # 1 second interval

    def start_timer2(self):
        self.timer2.start(1000)  # 1 second interval

    def start_timer3(self):
        self.timer3.start(1000)  # 1 second interval

    def update_timer1(self):
        self.timer1_time -= 1
        self.timer1_label.setText(f"Timer 1: {self.timer1_time} seconds")
        if self.timer1_time <= 0:
            self.timer1.stop()
            self.timer1_label.setText("Timer 1: Time's up!")
            self.timer1_time = 15  # Reset timer

    def update_timer2(self):
        self.timer2_time -= 1
        self.timer2_label.setText(f"Timer 2: {self.timer2_time} seconds")
        if self.timer2_time <= 0:
            self.timer2.stop()
            self.timer2_label.setText("Timer 2: Time's up!")
            self.timer2_time = 15  # Reset timer

    def update_timer3(self):
        self.timer3_time -= 1
        self.timer3_label.setText(f"Timer 3: {self.timer3_time} seconds")
        if self.timer3_time <= 0:
            self.timer3.stop()
            self.timer3_label.setText("Timer 3: Time's up!")
            self.timer3_time = 15  # Reset timer

    def resizeEvent(self, event):
        # Scale the image to fit the window whenever the window is resized
        self.pixmap = self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.background_label.setPixmap(self.pixmap)
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

