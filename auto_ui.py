
from PySide6.QtWidgets import QApplication,QMainWindow,QGridLayout, QDialog, QLabel
from PySide6.QtCore import QTimer, QThread
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from datetime import datetime
import pressure as p
import motor
# import relay
from ui.Kamor_pump_ui import Ui_Form
import threading

import matplotlib
matplotlib.use("agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

pump_ever = motor.Pump()
pump_model = motor.Module()
motor_module = motor.Module()


class Stats(QDialog, Ui_Form):

    def __init__(self, parent=None):
        super(Stats, self).__init__(parent)
        self.setupUi(self)
        self.init_signal_and_slot()
        
        self.first = 'pump'
   
    def init_signal_and_slot(self):
        
        # 泵的开启、停止、反向按钮连接函数
        self.pump_click_button()
        # 单元的开启、停止按钮连接函数
        self.unit_click_button()


        # 开始第二个单元控制
        # self.unit1_wash_start_button.clicked.connect(self.washstart)
        # 压力传感器的控制
        # self.pressure_start.clicked.connect(self.pressure_starts)
        # 压力数值的显示
        # self.pressure_display.clicked.connect(self.pressure_stop)
        # 文本框清除按钮
        self.clear_button.clicked.connect(self.clear_result_text)
        self.F = MyFigure(width=3, height=2, dpi=100)
        self.F.plotcos()

    # 点击开始溶胀操作
    # def swellstart(self):
    #     pump_model.swell(5, 3, 200)

    def pump_click_button(self):
        pump_dict = {
            1: [self.pump1_open_button, self.pump1_stop_button, self.pump1_reverse_button,],
            2: [self.pump2_open_button, self.pump2_stop_button, self.pump2_reverse_button,],
            3: [self.pump3_open_button, self.pump3_stop_button, self.pump3_reverse_button,],
            4: [self.pump4_open_button, self.pump4_stop_button, self.pump4_reverse_button,],
            5: [self.pump5_open_button, self.pump5_stop_button, self.pump5_reverse_button,],
            6: [self.pump6_open_button, self.pump6_stop_button, self.pump6_reverse_button,],
            7: [self.pump7_open_button, self.pump7_stop_button, self.pump7_reverse_button,],
            8: [self.pump8_open_button, self.pump8_stop_button, self.pump8_reverse_button,],
            9: [self.pump9_open_button, self.pump9_stop_button, self.pump9_reverse_button,],
            10: [self.pump10_open_button, self.pump10_stop_button, self.pump10_reverse_button,],
            11: [self.pump11_open_button, self.pump11_stop_button, self.pump11_reverse_button,],
            12: [self.pump12_open_button, self.pump12_stop_button, self.pump12_reverse_button,],
            13: [self.pump13_open_button, self.pump13_stop_button, self.pump13_reverse_button,],
            14: [self.pump14_open_button, self.pump14_stop_button, self.pump14_reverse_button,],
            15: [self.pump15_open_button, self.pump15_stop_button, self.pump15_reverse_button,],
            16: [self.pump16_open_button, self.pump16_stop_button, self.pump16_reverse_button,],
            17: [self.pump17_open_button, self.pump17_stop_button, self.pump17_reverse_button,]
        }
        
        for i in range(1,18):
            pump_dict[i][0].clicked.connect(lambda: self.pump_open(i))
            pump_dict[i][1].clicked.connect(lambda: self.pump_stop(i))
            pump_dict[i][2].clicked.connect(lambda: self.pump_open_reverse(i))
            

    def unit_click_button(self):    
        unit_depro_dict = {
            1: [self.unit1_depro_start_button, self.unit1_depro_stop_button],
            2: [self.unit2_depro_start_button, self.unit2_depro_stop_button],
            3: [self.unit3_depro_start_button, self.unit3_depro_stop_button],
            4: [self.unit4_depro_start_button, self.unit4_depro_stop_button],
            5: [self.unit5_depro_start_button, self.unit5_depro_stop_button]
        }
        unit_couple_dict = {
            1: [self.unit1_couple_start_button, self.unit1_couple_stop_button],
            2: [self.unit2_couple_start_button, self.unit2_couple_stop_button],
            3: [self.unit3_couple_start_button, self.unit3_couple_stop_button],
            4: [self.unit4_couple_start_button, self.unit4_couple_stop_button],
            5: [self.unit5_couple_start_button, self.unit5_couple_stop_button]
        }

        for i in range(1,5):
            unit_depro_dict[i][0].clicked.connect(lambda: self.deprotect(i))
            unit_depro_dict[i][1].clicked.connect(lambda: self.unit_stop(i))
            unit_couple_dict[i][0].clicked.connect(lambda: self.couple(i))
            unit_couple_dict[i][1].clicked.connect(lambda: self.unit_stop(i))


    # 点击开始单元脱保护
    def deprotect(self):
        unit1 = threading.Thread(target=self.depro_start_thread)
        unit1.start()
    
    def depro_start_thread(self, unit_add):
        self.unit_add = unit_add
        # print(self.slave_add)
        unit_info = {
        1: {'start_pump': [3, 4, 5]},
        2: {'start_pump': [6, 7, 8]},
        3: {'start_pump': [9, 10, 11]},
        4: {'start_pump': [12, 13, 14]},
        5: {'start_pump': [15, 16, 17]},
        }
        if self.unit_add in unit_info:
            unit_start_pump = unit_info[self.slave_add]
        speeds = [60, 60, 60, 120, 200]
        volumes = [40, 70]
        add = unit_start_pump['start_pump'][0]
        pump_model.deprotect_unit(add, speeds, volumes, True)

    # 点击开始单元耦合
    def couple(self):
        unit2 = threading.Thread(target=self.couple_start_thread)
        unit2.start()
    
    def couple_start_thread(self, unit_add):
        self.unit_add = unit_add
        # print(self.slave_add)
        unit_info = {
        1: {'start_pump': [3, 4, 5]},
        2: {'start_pump': [6, 7, 8]},
        3: {'start_pump': [9, 10, 11]},
        4: {'start_pump': [12, 13, 14]},
        5: {'start_pump': [15, 16, 17]},
        }
        if self.unit_add in unit_info:
            unit_start_pump = unit_info[self.slave_add]
        # for i in range(unit_start_pump['start_pump']) :
        #     pump_ever.pump_run(i, 1, 0, self.speed)
        speeds = [60, 60, 60, 120, 200]
        volumes = [40, 70]
        add = unit_start_pump['start_pump'][0]
        pump_model.couple_unit(add, speeds, volumes, True)
    
    # 点击开始清洗
    def washstart(self):
        # wash = threading.Thread(target=self.wash_start_thread)
        # wash.start()
        self.wash_frequence = 3
        for i in range(self.wash_frequence):
            pump_model.wash_ever(3, 200)
    
    def wash_start_thread(self): 
        self.wash_frequence = int(self.wash_frequence.text())
        if self.wash_frequence == 0:
            self.wash_frequence = 3
        for i in range(self.wash_frequence):
            pump_model.wash_ever(7, 200)

    # 点击开始压力传感器获得相应的数值并显示压力
    def pressure_starts(self):
        self.file = str(self.file_name.text())
        self.press_runtime = int(self.pressure_time.text())
        self.F = MyFigure(width=3, height=2, dpi=100)
        self.F.plotcos()
        self.gridlayout = QGridLayout(self.groupBox)  # 继承容器groupBox
        self.gridlayout.addWidget(self.F, 0, 1)
        self.press_window.presss_start(self.file, self.press_runtime)
    
    # def pressure_start(self):
    #     pressure = threading.Thread(target=self.pressurestart_thread)
    #     pressure.start()

    # def pressure_stop(self):
    #     self.a = 0

    def unit_stop(self, unit_add):
        self.unit_add = unit_add
        # print(self.slave_add)
        unit_info = {
        1: {'start_pump': [3, 4, 5]},
        2: {'start_pump': [6, 7, 8]},
        3: {'start_pump': [9, 10, 11]},
        4: {'start_pump': [12, 13, 14]},
        5: {'start_pump': [15, 16, 17]},
        }
        if self.unit_add in unit_info:
            unit_start_pump = unit_info[self.slave_add]
        for i in range(unit_start_pump['start_pump']) :
            pump_ever.pump_run(i, 0, 0, self.speed)

    # 点击开始第一种泵的运转
    def pump_open(self, add):
        
        self.slave_add = add
        # print(self.slave_add)
        self.speed = 0
        pump_info = {
        3: {'spinbox': self.pump3_spinbox, 'suffix': '3 pump open'},
        4: {'spinbox': self.pump4_spinbox, 'suffix': '4 pump open'},
        5: {'spinbox': self.pump5_spinbox, 'suffix': '5 pump open'},
        6: {'spinbox': self.pump6_spinbox, 'suffix': '6 pump open'},
        7: {'spinbox': self.pump7_spinbox, 'suffix': '7 pump open'},
        8: {'spinbox': self.pump8_spinbox, 'suffix': '8 pump open'},
        9: {'spinbox': self.pump9_spinbox, 'suffix': '9 pump open'},
        10: {'spinbox': self.pump10_spinbox, 'suffix': '10 pump open'},
        11: {'spinbox': self.pump11_spinbox, 'suffix': '11 pump open'},
        12: {'spinbox': self.pump12_spinbox, 'suffix': '12 pump open'},
        13: {'spinbox': self.pump13_spinbox, 'suffix': '13 pump open'},
        14: {'spinbox': self.pump14_spinbox, 'suffix': '14 pump open'},
        15: {'spinbox': self.pump15_spinbox, 'suffix': '15 pump open'},
        16: {'spinbox': self.pump16_spinbox, 'suffix': '16 pump open'},
        17: {'spinbox': self.pump16_spinbox, 'suffix': '17 pump open'},
        }

        if self.slave_add in pump_info:
            pump_data = pump_info[self.slave_add]
            self.speed = int(int(pump_data['spinbox'].text()) * 140)
            self.first = pump_data['suffix']

        self.newline(self.first)
        # 第一个泵的开启和命令展示
        pump_ever.pump_run(self.slave_add, 1, 1, self.speed)

    def pump_open_reverse(self, add):
        
        self.slave_add = add
        # print(self.slave_add)
        self.speed = 0
        pump_info = {
        3: {'spinbox': self.pump3_spinbox, 'suffix': '3 pump reverse'},
        4: {'spinbox': self.pump4_spinbox, 'suffix': '4 pump reverse'},
        5: {'spinbox': self.pump5_spinbox, 'suffix': '5 pump reverse'},
        6: {'spinbox': self.pump6_spinbox, 'suffix': '6 pump reverse'},
        7: {'spinbox': self.pump7_spinbox, 'suffix': '7 pump reverse'},
        8: {'spinbox': self.pump8_spinbox, 'suffix': '8 pump reverse'},
        9: {'spinbox': self.pump9_spinbox, 'suffix': '9 pump reverse'},
        10: {'spinbox': self.pump10_spinbox, 'suffix': '10 pump reverse'},
        }

        if self.slave_add in pump_info:
            pump_data = pump_info[self.slave_add]
            self.speed = int(int(pump_data['spinbox'].text()) * 140)
            self.first = pump_data['suffix']

        self.newline(self.first)
        # 第一个泵的开启和命令展示
        pump_ever.pump_run(self.slave_add, 1, 0, self.speed)        

    # 点击开始第二种泵的停止
    def pump_stop(self, add):
        self.slave_add = add
        self.pump_data = f'{self.slave_add}' + 'pump stop'

        # 第一个泵的关闭和命令展示
        self.newline(self.pump_data)
        pump_ever.pump_run(self.slave_add, 0, 0, 0)

    # 点击开始阀门的开启
    def value_open_button(self, add):
        self.value_add = add
        self.value_tranlation()
        self.value_con = relay.Value(self.value_add)
        self.value_con.value_start()

    # 点击开始阀门的关闭
    def value_stop_button(self, add):
        self.value_add = add
        self.value_tranlation()
        self.value_con = relay.Value(self.value_add)
        self.value_con.value_end()

    # 将阀门的值转化为树莓派对应的引脚
    def value_tranlation(self):
        self.values = {9: "11", 10: "12"}  # 第9个按钮，对应的是第一个阀门，对应的树莓上面第17个引脚
        if self.value_add in self.values:
            self.value_add = int(self.values[self.value_add])

    # 清除文本框内容
    def clear_result_text(self):
        self.display_text.clear()

    # 添加一行新的内容
    def newline(self, cmd):
        newline = f"{datetime.now().strftime('%H:%M:%S.%f')[:-3]}→{cmd}\n"
        self.display_text.append(newline)


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
        self.x = np.arange(0.0, 3.0, 0.1)
        self.y = np.sin(2 * np.pi * self.x)
        self.axes.plot(self.x, self.y)
        self.fig.suptitle("uv")  # 设置标题
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(100)  # 1秒钟更新一次图表

    def update_plot(self):
        self.y = np.random.random(30)
        self.mat_plot_drow_axes(self.x, self.y)


# def main():
#     global b
#     app = QApplication([])
#     stats = Stats()
#     stats.show()
#     app.exec()


# if __name__ == "__main__":

#     main()
