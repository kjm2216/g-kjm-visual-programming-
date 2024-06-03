import sys
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.image import imread

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, QMessageBox, QMenuBar, QStatusBar, QToolBar, QTextEdit
)
from PySide6.QtGui import QIcon, QAction, QKeySequence

class CustomNavigationToolbar(NavigationToolbar):
    def __init__(self, canvas, parent):
        super().__init__(canvas, parent)
        self.add_line_action = QAction("Draw Line", self)
        self.add_line_action.setCheckable(True)
        self.add_line_action.triggered.connect(parent.toggle_line_mode)
        self.addAction(self.add_line_action)

        self.add_pencil_action = QAction("Draw Pencil", self)
        self.add_pencil_action.setCheckable(True)
        self.add_pencil_action.triggered.connect(parent.toggle_pencil_mode)
        self.addAction(self.add_pencil_action)

        self.addSeparator()

class InteractivePlot(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Interactive Image Editor")
        self.resize(1000, 600)

        self.line_mode_active = False
        self.pencil_mode_active = False

        # 상태 표시줄 설정
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        # 메뉴 바 설정
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)
        file_menu = self.menuBar.addMenu("File")

        load_action = QAction("Load Image", self)
        load_action.triggered.connect(self.load_image_from_menu)
        file_menu.addAction(load_action)

        save_action = QAction("Save Image", self)
        save_action.setShortcut(QKeySequence.Save)  # Ctrl+S 단축키 설정
        save_action.triggered.connect(self.save_image)
        file_menu.addAction(save_action)

        # 기본 NavigationToolbar 설정
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = CustomNavigationToolbar(self.canvas, self)

        # 커스텀 도구 모음 설정
        self.custom_toolbar = QToolBar("Custom Toolbar")
        self.addToolBar(Qt.TopToolBarArea, self.custom_toolbar)
        self.add_toolbar_actions()

        # 메인 레이아웃 설정
        main_layout = QHBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # 그래프와 로그 레이아웃 설정
        plot_layout = QVBoxLayout()
        main_layout.addLayout(plot_layout)

        plot_layout.addWidget(self.toolbar)
        plot_layout.addWidget(self.canvas)

        # 로그 창 설정
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        main_layout.addWidget(self.log_text)

        # 그래프 영역 설정
        self.ax = self.figure.add_subplot(111)
        self.ax.axis('off')  # 축을 초기에 비활성화하여 이미지만 표시

        # 마우스 드래그 상태 및 사각형 선택을 위한 변수 초기화
        self.dragging = False
        self.rect = None
        self.line = None
        self.pencil_path = []
        self.start_point = (0, 0)
        self.image = None

        # 마우스 클릭 및 더블클릭 이벤트 연결
        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas.mpl_connect('motion_notify_event', self.on_drag)
        self.canvas.mpl_connect('button_release_event', self.on_release)

    def add_toolbar_actions(self):
        self.draw_line_action = QAction("Draw Line", self)
        self.draw_line_action.setCheckable(True)
        self.draw_line_action.triggered.connect(self.toggle_line_mode)
        self.custom_toolbar.addAction(self.draw_line_action)

        self.draw_pencil_action = QAction("Draw Pencil", self)
        self.draw_pencil_action.setCheckable(True)
        self.draw_pencil_action.triggered.connect(self.toggle_pencil_mode)
        self.custom_toolbar.addAction(self.draw_pencil_action)

    def toggle_line_mode(self):
        self.line_mode_active = not self.line_mode_active
        if self.line_mode_active:
            self.pencil_mode_active = False
            self.draw_pencil_action.setChecked(False)
            self.statusBar.showMessage("Line drawing mode activated")
        else:
            self.statusBar.showMessage("Line drawing mode deactivated")

    def toggle_pencil_mode(self):
        self.pencil_mode_active = not self.pencil_mode_active
        if self.pencil_mode_active:
            self.line_mode_active = False
            self.draw_line_action.setChecked(False)
            self.statusBar.showMessage("Pencil drawing mode activated")
        else:
            self.statusBar.showMessage("Pencil drawing mode deactivated")

    def load_image_from_menu(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 
                                                   "Open Image", 
                                                   "", 
                                                   "Image Files (*.png *.jpg *.bmp)")
        if file_name:
            self.load_image(file_name)

    def load_image(self, file_name):
        if not file_name.lower().endswith(('.png', '.jpg', '.bmp')):
            QMessageBox.warning(self, "Invalid File", "Please select a valid image file.")
            return
        self.image = imread(file_name)
        self.ax.clear()
        self.ax.imshow(self.image)
        self.ax.axis('on')
        self.canvas.draw()
        self.statusBar.showMessage(f"Loaded image: {file_name}")
        self.log_text.append(f"Loaded image: {file_name}")

    def save_image(self):
        if self.image is None:
            QMessageBox.warning(self, "No Image", "No image to save.")
            return
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG Files (*.png);;JPG Files (*.jpg);;BMP Files (*.bmp)")
        if file_name:
            self.figure.savefig(file_name)
            self.statusBar.showMessage(f"Saved image: {file_name}")
            self.log_text.append(f"Saved image: {file_name}")

    def is_navigation_active(self):
        return self.toolbar.mode != ''

    def on_click(self, event):
        if self.image is None or self.is_navigation_active():
            return

        if self.line_mode_active:
            if event.inaxes != self.ax:
                return
            self.dragging = True
            self.start_point = (event.xdata, event.ydata)
            self.line = self.ax.add_line(plt.Line2D([event.xdata, event.xdata], [event.ydata, event.ydata], color='green'))
            self.log_text.append(f"Started line at ({event.xdata:.2f}, {event.ydata:.2f})")
            self.canvas.draw()
            return

        if self.pencil_mode_active:
            if event.inaxes != self.ax:
                return
            self.dragging = True
            self.pencil_path = [(event.xdata, event.ydata)]
            self.log_text.append(f"Started drawing at ({event.xdata:.2f}, {event.ydata:.2f})")
            return

        if event.button == 3:
            self.on_right_click(event)
        else:
            if event.inaxes != self.ax:
                return
            self.dragging = True
            self.start_point = (event.xdata, event.ydata)
            self.rect = self.ax.add_patch(
                plt.Rectangle(self.start_point, 0, 0, fill=False, color='red')
            )
            self.canvas.draw()

    def on_right_click(self, event):
        if self.image is None or self.is_navigation_active():
            return
        if event.dblclick:
            self.ax.add_patch(
                plt.Circle((event.xdata, event.ydata), 10, color='blue', fill=True)
            )
            self.log_text.append(f"Drew circle at ({event.xdata:.2f}, {event.ydata:.2f}) with radius 10")
            self.canvas.draw()

    def on_drag(self, event):
        if self.image is None or self.is_navigation_active():
            return
        if not self.dragging or not event.inaxes:
            return
        if event.dblclick:
            return 

        if self.line_mode_active:
            x0, y0 = self.start_point
            x1, y1 = event.xdata, event.ydata
            self.line.set_data([x0, x1], [y0, y1])
            self.canvas.draw()
            return

        if self.pencil_mode_active:
            self.pencil_path.append((event.xdata, event.ydata))
            path_x, path_y = zip(*self.pencil_path)
            self.ax.plot(path_x, path_y, color='black')
            self.canvas.draw()
            return

        x0, y0 = self.start_point
        x1, y1 = event.xdata, event.ydata
        self.rect.set_width(x1 - x0)
        self.rect.set_height(y1 - y0)
        self.rect.set_xy((min(x0, x1), min(y0, y1)))
        self.canvas.draw()

    def on_release(self, event):
        if self.image is None or self.is_navigation_active():
            return
        if event.button == 3:
            return
        if self.line_mode_active:
            if self.dragging:
                self.dragging = False
                x0, y0 = self.start_point
                x1, y1 = event.xdata, event.ydata
                self.log_text.append(f"Drew line to ({x1:.2f}, {y1:.2f})")
                self.canvas.draw()
            return

        if self.pencil_mode_active:
            if self.dragging:
                self.dragging = False
                self.log_text.append(f"Finished drawing")
                self.canvas.draw()
            return

        if self.dragging:
            self.dragging = False
            x0, y0 = self.start_point
            x1, y1 = event.xdata, event.ydata
            width = abs(x1 - x0)
            height = abs(y1 - y0)
            response = QMessageBox.question(self, 
                                            "Confirm", 
                                            "Keep the rectangle?", 
                                            QMessageBox.Yes | QMessageBox.No)
            if response == QMessageBox.No:
                self.rect.remove()
                self.log_text.append("Rectangle removed")
            else:
                self.log_text.append(f"Rectangle kept at ({min(x0, x1):.2f}, {min(y0, y1):.2f})\n"
                                     f"Width : {width:.2f}\n"
                                     f"Height : {height:.2f}")
            self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mwd = InteractivePlot()
    mwd.show()
    sys.exit(app.exec())
