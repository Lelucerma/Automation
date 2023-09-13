from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QTimer
from datetime import datetime
import time
import pressure as p
import motor
import threading
import random

import sys
from PySide6.QtWidgets import QApplication,QMainWindow, QVBoxLayout, QWidget, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import threading
import numpy as np


class Stats:

    def __init__(self):

        self.pump_ever = motor.Pump()
        self.slave_press = p.PressUnit()

        # 从文件中加载UI定义
        qfile_stats = QFile("D:\\2 code\\Automation\\ui\\Kamor pump.ui")
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()

        self.ui = QUiLoader().load(qfile_stats)
        self.motor = motor.Module()

        # 6、第三个泵的控制
        self.ui.pump3_open_button.clicked.connect(
            lambda: self.pump_open_button(3))
        self.ui.pump3_stop_button.clicked.connect(
            lambda: self.pump_stop_button(3))
        # 7、第四个泵的控制
        self.ui.pump4_open_button.clicked.connect(
            lambda: self.pump_open_button(4))
        self.ui.pump4_stop_button.clicked.connect(
            lambda: self.pump_stop_button(4))
        # 8、第五个泵的控制
        self.ui.pump5_open_button.clicked.connect(
            lambda: self.pump_open_button(5))
        self.ui.pump5_stop_button.clicked.connect(
            lambda: self.pump_stop_button(5))
        # 9、第六个泵的控制
        self.ui.pump6_open_button.clicked.connect(
            lambda: self.pump_open_button(6))
        self.ui.pump6_stop_button.clicked.connect(
            lambda: self.pump_stop_button(6))
        # 10、第七个泵的控制
        self.ui.pump7_open_button.clicked.connect(
            lambda: self.pump_open_button(7))
        self.ui.pump7_stop_button.clicked.connect(
            lambda: self.pump_stop_button(7))
        # 11、第八个泵的控制
        self.ui.pump8_open_button.clicked.connect(
            lambda: self.pump_open_button(8))
        self.ui.pump8_stop_button.clicked.connect(
            lambda: self.pump_stop_button(8))
        # 10、第九个泵的控制
        self.ui.pump9_open_button.clicked.connect(
            lambda: self.pump_open_button(9))
        self.ui.pump9_stop_button.clicked.connect(
            lambda: self.pump_stop_button(9))
        # 10、第十个泵的控制
        self.ui.pump10_open_button.clicked.connect(
            lambda: self.pump_open_button(10))
        self.ui.pump10_stop_button.clicked.connect(
            lambda: self.pump_stop_button(10))
        # 10、第十一个泵的控制
        self.ui.pump11_open_button.clicked.connect(
            lambda: self.pump_open_button(11))
        self.ui.pump11_stop_button.clicked.connect(
            lambda: self.pump_stop_button(11))
        # 开始溶胀
        self.ui.unit1_start.clicked.connect(self.swell_start)
        # 开始第一个单元控制
        self.ui.unit1_start.clicked.connect(self.unit1_start)
        # 开始第二个单元控制
        self.ui.unit1_start.clicked.connect(self.unit2_start)
        # 开始第二个单元控制
        self.ui.wash_start.clicked.connect(self.wash_start)
        # 压力传感器的控制
        self.ui.pressure_start.clicked.connect(self.pressure_start)
        # 压力数值的显示
        self.ui.pressure_display.clicked.connect(self.pressure_display)
        # 文本框清除按钮
        self.ui.clear_button.clicked.connect(self.clear_result_text)

    # 点击开始溶胀操作
    def swell_start(self):
        self.motor.swell(5, 3, 200)

    # 点击开始第一个单元脱保护
    def unit1_start(self):
        unit1 = threading.Thread(target=self.unit1_start_thread)
        unit1.start()
    def unit1_start_thread(self):
        speeds = [60, 60, 60, 120, 200]
        volumes = [40, 70]
        self.motor.deprotect_unit(4, speeds, volumes, True)

    # 点击开始第二个单元耦合
    def unit2_start(self):
        unit2 = threading.Thread(target=self.unit2_start_thread)
        unit2.start()
    def unit2_start_thread(self):
        speeds = [60, 60, 60, 120, 200]
        volumes = [40, 70]
        self.motor.couple_unit(4, speeds, volumes, True)
    
    # 点击开始清洗
    def wash_start(self):
        wash = threading.Thread(target=self.wash_start_thread)
        wash.start()
    def wash_start_thread(self): 
        self.wash_frequence = int(self.ui.wash_frequence.text())
        if self.wash_frequence == 0:
            self.wash_frequence = 3
        for i in range(self.wash_frequence):
            self.motor.wash_ever(7, 200)
        
        
    # 点击开始压力传感器获得相应的数值
    def pressure_start(self):
        press = threading.Thread(target=self.pressure_start_thread)
        press.start()
    def pressure_start_thread(self):
        self.path = 'D:\\2 code\\Automation\\data\\230830\\'
        self.file = str(self.ui.file_name.text())
        if self.file is None:
            self.file = 'test'
        p.serOpen('com6')
        self.press_runtime = int(self.ui.pressure_time.text())
        self.slave_addb, self.slave_adde = 3, 4
        self.slave_adds = []
        if self.slave_adde != 0:
            for i in range(self.slave_addb, self.slave_adde+1):
                self.slave_adds.append(i)
        else:
            self.slave_adds = [self.slave_addb]
        self.slave_press.slaves(self.slave_adds, self.press_runtime, self.path, self.file)
        p.serClose()

    # 显示压力
    def pressure_display(self):
        self.windows = self.slave_press.pre()
        self.windows.show()
        print('1')
    
    def update_data(self):        
        a = self.slave_press.data[3]
        b = self.slave_press.data[4]
        return a, b
    
    # 点击开始第一种泵的运转
    def pump_open_button(self, add):
        self.slave_add = add
        if self.slave_add == 3:
            self.speed = int(int(self.ui.pump3_spinbox.text()) * 140)
            self.first = '3 pump open'
        elif self.slave_add == 4:
            self.speed = int(int(self.ui.pump4_spinbox.text()) * 140)
            self.first = '4 pump open'
        elif self.slave_add == 5:
            self.speed = int(int(self.ui.pump5_spinbox.text()) * 140)
            self.first = '5 pump open'
        elif self.slave_add == 6:
            self.speed = int(int(self.ui.pump6_spinbox.text()) * 140)
            self.first = '6 pump open'
            self.newline(self.speed)
        elif self.slave_add == 7:
            self.speed = int(int(self.ui.pump7_spinbox.text()) * 140)
            self.first = '7 pump open'
            self.newline(self.speed)
        elif self.slave_add == 8:
            self.speed = int(int(self.ui.pump8_spinbox.text()) * 140)
            self.first = '8 pump open'
            self.newline(self.speed)
        elif self.slave_add == 9:
            self.speed = int(int(self.ui.pump9_spinbox.text()) * 140)
            self.first = '9 pump open'
            self.newline(self.speed)
        elif self.slave_add == 10:
            self.speed = int(int(self.ui.pump10_spinbox.text()) * 140)
            self.first = '10 pump open'
            self.newline(self.speed)
        elif self.slave_add == 11:
            self.speed = int(int(self.ui.pump11_spinbox.text()) * 140)
            self.first = '11 pump open'
            self.newline(self.speed)

        # 第一个泵的开启和命令展示
        self.pump_ever.pump_run(self.slave_add, 1, 1, self.speed)
        self.newline(self.first)

    # 点击开始第二种泵的停止
    def pump_stop_button(self, add):
        self.slave_add = add
        if self.slave_add == 3:
            self.first = '3 pump stop'
        elif self.slave_add == 4:
            self.first = '4 pump stop'
        elif self.slave_add == 5:
            self.first = '5 pump stop'
        elif self.slave_add == 6:
            self.first = '6 pump stop'
        elif self.slave_add == 7:
            self.first = '7 pump stop'
        elif self.slave_add == 8:
            self.first = '8 pump stop'
        elif self.slave_add == 9:
            self.first = '9 pump stop'
        elif self.slave_add == 10:
            self.first = '10 pump stop'
        elif self.slave_add == 11:
            self.first = '11 pump stop'
        self.newline(self.first)
        self.pump_ever.pump_run(self.slave_add, 0, 0)

    # 清除文本框内容
    def clear_result_text(self):
        self.ui.display_text.clear()

    def newline(self, cmd):
        newline = f"{datetime.now().strftime('%H:%M:%S.%f')[:-3]}→{cmd}\n"
        self.ui.display_text.append(newline)


class Great(QWidget):
    def __init__(self):
        super().__init__()
        self.window = QWidget()

        self.window.setWindowTitle('压力变化')
        self.window.setGeometry(100, 100, 800, 400)

        self.window.central_widget = QWidget()
        layout = QVBoxLayout(self.window.central_widget)

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
        # print(self.slaves.data)
        p1 = random.randint(1,100)
        p2 = random.randint(1,100)
        p3, p4 = self.a.update_data()
        # print(p3,p4)
        text1 = f"压力1: {p1} kpa"
        text2 = f"压力2: {p2} kpa"

        self.text1_label.setText(text1)
        self.text2_label.setText(text2)
        # self.data_x.pop(0)
        self.data_y1.pop(0)
        self.data_y2.pop(0)
        # 模拟实时数据，这里使用随机数
        # self.data_x.append(len(self.data_x))
        # print(self.data_x,self.data_y)
        self.data_y1.append(p1)
        self.data_y2.append(p2)
        self.line1.set_data(self.data_x, self.data_y1)
        self.line2.set_data(self.data_x, self.data_y2)
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()

def main():
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.exec()


if __name__ == "__main__":

    main()
