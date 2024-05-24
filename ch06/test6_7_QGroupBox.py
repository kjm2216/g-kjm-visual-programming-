import sys, os
from PySide6.QtWidgets import (QApplication, QWidget, 
                             QRadioButton, QCheckBox,
                             QHBoxLayout,QVBoxLayout,
                             QGroupBox)

class MW (QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setMinimumSize(400,200)
        self.setWindowTitle("QGroupBox Ex")
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):

        lm = QHBoxLayout()
        self.checks = QGroupBox("QCheckBox Grp")
        self.checks.setCheckable(True)
        self.checks.setChecked(False)
        self.radios = QGroupBox("QRadioButton Grp")

        lm.addWidget(self.checks)
        lm.addWidget(self.radios)


        self.set_checks()
        self.set_radios()

        self.setLayout(lm)

    def set_checks(self):

        lm = QVBoxLayout()

        self.cb_0 = QCheckBox(f"check 0")
        self.cb_1 = QCheckBox(f"check 1")
        self.cb_2 = QCheckBox(f"check 2")
        lm.addWidget(self.cb_0)
        lm.addWidget(self.cb_1)
        lm.addWidget(self.cb_2)
        self.checks.setLayout(lm)
        self.cb_0.clicked.connect(self.toggle_check_box)
        self.cb_1.clicked.connect(self.toggle_check_box)
        self.cb_2.clicked.connect(self.toggle_check_box)
        self.checks.clicked.connect(self.clk_checks)

    def set_radios(self):

        lm = QVBoxLayout()

        self.rb_0 = QRadioButton(f"radio 0")
        self.rb_1 = QRadioButton(f"radio 1")
        self.rb_2 = QRadioButton(f"radio 2")
        lm.addWidget(self.rb_0)
        lm.addWidget(self.rb_1)
        lm.addWidget(self.rb_2)
        self.radios.setLayout(lm)
        self.rb_0.clicked.connect(self.toggle_radio_btn)
        self.rb_1.clicked.connect(self.toggle_radio_btn)
        self.rb_2.clicked.connect(self.toggle_radio_btn)
        self.radios.clicked.connect(self.clk_radios)

    def toggle_check_box(self):
        # if state:
        #     print(self.sender().text())
        if self.cb_0.isChecked():
            print(self.cb_0.text())
        if self.cb_1.isChecked():
            print(self.cb_1.text())
        if self.cb_2.isChecked():
            print(self.cb_2.text())
        print("==================")

    def toggle_radio_btn(self):
        # if state:
        #     print("sender:", self.sender().text())
        if self.rb_0.isChecked():
            print(self.rb_0.text())
        if self.rb_1.isChecked():
            print(self.rb_1.text())
        if self.rb_2.isChecked():
            print(self.rb_2.text())
        print("==================")

    def clk_checks(self, checked):
        print("checks!", checked)
        print("-----------------")

    def clk_radios(self, checked):
        print("radios!", checked)
        print("-----------------")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())
