import sys 
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QListWidget,
    QVBoxLayout, QWidget, QFileDialog, QMenuBar,
    QStatusBar
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Directory to QListWidget Example")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)
        
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        menubar.setNativeMenuBar(False)
        
        open_action = QAction("Open Directory", self)
        open_action.triggered.connect(self.open_directory)
        file_menu.addAction(open_action)


        self.list_widget.itemClicked.connect(self.show_file_path)

        self.dir_path = None  # 선택된 디렉토리 경로 저장 변수
        self.show()  # 윈도우 표시

    def open_directory(self):
        # 디렉토리 선택 다이얼로그 열기
        self.dir_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if self.dir_path:
            self.list_widget.clear()  # 기존 리스트 항목 제거
            # 디렉토리의 txt 파일 목록 가져오기
            txt_files = [os.path.basename(f) 
                         for f in os.listdir(self.dir_path) 
                         if f.endswith('.txt')]

            for txt_file in txt_files:
                self.list_widget.addItem(txt_file)  # QListWidget에 txt 파일 추가

    def show_file_path(self, item):
        # 선택된 아이템의 파일 경로를 상태바에 출력
        f_path = os.path.join(self.dir_path, item.text())
        self.status_bar.showMessage(f_path)  # 상태바에 파일 경로 표시

if __name__ == "__main__":
    app = QApplication(sys.argv)  
    mwd = MainWindow()  
    sys.exit(app.exec()) 