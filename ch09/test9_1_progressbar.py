import sys

from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QProgressBar, 
    QPushButton,
    QWidget, QVBoxLayout,
)
from PySide6.QtCore import QTimer

class MW(QMainWindow):

    def __init__(self):
        super(MW, self).__init__()
        self.setWindowTitle("ex: QProgressBar")
        self.setGeometry(200, 200, 300, 150)

        self.progressBar = QProgressBar(self, minimum=2, maximum=20)
        self.progressValue = self.progressBar.minimum()
        #self.progressBar.setGeometry(50, 50, 200, 30)

        self.startButton = QPushButton("start", self)
        #self.startButton.setGeometry(100, 100, 100, 30)
        self.startButton.clicked.connect(self.startProgress)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateProgress)
        #self.progressValue = 0

        lm = QVBoxLayout()
        lm.addWidget(self.progressBar)
        lm.addWidget(self.startButton)

        tmp = QWidget()
        tmp.setLayout(lm)

        self.setCentralWidget(tmp)
        self.show()

    def startProgress(self):
        self.progressBar.reset()
        self.progressValue = self.progressBar.value()
        # self.progressValue = 0
        self.startButton.setEnabled(False)
        self.timer.start(100)  
        
    def updateProgress(self):
        self.progressValue += 1
        self.progressBar.setValue(self.progressValue)
        
        if self.progressValue >= self.progressBar.maximum():
            self.timer.stop()
            self.progressBar.reset()
            self.startButton.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec())