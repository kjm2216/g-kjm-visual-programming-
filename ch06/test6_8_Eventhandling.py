import sys
from PySide6.QtWidgets import (QApplication, 
                                         QMainWindow, QLabel)
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent

class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Event Handling Ex")
        
        self.set_main_wnd()
        self.show()
        
    def set_main_wnd(self):
        label = QLabel(
            """<p>Press the <b>ESC</b> key
            to quit this program.</p>""" 
        )
        
        self.setCentralWidget(label)
        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Escape:
            print("ESC key pressed!")
            self.close()
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec())
