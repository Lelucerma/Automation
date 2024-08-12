'''
Author: wang w1838978548@126.com
Date: 2024-01-08 13:38:44
LastEditors: wang w1838978548@126.com
LastEditTime: 2024-01-11 15:31:16
FilePath: \Automation\data.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.datasets import electrocardiogram
# from scipy.signal import find_peaks, peak_prominences, peak_widths
# x = np.linspace(0, 6 * np.pi, 1000)
# x = np.sin(x) + 0.6 * np.sin(2.6 * x)
# peaks, _ = find_peaks(x)
# # result_half = peak_widths(x, peaks)
# prominences = peak_prominences(x, peaks)[0]
# contour_heights = x[peaks] - prominences
# result_full = peak_widths(x, peaks, rel_height=1)
# # print(result_half)
# plt.plot(x)
# plt.plot(peaks, x[peaks], "x")
# # plt.hlines(*result_half[1:], color="C2")
# # plt.vlines(x=peaks, ymin=contour_heights, ymax=x[peaks])
# plt.hlines(*result_full[1:], color="C3")
# # plt.plot(np.zeros_like(x), "--", color="gray")
# plt.show()

# # print(type(x), x[peaks], peaks)

import matplotlib
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QGridLayout, QWidget

matplotlib.use("agg")  # 声明使用QT5
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import sys
import random
from PySide6.QtCore import QTimer

from ui.Kamor_pump_ui import Ui_Form

#创建一个matplotlib图形绘制类
#-*-coding:utf-8-*-
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import numpy as np

import matplotlib

matplotlib.use("agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


# 创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        # 第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # 第二步：在父类中激活Figure窗口
        super(MyFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)

    # 第四步：就是画图，【可以在此类中画，也可以在其它类中画】
    def mat_plot_drow_axes(self, t, s):
        """
        用清除画布刷新的方法绘图
        :return:
        """
        self.axes.cla()  # 清除绘图区

        self.axes.spines['top'].set_visible(False)  # 顶边界不可见
        self.axes.spines['right'].set_visible(False)  # 右边界不可见
        # 设置左、下边界在（0，0）处相交
        # self.axes.spines['bottom'].set_position(('data', 0))  # 设置y轴线原点数据为 0
        self.axes.spines['left'].set_position(('data', 0))  # 设置x轴线原点数据为 0
        self.axes.plot(t, s, linewidth=0.5)
        self.fig.canvas.draw()  # 这里注意是画布重绘，self.figs.canvas
        self.fig.canvas.flush_events()  # 画布刷新self.figs.canvas

    def plotcos(self):
        self.x = np.arange(0.0, 3.0, 0.01)
        self.y = np.sin(2 * np.pi * self.x)
        self.axes.plot(self.x, self.y)
        self.fig.suptitle("uv")  # 设置标题
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(100)  # 1秒钟更新一次图表

    def update_plot(self):
        self.y = np.random.random(300)
        self.mat_plot_drow_axes(self.x, self.y)


class MainDialogImgBW(QDialog, Ui_Form):
    def __init__(self):
        super(MainDialogImgBW, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("显示matplotlib绘制图形")
        self.setMinimumSize(0, 0)

        # 第五步：定义MyFigure类的一个实例
        self.F = MyFigure(width=3, height=2, dpi=100)
        self.F.plotcos()
        # self.plotcos()
        # 第六步：在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。
        self.gridlayout = QGridLayout(self.groupBox)  # 继承容器groupBox
        self.gridlayout.addWidget(self.F, 0, 1)
        # pres = threading.Thread(target=self.pressurestart)
        #         pres.start()
        # 补充：另创建一个实例绘图并显示
        # self.plotother()

    def plotcos(self):
        self.t = np.arange(100)
        self.s = np.random.random(100)
        self.F.fig.suptitle("sin")  # 设置标题
        self.F.mat_plot_drow_axes(self.t, self.s)

    def plotother(self):
        F1 = MyFigure(width=5, height=4, dpi=100)
        F1.fig.suptitle("Figuer_4")
        F1.axes1 = F1.fig.add_subplot(221)
        x = np.arange(0, 50)
        y = np.random.rand(50)
        F1.axes1.hist(y, bins=50)
        F1.axes1.plot(x, y)
        F1.axes1.bar(x, y)
        F1.axes1.set_title("hist")
        F1.axes2 = F1.fig.add_subplot(222)

        # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
        F1.axes2.plot(x, y)
        F1.axes2.set_title("line")
        # 散点图
        F1.axes3 = F1.fig.add_subplot(223)
        F1.axes3.scatter(np.random.rand(20), np.random.rand(20))
        F1.axes3.set_title("scatter")
        # 折线图
        F1.axes4 = F1.fig.add_subplot(224)
        x = np.arange(0, 5, 0.1)
        F1.axes4.plot(x, np.sin(x), x, np.cos(x))
        F1.axes4.set_title("sincos")
        self.gridlayout.addWidget(F1, 0, 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainDialogImgBW()
    main.show()
    #app.installEventFilter(main)
    sys.exit(app.exec())
