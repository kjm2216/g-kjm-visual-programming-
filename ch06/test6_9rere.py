import sys

from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QWidget,
    QVBoxLayout,)
from PySide6.QtCore import Qt

class MW (QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setGeometry(100,100, 400, 400)
        self.setWindowTitle('Event Handling Ex.')
        
        self.set_main_wnd()
        self.sub_wnd = ChildWindow()
        self.show()
    
    def set_main_wnd(self):
        label = QLabel(
            """<p>Press the <b>ESC</b> key
            to quit this program.</p>"""
        )
        self.setCentralWidget(label)
        
    def keyPressEvent(self, event: QKeyEvent) -> None:        
        # super().keyPressEvent(event)
        if event.key() == Qt.Key.Key_Escape:
            print('ESC Key Pressed!')
            if self.a is not None:
                self.a.close()
            self.close()
        elif event.key() == Qt.Key.Key_A:
            self.sub_wnd.show()            

class ChildWindow(QWidget):    
    def __init__ (self):
        super().__init__()
        label = QLabel("I am Child!")
        lm = QVBoxLayout()
        lm.addWidget(label)
        self.setLayout(lm)
        # self.show() # sub window이므로, show를 필요할 때 명시적으로 호출할 예정임.
        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Q:
            self.hide()
        return super().keyPressEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mwd = MW()
    sys.exit(app.exec())