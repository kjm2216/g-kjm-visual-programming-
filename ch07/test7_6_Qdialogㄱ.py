import sys
from PySide6.QtWidgets import (QApplication, 
                               QDialog, 
                               QDialogButtonBox, 
                               QLabel, 
                               QVBoxLayout, 
                               QMainWindow, 
                               QPushButton, 
                               QWidget, 
                               QMessageBox)


class CustomDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle('Hello, QDialog')
        
        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.button_box = QDialogButtonBox(buttons)
        
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        
        message = QLabel("Is something ok?")
        
        self.layout = QVBoxLayout()
        
        self.layout.addWidget(message)
        self.layout.addWidget(self.button_box)
        self.setLayout(self.layout)


class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDialog 최종exampl 교수님버전")
        
        l_str = ['Simple QDialog',
                 'Custom Dialog',
                 'QMessageBox.information',
                 'QMessageBox.warning',
                 'QMessageBox.critical',
                 'QMessageBox.about',
                 'QMessageBox.question']
        
        l_slot = [self.slot0,
                  self.slot1,
                  self.slot2,
                  self.slot3,
                  self.slot4,
                  self.slot5,
                  self.slot6]
        
        layout = QVBoxLayout()
        for idx, (i, s) in enumerate(zip(l_str, l_slot)):
            button = QPushButton(i)
            button.clicked.connect(s)
            layout.addWidget(button)
        
        a = QWidget()
        a.setLayout(layout)
        self.setCentralWidget(a)
    
    def slot0(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("QDialog Title")
        dlg.exec()
        
    def slot1(self):
        dlg = CustomDlg(self)
        if dlg.exec():
            print('ok')
        else:
            print("cancel")
            
    def slot2(self):
        QMessageBox.information(
            self,
            'Message',
            'This is an information message'
        )
    
    def slot3(self):
        QMessageBox.warning(
            self,
            'Message',
            'This is an warning message'
        )
        
    def slot4(self):
        QMessageBox.critical(
            self,
            'Message',
            'This is an critical message'
        )
        
    def slot5(self):
        QMessageBox.about(
            self,
            "About This SW",
            """<p>The example of QMessageBox</p> <p>version 0.1</p>"""
        )
        
    def slot6(self):
        ans = QMessageBox.question(
            self,
            "title of question",
            "content of question",
            QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes,
            QMessageBox.StandardButton.Yes,
        )
        print(f'{ans=},{QMessageBox.StandardButton.Yes=}')
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    window.show()
    sys.exit(app.exec())
