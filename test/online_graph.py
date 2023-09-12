import sys
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
