'''
Author: wang w1838978548@126.com
Date: 2023-09-11 21:23:35
LastEditors: wang w1838978548@126.com
LastEditTime: 2023-11-23 16:42:45
FilePath: \Automation\test\online_graph.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class RealTimePlot(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('实时折线图示例')
        self.setGeometry(100, 100, 800, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 100)
        self.line, = self.ax.plot([], [])

        self.data_x = np.arange(10)
        self.data_y = [0,0,0,0,0,0,0,0,0,0]

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # 1秒钟更新一次图表

    def update_plot(self):
        # self.data_x.pop(0)
        self.data_y.pop(0)
        # 模拟实时数据，这里使用随机数
        # self.data_x.append(len(self.data_x))
        print(self.data_x,self.data_y)
        self.data_y.append(random.randint(0, 100))
        self.line.set_data(self.data_x, self.data_y)
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RealTimePlot()
    window.show()
    sys.exit(app.exec_())
"""
import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSizePolicy
from PySide6.QtCore import QTimer  # 导入 QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import time

class RealTimePlotApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Real-Time Plot")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.figure = Figure()
        self.ax = self.figure.add_subplot(111)  # 1行1列的子图
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(NavigationToolbar(self.canvas, self))  # 添加工具栏
        layout.addWidget(self.canvas)

        self.x_data = np.linspace(0, 10, 1000)
        self.y_data = np.zeros_like(self.x_data)

        self.line, = self.ax.plot(self.x_data, self.y_data)

        self.start_time = time.time()
        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.update_plot)
        self.animation_timer.start(100)  # 更新频率为每100毫秒

    def update_plot(self):
        # 模拟实时数据更新
        elapsed_time = time.time() - self.start_time
        self.y_data = np.sin(self.x_data + elapsed_time)
        self.line.set_ydata(self.y_data)
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()

def main():
    app = QApplication(sys.argv)
    window = RealTimePlotApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
