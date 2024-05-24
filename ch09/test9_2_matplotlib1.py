import sys

from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
)

import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

matplotlib.use('QtAgg')

class MyCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, figsize =(5,5), dpi=100):

        self.fig, self.axes = plt.subplots(
            1,2,
            figsize=figsize, 
            dpi=dpi
        )
        super(MyCanvas, self).__init__(self.fig)

class MW(QMainWindow):

    def __init__(self):

        super().__init__()

        plt_canvas = MyCanvas(self, (10,10), 100)
        plt_canvas.axes[0].plot([0,1,2,3,4], [10,13,20,30,15], label='line')
        plt_canvas.axes[1].scatter([0,1,2,3,4], [10,13,20,30,15], label='scatter')
        for a in plt_canvas.axes:
            a.legend()
            a.grid()

        self.setCentralWidget(plt_canvas)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())
    
    
    
# from __future__ import print_function
# import matplotlib.pyplot as plt
# import matplotlib

# backends = matplotlib.rcsetup.interactive_bk
# # validate backends
# backends_valid = []
# for b in backends:
#     try:
#         plt.switch_backend(b)
#         backends_valid += [b]
#     except:
#         continue
# print(backends_valid)