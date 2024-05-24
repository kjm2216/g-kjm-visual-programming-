import psutil  # 시스템 리소스 모니터링을 위한 라이브러리
import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer

class DynamicPlot(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dynamic Plotting")

        # 메인 윈도우에 중앙 위젯을 설정합니다.
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # 중앙 위젯에 수직 레이아웃을 설정합니다.
        self.layout = QVBoxLayout(self.central_widget)

        # Matplotlib figure 객체를 생성합니다.
        self.canvas = plt.figure()

        # CPU 사용량을 플로팅할 subplot을 추가합니다.
        self.ax_cpu = self.canvas.add_subplot(2, 1, 1)

        # RAM 사용량을 플로팅할 subplot을 추가합니다.
        self.ax_ram = self.canvas.add_subplot(2, 1, 2)

        # 중앙 위젯에 캔버스를 추가합니다.
        self.layout.addWidget(self.canvas.canvas)

        # CPU 및 RAM 데이터를 저장할 리스트를 초기화합니다.
        self.cpu_data = []
        self.ram_data = []

        # CPU 코어 수를 가져옵니다.
        self.cpu_count = psutil.cpu_count(logical=False)

        # 플롯을 초기화합니다.
        self.init_plots()

        # 타이머를 설정하여 일정 주기로 플롯을 업데이트합니다.
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)

    def init_plots(self):
        # CPU 사용량 플롯 설정
        self.ax_cpu.set_title('CPU Usage (%)')
        self.ax_cpu.set_ylim(0, 100)
        self.ax_cpu.set_xlim(0, 10)

        # RAM 사용량 플롯 설정
        self.ax_ram.set_title('RAM Usage (%)')
        self.ax_ram.set_ylim(0, 100)
        self.ax_ram.set_xlim(0, 10)

        # CPU 및 RAM 사용량을 플롯할 선을 초기화합니다.
        self.cpu_line, = self.ax_cpu.plot([], [], lw=2)
        self.ram_line, = self.ax_ram.plot([], [], lw=2)

    def update_plot(self):
        # 현재 CPU 사용량을 가져와서 각 코어의 사용량을 계산합니다.
        cpu_percent = psutil.cpu_percent(percpu=True)

        # 현재 RAM 사용량을 가져옵니다.
        ram_percent = psutil.virtual_memory().percent

        # CPU 및 RAM 데이터 리스트에 값을 추가합니다.
        self.cpu_data.append(sum(cpu_percent) / self.cpu_count)
        self.ram_data.append(ram_percent)

        # 데이터 리스트가 10개 이상이면 가장 오래된 값을 삭제합니다.
        if len(self.cpu_data) > 10:
            self.cpu_data.pop(0)
            self.ram_data.pop(0)

        # CPU 및 RAM 데이터를 플롯에 업데이트합니다.
        self.cpu_line.set_data(range(len(self.cpu_data)), self.cpu_data)
        self.ram_line.set_data(range(len(self.ram_data)), self.ram_data)

        # x축의 범위를 업데이트합니다.
        self.ax_cpu.set_xlim(0, len(self.cpu_data))
        self.ax_ram.set_xlim(0, len(self.ram_data))

        # 캔버스를 다시 그립니다.
        self.canvas.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DynamicPlot()
    window.show()
    sys.exit(app.exec())
