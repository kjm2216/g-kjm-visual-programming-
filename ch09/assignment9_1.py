import sys  
import os 
from PySide6.QtWidgets import ( QWidget, QApplication, QLabel )

class MW(QWidget):  
    def __init__(self): 
        super().__init__() 

        self.setGeometry(200, 100, 400, 200)
        self.setWindowTitle("script_dir")

        # "Hello, World" 레이블 생성 및 설정
        hello_label = QLabel(self)
        hello_label.setText('Hello, World')
        hello_label.move(150, 90)

        # 현재 스크립트 파일의 디렉토리 경로를 가져옴
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # 디렉토리 경로를 표시할 레이블 생성 및 설정
        dir_label = QLabel(self)
        dir_label.setText(f'현재 스크립트의 디렉토리 경로: {script_dir}')
        dir_label.move(100, 120)

        self.show()

if __name__ == "__main__":  # 스크립트가 직접 실행될 때만 아래 코드 실행
    app = QApplication(sys.argv)  # PyQt6 애플리케이션 객체 생성
    window = MW()  # MW 클래스의 인스턴스 생성
    sys.exit(app.exec())  # 애플리케이션의 이벤트 루프 실행 및 프로그램 종료

