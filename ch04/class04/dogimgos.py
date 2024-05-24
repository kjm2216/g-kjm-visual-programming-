from PySide6.QtWidgets import (QWidget, QLabel, QApplication)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt
import os

import sys

class main_wnd (QWidget):
    def __init__(self):
        super().__init__()
        # Main wnd 크기 등을 설정
        self.setGeometry(100,200,600,600)
        # self.setFixedSize(600,300)
        
        self.ds_set_mw()
        self.show()
        
        #Main wnd에 포함되는 Widgets을 생성 및 추가
        label0 = QLabel("Hello, World!",self)
        label0.move(30,30)
        
        self.show()
        
    def ds_set_mw(self):
        label0 = QLabel("Hello, World!",self)
        label0.setFont(QFont('Arial,20'))
        label0.setStyleSheet('background-color: red')
        label0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label0.move(30,30)
        
        self.ds_set_label1()
        
    def ds_set_label1(self):
        label1 = QLabel(self)
        
        fstr = os.path.realpath(__file__)
        pstr = os.path.dirname(fstr)
        istr = os.path.join(pstr,"C:/visual programming/img/ggg.jpg.jpg")
        
        #pixmap = QPixmap("C:/visual programming/img/ggg.png")
        
        pixmap = QPixmap(istr)
        pixmap.scaled(200,200,Qt.AspectRatioMode.KeepAspectRatio)
        label1.setPixmap(pixmap)
        label1.setScaledContents(True)
        
        #label1.setPixmap(QPixmap('./imf/ggg.png'))
        
        label1.move(30,80)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 내가 만든 Qt 관련 main window 인스턴스를 만들어져야한다
    mw = main_wnd()
    sys.exit(app.exec())