import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPlainTextEdit, QMenuBar, QMenu, QLabel, QMessageBox
from PyQt6.QtGui import QAction

class SimpleTextViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Text Viewer")
        self.setGeometry(100, 100, 600, 400)

        # 텍스트 편집 위젯 생성
        self.text_area = QPlainTextEdit(self)
        self.setCentralWidget(self.text_area)

        # 상태 표시줄 생성
        self.status_bar = self.statusBar()

        # 문자 수를 표시할 레이블 생성
        self.character_count_label = QLabel("Characters: 0", self)
        self.status_bar.addPermanentWidget(self.character_count_label)

        # textChanged 시그널을 update_status_bar 슬롯에 연결
        self.text_area.textChanged.connect(self.update_status_bar)

        # 메뉴 바 생성
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        # 파일 메뉴 생성
        file_menu = QMenu("File", self)
        menu_bar.addMenu(file_menu)

        # 액션 생성
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        new_action = QAction("New", self)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        save_as_action = QAction("Save As", self)
        save_as_action.triggered.connect(self.save_as_file)
        file_menu.addAction(save_as_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                    self.text_area.setPlainText(file_content)
            except Exception as e:
                self.show_error_message(f"Could not open file: {e}")

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Text File", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            try:
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(self.text_area.toPlainText())
            except Exception as e:
                self.show_error_message(f"Could not save file: {e}")

    def save_as_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save As Text File", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            try:
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(self.text_area.toPlainText())
            except Exception as e:
                self.show_error_message(f"Could not save file: {e}")

    def new_file(self):
        self.text_area.clear()

    def update_status_bar(self):
        text = self.text_area.toPlainText()
        char_count = len(text)
        self.character_count_label.setText(f"Characters: {char_count}")

    def show_error_message(self, message):
        QMessageBox.critical(self, "Error", message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleTextViewer()
    window.show()
    sys.exit(app.exec())
