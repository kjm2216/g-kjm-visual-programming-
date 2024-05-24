import sys
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class WorkerThread(QThread):
    update_signal = pyqtSignal(int)

    def run(self):
        for i in range(1, 11):
            self.sleep(1)  # 1초 동안 스레드를 일시 중지
            self.update_signal.emit(i)

class ExampleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QThread Example')
        layout = QVBoxLayout()

        self.label = QLabel("Waiting for thread to finish...")
        layout.addWidget(self.label)

        self.start_button = QPushButton('Start Thread')
        self.start_button.clicked.connect(self.startThread)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton('Stop Thread')
        self.stop_button.clicked.connect(self.stopThread)
        layout.addWidget(self.stop_button)

        self.close_button = QPushButton('Close Window')
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)

        self.setLayout(layout)

        self.thread = WorkerThread()
        self.thread.update_signal.connect(self.updateLabel)

    def startThread(self):
        self.label.setText("Thread is running...")
        self.thread.start()

    def stopThread(self):
        if self.thread.isRunning():
            self.thread.terminate()

    def updateLabel(self, iteration):
        self.label.setText("Iteration: {}".format(iteration))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExampleApp()
    ex.show()
    sys.exit(app.exec())
