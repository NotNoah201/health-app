#this is for me and jake. test screen.
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# Step 1: Create a subclass of QMainWindow to set up the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("PyQt5 Basic Window")
        self.setGeometry(100, 100, 800, 600)  # (x, y, width, height)

# Step 2: Initialize the QApplication
app = QApplication(sys.argv)

# Step 3: Create an instance of the MainWindow
window = MainWindow()
window.show()  # Display the window

# Step 4: Start the event loop
sys.exit(app.exec_())

