from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget
import sys
from Results import PageThree

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Main Window")
        self.resize(2000, 1000)

        self.stack = QStackedWidget(self)
        self.page3 = PageThree()

        self.stack.addWidget(self.page3)

        layout = QVBoxLayout()
        layout.addWidget(self.stack)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
