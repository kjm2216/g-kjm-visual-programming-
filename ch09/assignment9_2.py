import sys
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import ( QApplication, QMainWindow, QVBoxLayout, 
                                QLabel, QLineEdit, QPushButton,
                                QDialog, QDialogButtonBox, QWidget )

class MainWindow(QMainWindow):
    my_signal = Signal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Enter Key 입력")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.info_label = QLabel("Enter를 누르세요")
        layout.addWidget(self.info_label)

        self.button = QPushButton("Enter")
        self.button.clicked.connect(self.emit_signal)
        layout.addWidget(self.button)

        self.setLayout(layout)

    # 키 이벤트가 발생했을 때 호출되는 함수
    def keyPressEvent(self, event):
        # 만약 Enter 키가 눌렸다면 커스텀 시그널을 발생
        if event.key() == Qt.Key_Return:
            self.my_signal.emit()

    # 버튼 클릭 이벤트에 대한 핸들러 함수
    def emit_signal(self):
        # 커스텀 시그널을 발생
        self.my_signal.emit()

class MyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Enter Key 입력")
        layout = QVBoxLayout()
        self.label = QLabel("정수 값을 입력하세요:")
        self.input_lineedit = QLineEdit()
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        layout.addWidget(self.label)
        layout.addWidget(self.input_lineedit)
        layout.addWidget(self.button_box)
        self.setLayout(layout)

    def get_integer_value(self):
        if self.exec() == QDialog.Accepted:
            return int(self.input_lineedit.text())
        else:
            return None

# 모달 다이얼로그를 보여주는 함수
def show_dialog():
    dialog = MyDialog()
    integer_value = dialog.get_integer_value()
    if integer_value is not None:
        # 유효한 정수 값이 입력된 경우 콘솔에 출력
        print("입력된 정수 값:", integer_value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.my_signal.connect(show_dialog)
    window.show()
    sys.exit(app.exec())
