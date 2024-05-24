import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PySide6.QtCore import Qt

class IDPWEntry(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('회원가입')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # 아이디 입력 창
        self.id_input = QLineEdit(self)
        self.id_input.setPlaceholderText("아이디를 입력하세요")
        self.id_input.setMaxLength(10)  # 최대 10글자까지 입력 가능
        layout.addWidget(self.id_input)

        # 비밀번호 입력 창
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("비밀번호를 입력하세요")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)  # 입력시 *로 표시
        self.password_input.setMaxLength(10)  # 최대 10글자까지 입력 가능
        layout.addWidget(self.password_input)

        # 처리 버튼
        self.submit_button = QPushButton('가입하기', self)
        self.submit_button.setEnabled(False)
        self.submit_button.clicked.connect(self.submitInfo)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

        # 입력이 유효한지 확인하는 시그널 연결
        self.id_input.textChanged.connect(self.checkInfo)
        self.password_input.textChanged.connect(self.checkInfo)

    def checkInfo(self):
        # 아이디와 비밀번호가 모두 알파벳 문자와 숫자로만 이루어져 있는지 확인
        if self.id_input.text().isalnum() and self.password_input.text().isalnum():
            self.submit_button.setEnabled(True)
        else:
            self.submit_button.setEnabled(False)

    def submitInfo(self):
        id_text = self.id_input.text()
        pw_text = self.password_input.text()
        print("입력한 아이디:", id_text)
        print("입력한 비밀번호:", pw_text)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IDPWEntry()
    window.show()
    sys.exit(app.exec())
