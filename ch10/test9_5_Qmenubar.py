import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt

class MW (QMainWindow):
  def __init__(self):
    super().__init__()
    self.init_ui()
  def init_ui(self):
    """ application의 gui를 초기화하는 메서드"""
    self.fstr = os.path.dirname(
      os.path.abspath(__file__)
    )
    self.setMinimumSize(600,600)
    self.setWindowTitle("Menu bar Ex")
    self.setup_main_wnd()    
    self.create_actions()   
    self.create_menu()        
    self.show()

  def create_actions (self):
    self.quit_act = QAction("Quit")
    self.quit_act.setShortcut("Ctrl+X")
    tmp = os.path.join(self.fstr,"exit.png")
    self.quit_act.setIcon(QIcon(tmp))
    self.quit_act.triggered.connect(self.close)

  def create_menu(self):
    """어플리케이션의 menu bar를 만드는 method."""
    mb = self.menuBar()                        
    menu_item = mb.addMenu("test")   
    menu_item.addAction(self.quit_act)
    mb.setNativeMenuBar(False) 

  def setup_main_wnd(self):
    label = QLabel('test')
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.setCentralWidget(label)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  wnd = MW()
  sys.exit(app.exec())
