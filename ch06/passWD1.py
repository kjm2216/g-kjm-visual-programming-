import sys

from PySide6.QtWidgets import (QApplication, QWidget, 
                             QVBoxLayout, QLineEdit, QPushButton)
from PySide6.QtCore import Qt

class PMW(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('비밀번호 입력')
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("비밀번호를 입력하세요")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)  # 입력시 *로 표시되도록 설정
        self.password_input.setMaxLength(10)
        self.password_input.textChanged.connect(self.checkPassword)

        self.submit_button = QPushButton('ㄱㄱ', self)
        self.submit_button.setEnabled(False)
        self.submit_button.clicked.connect(self.submitPassword)
        self.password_input.returnPressed.connect(self.submitPassword)

        layout.addWidget(self.password_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def checkPassword(self, text):   # 비밀번호가 숫자와 문자로만 이루어져 있는지 확인
        if not text.isalnum():
            self.submit_button.setEnabled(False)   # 버튼 비활성화
        else:
            self.submit_button.setEnabled(True)

    def submitPassword(self):
        password = self.password_input.text()
        print("입력한 비밀번호:", password)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PMW()
    window.show()
    sys.exit(app.exec())
