import sys,os
from PySide6.QtWidgets import ( QMainWindow, QApplication ) 

from test11_1 import Ui_MainWindow 

class MW(QMainWindow, Ui_MainWindow): 
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.lineEdit.returnPressed.connect(self.update_label)
        
        self.show()
        
    def update_label(self):
        c_text = self.lineEdit.text()
        self.label.setText(c_text)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mwd = MW()
    sys.exit(app.exec())
    
