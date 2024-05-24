import sys

from PyQt6.QtWidgets import (QApplication, QWidget,
                             QLabel,
                             QVBoxLayout,
                             QRadioButton, QButtonGroup)
from PyQt6.QtCore import Qt

class MW (QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Ex: QRadioButton")
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        lm = QVBoxLayout()

        lm.addWidget(QLabel('What is most important?'))

        self.bg = QButtonGroup(self)        
        self.rb01 = QRadioButton('1. faith')
        lm.addWidget(self.rb01)
        self.bg.addButton(self.rb01)
        self.rb02 = QRadioButton('2. hope')
        lm.addWidget(self.rb02)
        self.bg.addButton(self.rb02)
        self.rb03 = QRadioButton('3. love')
        lm.addWidget(self.rb03)        
        self.bg.addButton(self.rb03)

        self.bg.buttonClicked.connect(self.ck_click)

        self.dp_label = QLabel("")
        lm.addWidget(self.dp_label)

        self.setLayout(lm)

    def ck_click(self, button):
        tmp = ""
        tmp = button.text()        
        print(tmp)
        self.dp_label.setText(tmp)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_wnd = MW()
    sys.exit(app.exec())
