import sys

from PyQt6.QtWidgets import (QApplication, QWidget,
                             QLabel,
                             QVBoxLayout,
                             QCheckBox,QButtonGroup)
from PyQt6.QtCore import Qt

class MW (QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Ex: QCheckbox")
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        lm = QVBoxLayout()

        lm.addWidget(QLabel('What is most important?'))

        self.bg = QButtonGroup(self)

        self.cb01 = QCheckBox('1. faith')
        lm.addWidget(self.cb01)
        self.bg.addButton(self.cb01)
        self.cb02 = QCheckBox('2. hope')
        lm.addWidget(self.cb02)
        self.bg.addButton(self.cb02)
        self.cb03 = QCheckBox('3. love')
        lm.addWidget(self.cb03)
        self.bg.addButton(self.cb03)

        self.bg.setExclusive(True)
        self.bg.buttonClicked.connect(self.ck_click)

        self.dp_label = QLabel("")
        lm.addWidget(self.dp_label)

        self.cb = QCheckBox('Check it for the multiple selection.')
        self.cb.setChecked(not self.bg.exclusive())
        self.cb.toggled.connect(self.ck_multiple)
        lm.addWidget(self.cb)

        self.setLayout(lm)

    def ck_click(self, button):
        tmp = ""
        tmp = button.text()
        # print(type(button))
        # print(tmp)
        self.dp_label.setText(tmp)

    def ck_multiple(self, state):
        self.reset_ckbox(False)
        print("ck_multiple:",state)
        if state:
            self.bg.setExclusive(False)
        else:
            self.bg.setExclusive(True)

    def reset_ckbox(self, state):
        # print("reset_ckbox: cb01",self.cb01.isChecked())
        # print("reset_ckbox: cb02",self.cb02.isChecked())
        # print("reset_ckbox: cb03",self.cb03.isChecked())

        # exlusive인 경우, 모두 unchecked 로 못 만듬.
        # 때문에 exclusive를 잠시 해제하고, reset후, 다시 원래 상태로 돌아가는 처리함.
        old_exclusive = self.bg.exclusive()
        self.bg.setExclusive(False)

        # approach 01
        # if self.cb01.isChecked() : self.cb01.toggle()
        # if self.cb02.isChecked() : self.cb02.toggle()
        # if self.cb03.isChecked() : self.cb03.toggle()

        # approach 02
        # self.cb01.setChecked(state)
        # self.cb02.setChecked(state)
        # self.cb03.setChecked(state)

        # approach 03
        for cb in self.bg.buttons():
            cb.setChecked(state)

        self.bg.setExclusive(old_exclusive)
        print("--------------")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_wnd = MW()
    sys.exit(app.exec())
