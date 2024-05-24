import sys
from PySide6.QtWidgets import(QApplication, QWidget,
                            QLabel, QGridLayout)
from PySide6.QtCore import Qt
from  PySide6.QtGui  import  QFont

class  MW(QWidget):
    def  __init__(self):
        super().__init__()
        self.init_ui()

    def  init_ui(self):
        """Set up the application's GUI."""
        self.setMinimumSize(500, 500)
        self.setWindowTitle("QGridLayout Example")
        self.setup_mw()
        self.show()

    def  setup_mw(self):
        colors = ['white','gray','blue','red','yellow']
        labels = []
        for  i  in  range(5):
            label = QLabel(f"label {i}")
            label.setFont(QFont("Arial", 20))
            label.setStyleSheet(f"background-color:{colors[i]}")
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            labels.append(label)

        self.main_grid = QGridLayout()

        self.main_grid.addWidget(labels[0], 0, 0)       
        self.main_grid.addWidget(labels[1], 1, 0, 3, 3)
        self.main_grid.addWidget(labels[2], 4, 0, 1, 1)
        self.main_grid.addWidget(labels[3], 4, 1)
        self.main_grid.addWidget(labels[4], 5, 2)

        self.setLayout(self.main_grid)

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    wd = MW()
    sys.exit(app.exec())