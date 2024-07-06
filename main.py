from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget
import sys
from instuctions import PageOne
from testscreen import PageTwo
from Results import PageThree
from PyQt5.QtGui import QPalette, QBrush, QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_background_image("./images/background2.png")
    def set_background_image(self, image_path):
        oImage = QPixmap(image_path)
        sImage = oImage.scaled(self.size())  # Scaled to window size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def initUI(self):
        self.setWindowTitle("Main Window")
        self.resize(2000, 1000)

        self.stack = QStackedWidget(self)
        self.page1 = PageOne(self.go_to_page2)
        self.page2 = PageTwo(self.go_to_page3)
        self.page3 = PageThree()

        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)
        self.stack.addWidget(self.page3)

        layout = QVBoxLayout()
        layout.addWidget(self.stack)

        self.setLayout(layout)
    
    def go_to_page2(self):
        self.stack.setCurrentWidget(self.page2)
        
    def go_to_page3(self):
        self.stack.setCurrentWidget(self.page3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
