import sys
from PySide6.QtWidgets import QDialog, QPushButton, QApplication, QLabel, QDialogButtonBox, QVBoxLayout

class CustomDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Hello, QDialog")
        
        buttons = QDialogButtonBox.Ok
        self.button_box = QDialogButtonBox(buttons)
        
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        
        message = QLabel("Is something ok?")
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(message)
        self.layout.addWidget(self.button_box)
        self.setLayout(self.layout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = CustomDlg()
    dlg.exec()
    sys.exit(app.exec())


        
    