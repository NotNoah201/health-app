import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QApplication, QGraphicsDropShadowEffect
from PyQt5.QtGui import QMovie, QFont, QIcon

class GifPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GIF Player")
        self.setGeometry(100, 100, 800, 600)
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        gif_path = "./images/icons8-pulse.gif"
        self.movie = QMovie(gif_path)
        self.label.setMovie(self.movie)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.movie.start()
        
class PageOne(QWidget):
    def __init__(self, on_start_clicked):
        super().__init__()
        self.on_start_clicked = on_start_clicked
        self.initUI()
        gif_player = GifPlayer()
        self.setWindowIcon(QIcon('./icon.png'))
        self.show()
        

    def initUI(self):
        self.setWindowTitle("Health")
        self.resize(1280, 720)
        self.move(0, 0)

        button = QPushButton('Start')
        button.clicked.connect(self.on_start_clicked)
        
        text1 = QLabel('Welcome to the Health status detection program!')
        text1.setFont(QFont('Alore', 20))  
        text1.setAlignment(Qt.AlignCenter)
        text2 = QLabel("This application allows you to use the Rufier test to make an initial diagnosis of your health.\n")
        text3 = QLabel("The Rufier test is a set of physical exercises designed to assess your cardiac performance during physical exertion.\n"
                        "The subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds;\n"
                        "then, within 45 seconds, the subject performs 30 squats.\n"
                        "When the exercise ends, the subject lies down and their pulse is measured again for the first 15 seconds\n"
                        "and then for the last 15 seconds of the first minute of the recovery period.\n"
                        "Important! If you feel unwell during the test (dizziness, tinnitus, shortness of breath, etc.), stop the test and consult a physician.")
        text3.setFont(QFont('Aria', 10))  
        shadow = QGraphicsDropShadowEffect() 
        shadow.setBlurRadius(15) 
        text1.setGraphicsEffect(shadow) 

        self.gif_label = QLabel(self)
        self.gif_label.setAlignment(Qt.AlignRight | Qt.AlignTop)


        self.movie = QMovie("images\icons8-pulse.gif")
        

        self.gif_label.setMovie(self.movie)
        self.movie.start()
        gif_player = GifPlayer()
        gif_player.show()
        vertical = QVBoxLayout()
        horizontal = QHBoxLayout()

        vertical.addWidget(text1, alignment =Qt.AlignCenter)
        vertical.addWidget(text2, alignment =Qt.AlignCenter)
        vertical.addWidget(text3, alignment =Qt.AlignCenter)
        vertical.addWidget(button, alignment =Qt.AlignCenter)


        top_layout = QHBoxLayout()
        top_layout.addWidget(self.gif_label, alignment=Qt.AlignRight)

        vertical.insertLayout(0, top_layout)  # Insert at the top

        self.setLayout(vertical)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    def start_clicked():
        gif_player = GifPlayer()
        gif_player.show()

    page_one = PageOne(on_start_clicked=start_clicked)
    page_one.show()

    sys.exit(app.exec_())
