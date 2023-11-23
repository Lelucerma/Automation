import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class DraggableLineChart(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Draggable Line Chart")
        self.setGeometry(100, 100, 800, 600)
        self.setAttribute(Qt.WA_DeleteOnClose)  # 关闭窗口时删除对象

        # 添加阴影效果
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)
        shadow.setColor(Qt.black)
        self.setGraphicsEffect(shadow)

        # 创建主窗口布局
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # 创建 Matplotlib 画布
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # 添加拖动功能
        self.draggable(True)

        # 创建折线图
        self.plot_line()

    def plot_line(self):
        ax = self.figure.add_subplot(111)
        x_data = np.linspace(0, 10, 100)
        y_data = np.sin(x_data)
        ax.plot(x_data, y_data)
        self.canvas.draw()

    def draggable(self, enabled=True):
        if enabled:
            self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMinMaxButtonsHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.setMouseTracking(True)
            self.show()
        else:
            self.setWindowFlags(Qt.Window)
            self.setAttribute(Qt.WA_TranslucentBackground, False)
            self.setMouseTracking(False)

    def mousePressEvent(self, event):
        self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = event.globalPos() - self.old_pos
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_pos = event.globalPos()

def main():
    app = QApplication(sys.argv)
    window = DraggableLineChart()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
