import sys

PYSIDE = True

try:

      import PySide6.QtCore

      from PySide6.QtWidgets import (QApplication, QWidget, QLabel)

except:

      PYSIDE = False

PYQT = True

try:

      import PyQt6.Qtcore

      from PyQt6.QtWidgets import (QApplication, QWidget, QLabel)

except:

      PYQT = False

class MW(QWidget):

      def __init__(self):

            """ Constructor for Empty Window Class """

            super().__init__()

            self.initializeUI()

      def initializeUI(self):

            """set up the application"""

            self.setGeometry(200, 100, 400, 200)

            self.setWindowTitle("Main Window in PyQt")

            self.setup_main_wnd()

            self.show()  #Display the window on the screen

      def setup_main_wnd(self):

            """set up the main window"""

            hello_label = QLabel(self)

            hello_label.setText('Hello, World and Qt!')

            hello_label.move(150,90)

# Run the program

if __name__=='__main__':
    if PYSIDE:

        print(PySide6.__version__)

        print(PySide6.QtCore.__version__)

    if PYQT:

        print(PyQt6.Qtcore.qVersion())

app = QApplication(sys.argv)

print(sys.argv)​

window = MW()

sys.exit(app.exec())