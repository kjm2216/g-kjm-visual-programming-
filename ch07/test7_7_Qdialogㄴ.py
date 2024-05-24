import sys
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QVBoxLayout,
    QMainWindow,
    QPushButton,
    QMessageBox,
    QWidget
)

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
        self.setWindowTitle("QDialog Ex 내버전.")


        self.info_button = QPushButton("Information")
        self.about_button = QPushButton("About")
        self.question_button = QPushButton("Question")
        self.critical_button = QPushButton("Critical")
        self.warning_button = QPushButton("Warning")
        self.Simple_button = QPushButton("QDialog")
        self.Custom_button = QPushButton("CutomDlg")


        self.info_button.clicked.connect(self.slot0)
        self.about_button.clicked.connect(self.slot1)
        self.question_button.clicked.connect(self.slot2)
        self.critical_button.clicked.connect(self.slot3)
        self.warning_button.clicked.connect(self.slot4)
        self.Simple_button.clicked.connect(self.slot5)
        self.Custom_button.clicked.connect(self.slot6)
        

 
        layout = QVBoxLayout()
        layout.addWidget(self.info_button)
        layout.addWidget(self.about_button)
        layout.addWidget(self.question_button)
        layout.addWidget(self.critical_button)
        layout.addWidget(self.warning_button)
        layout.addWidget(self.Simple_button)
        layout.addWidget(self.Custom_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def slot0(self):
        result = QMessageBox.information(       # waring, information, critical
            self,                    # parent
            "info title",            # 제목
            "info content",          # 보여줄 메시지.
            QMessageBox.StandardButton.Ok |QMessageBox.StandardButton.Cancel # 버튼들.
        )
        print(f'QMessageBox.information :{result}')

    def slot1(self):
        QMessageBox.about(
             self,              # parent
             "About This SW",   # title of about dialog.
             """<p>The example of QMessageBox</p>
             <p>version 0.1</p>"""
        )

    def slot2(self):
        ans = QMessageBox.question(
          self,                 # parent
          "title of question",  # 질문 제목
          "cotent of question", # 질문 내용.
          QMessageBox.StandardButton.No | \
          QMessageBox.StandardButton.Yes, # responses
          QMessageBox.StandardButton.Yes, # default response
        )
        print(f'{ans=},{QMessageBox.StandardButton.Yes}')

    def slot3(self):
        result = QMessageBox.critical(       # waring, information, critical
            self,                    # parent
            "info title",            # 제목
            "info content",          # 보여줄 메시지.
            QMessageBox.StandardButton.Ok |QMessageBox.StandardButton.Cancel # 버튼들.
        )
        print(f'QMessageBox.information :{result}')

    def slot4(self):
        result = QMessageBox.warning(       # waring, information, critical
            self,                    # parent
            "info title",            # 제목
            "info content",          # 보여줄 메시지.
            QMessageBox.StandardButton.Ok |QMessageBox.StandardButton.Cancel # 버튼들.
        )
        print(f'QMessageBox.information :{result}')
        
    def slot5(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("QDialog Title")
        dlg.exec()
        
    def slot6(self):
        dlg = CustomDlg(self)
        if dlg.exec():
            print('ok')
        else:
            print("cancel")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    window.show()
    app.exec()
