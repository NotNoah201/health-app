from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget
import sys
from instuctions import PageOne

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Main Window")
        self.resize(1280, 720)

        self.stack = QStackedWidget(self)
        self.page1 = PageOne(self.go_to_page2)
        # self.page2 = PageTwo()

        self.stack.addWidget(self.page1)
        # self.stack.addWidget(self.page2)

        layout = QVBoxLayout()
        layout.addWidget(self.stack)

        self.setLayout(layout)
    
    def go_to_page2(self):
        # self.stack.setCurrentWidget(self.page2)
        print("This would switch to Page 2")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
