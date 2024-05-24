import sys 
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent

class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Event Handling Ex2")
        
        label = QLabel("""<p>Press the <b>A</b> key
                    to open a sub window.</p>""")
        self.setCentralWidget(label)
        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Escape:
            print("ESC key pressed!")
            self.close()
            
        if event.key() == Qt.Key.Key_A:
            self.A = SMW()
            self.A.show()

class SMW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Sub Window")
        self.setGeometry(200, 200, 300, 200)
        
        label = QLabel("Press Q to close this window")
        
        self.setCentralWidget(label)
        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Q:
            self.close()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MW()
    window.show()
    sys.exit(app.exec())
            