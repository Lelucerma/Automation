import sys
from PySide6.QtWidgets import QApplication,QMainWindow, QVBoxLayout, QWidget, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import threading
import numpy as np
# import pressure as p

class Stats:

    def __init__(self):

        # 从文件中加载UI定义
        qfile_stats = QFile("D:\\2 code\\Automation\\ui\\Kamor pump.ui")
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()

        self.ui = QUiLoader().load(qfile_stats)
        self.ui.pressure_display.clicked.connect(self.pressure_display)

    def pressure_display(self):
        self.window = pressureupdate()
        self.window.show()

class pressureupdate(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('压力变化')
        self.setGeometry(100, 100, 620, 480)

        self.central_widget = QWidget(self)
        layout = QVBoxLayout(self.central_widget)

        self.text1_label = QLabel('压力1:')
        self.text2_label = QLabel('压力2:')
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text2_label)

        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 100)
        self.line1, = self.ax.plot([], [])
        self.line2, = self.ax.plot([], [])

        self.data_x = np.arange(10)
        self.data_y1 = [0,0,0,0,0,0,0,0,0,0]
        self.data_y2 = [0,0,0,0,0,0,0,0,0,0]

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # 1秒钟更新一次图表


    def update_plot(self):
        # 这里可以替换为你自己的文本数据生成逻辑
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        text1 = f"压力1: {a} kpa"
        text2 = f"压力2: {b} kpa"

        self.text1_label.setText(text1)
        self.text2_label.setText(text2)
        # self.data_x.pop(0)
        self.data_y1.pop(0)
        self.data_y2.pop(0)
        # 模拟实时数据，这里使用随机数
        # self.data_x.append(len(self.data_x))
        # print(self.data_x,self.data_y)
        self.data_y1.append(a)
        self.data_y2.append(b)
        self.line1.set_data(self.data_x, self.data_y1)
        self.line2.set_data(self.data_x, self.data_y2)
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication([])
    windows = Stats()
    window = pressureupdate()
    # window.show()
    windows.ui.show()
    app.exec()

