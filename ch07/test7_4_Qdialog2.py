import sys
from PySide6.QtWidgets import ( QApplication,
    QDialog,
    QDialogButtonBox, 
    QLabel, 
    QVBoxLayout,
    QMainWindow,
    QPushButton
)

class CustomDlg(QDialog): 
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Hello, QDialog')

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.button_box = QDialogButtonBox(buttons) # buttons에 해당하는 button객체

        self.button_box.accepted.connect(self.accept) #QDialog의 메서드를 slot으로
        self.button_box.rejected.connect(self.reject)    #QDialog의 메서드를 slot으로

        message = QLabel('Is something ok?')

        self.layout = QVBoxLayout()
        self.layout.addWidget(message)
        self.layout.addWidget(self.button_box) # QDialogButtonBox객체 추가.
        self.setLayout(self.layout)


class MW(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDialog Ex.")

        button = QPushButton("Press it for a Dialog")
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)
        
        # #dlg = QDialog(self) 
        # dlg = QDialog() 
        # dlg.setWindowTitle("QDialog Title") 
        # dlg.exec()  #중요!
        
        # -------------
        # for custom dlg
        dlg = CustomDlg(self)
        if dlg.exec(): # Modal Dialog
            print('ok')
        else:
            print("cancel")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    window.show()
    app.exec()
