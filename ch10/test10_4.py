import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QTextEdit, QStatusBar, QToolBar
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Qt

class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.fpath = os.path.dirname(os.path.abspath(__file__))
        self.setFixedSize(600, 600)
        self.setWindowTitle("ds status bar Ex")
        self.setup_main_wnd()
        self.create_tool_bar()
        self.create_menu()
        self.setStatusBar(QStatusBar())  # 최초 호출시 status bar 추가됨.
        self.show()

    def setup_main_wnd(self):
        self.label = QLabel("QStatusBar Example")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)

    def create_tool_bar(self):
        tool_bar = QToolBar("QToolBar for QStatusBar Ex")
        tool_bar.setIconSize(QSize(30, 30))

        open_btn = QPushButton(QIcon(f"{self.fpath}/img/open_file.png"), "Open", self)
        open_btn.setShortcut("Ctrl+O")
        open_btn.clicked.connect(self.open_event)
        tool_bar.addWidget(open_btn)

        close_btn = QPushButton(QIcon(f"{self.fpath}/img/clear.png"), "Close", self)
        close_btn.setShortcut("Ctrl+X")
        close_btn.clicked.connect(self.close)
        tool_bar.addWidget(close_btn)

        self.addToolBar(tool_bar)

    def create_menu(self):
        mb = self.menuBar()
        mb.setNativeMenuBar(False)

        file_menu = mb.addMenu("File")

        open_act = file_menu.addAction("Open")
        open_act.setShortcut("Ctrl+O")
        open_act.triggered.connect(self.open_event)

        close_act = file_menu.addAction("Close")
        close_act.setShortcut("Ctrl+X")
        close_act.triggered.connect(self.close)

    def open_event(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Text files (*.txt)")
        file_dialog.setViewMode(QFileDialog.ViewMode.List)

        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.label.setText(content)
                self.statusBar().showMessage("파일을 열었습니다.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())

