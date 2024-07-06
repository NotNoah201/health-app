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

        text1 = QLabel('RESULTS:', self)
        text1.setAlignment(Qt.AlignCenter)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(text1, alignment=Qt.AlignCenter)

        self.setLayout(vertical_layout)

p1 = 50
p2 = 50
p3 = 50
age = 30

def evaluate_expression(p1, p2, p3):
    return (4 * (p1 + p2 + p3) - 200) / 10

ScoreInterpret = {(15,100): {(15,100): "Low",
                             (11,14.9): "Satisfactory",
                             (6,10.9): "Average",
                             (0.5,5.9): "Above average",
                             (0,0.4): "High"},
                    (13,14) : {(16.5,100): "Low",
                               (12.5,16.4): "satisfactory",
                               (7.5,12.4): "Average",
                               (2,7.4): "Above Average",
                               (0,1.9): "High"},
                    (11,12) : {(18,100): "Low",
                               (14,17.9): "satisfactory",
                               (9,13.9): "Average",
                               (3.5,8.9): "Above Average",
                               (0,3.4): "High"},
                    (9,10) : {(19.5,100): "Low",
                               (15.5,19.4): "satisfactory",
                               (10.5,15.4): "Average",
                               (5,10.4): "Above Average",
                               (0,4.9): "High"},
                     (7,8) : {(21,100): "Low",
                               (17,20.9): "satisfactory",
                               (12,16.9): "Average",
                               (6.5,11.9): "Above Average",
                               (0,6.4): "High"},
                             }

def get(AGE, RuffierScore):
    for ageRange in ScoreInterpret.key():
        if ageRange[0]<AGE<ageRange[1]:
            for RuffierRange in ScoreInterpret[ageRange].key():
                if RuffierRange[0]<RuffierScore<RuffierRange[1]:
                    return ScoreInterpret[ageRange][RuffierRange]
