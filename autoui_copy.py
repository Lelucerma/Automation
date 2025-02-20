'''
Author: wang w1838978548@126.com
Date: 2024-07-24 16:35:48
LastEditors: wang w1838978548@126.com
LastEditTime: 2025-02-18 20:35:43
FilePath: \Automation\auto_ui.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

from PySide6.QtWidgets import QGridLayout, QDialog
from PySide6.QtCore import QTimer, Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from datetime import datetime
import pressure as p
import motor
import random
import os
from ui.Kamor_pump_2_ui import Ui_Form
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
        self.stop_event = threading.Event()
        self.first = 'pump'
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)

    def init_signal_and_slot(self):

        self.start_pushButton.clicked.connect(self.start)
        self.stop_pushButton.clicked.connect(self.stop)

        # 泵的开启与停止控制按钮
        # 6、第三个泵的控制
        self.pump3_open_button.clicked.connect(
            lambda: self.pump_open_button(3))
        self.pump3_reverse.clicked.connect(lambda: self.pump_open_reverse(3))
        self.pump3_stop_button.clicked.connect(
            lambda: self.pump_stop_button(3))
        # 7、第四个泵的控制
        self.pump4_open_button.clicked.connect(
            lambda: self.pump_open_button(4))
        self.pump4_reverse.clicked.connect(lambda: self.pump_open_reverse(4))
        self.pump4_stop_button.clicked.connect(
            lambda: self.pump_stop_button(4))
        # 8、第五个泵的控制
        self.pump5_open_button.clicked.connect(
            lambda: self.pump_open_button(5))
        self.pump5_reverse.clicked.connect(lambda: self.pump_open_reverse(5))
        self.pump5_stop_button.clicked.connect(
            lambda: self.pump_stop_button(5))
        # 9、第六个泵的控制
        self.pump6_open_button.clicked.connect(
            lambda: self.pump_open_button(6))
        self.pump6_reverse.clicked.connect(lambda: self.pump_open_reverse(6))
        self.pump6_stop_button.clicked.connect(
            lambda: self.pump_stop_button(6))
        # 10、第七个泵的控制
        self.pump7_open_button.clicked.connect(
            lambda: self.pump_open_button(7))
        self.pump7_reverse.clicked.connect(lambda: self.pump_open_reverse(7))
        self.pump7_stop_button.clicked.connect(
            lambda: self.pump_stop_button(7))
        # 11、第八个泵的控制
        self.pump8_open_button.clicked.connect(
            lambda: self.pump_open_button(8))
        self.pump8_reverse.clicked.connect(lambda: self.pump_open_reverse(8))
        self.pump8_stop_button.clicked.connect(
            lambda: self.pump_stop_button(8))
        # 10、第九个泵的控制
        self.pump9_open_button.clicked.connect(
            lambda: self.pump_open_button(9))
        self.pump9_reverse.clicked.connect(lambda: self.pump_open_reverse(9))
        self.pump9_stop_button.clicked.connect(
            lambda: self.pump_stop_button(9))
        # 10、第十个泵的控制
        self.pump10_open_button.clicked.connect(
            lambda: self.pump_open_button(10))
        self.pump10_reverse.clicked.connect(lambda: self.pump_open_reverse(10))
        self.pump10_stop_button.clicked.connect(
            lambda: self.pump_stop_button(10))
        # 11、第十一个泵的控制
        self.pump11_open_button.clicked.connect(
            lambda: self.pump_open_button(11))
        self.pump11_reverse.clicked.connect(lambda: self.pump_open_reverse(11))
        self.pump11_stop_button.clicked.connect(
            lambda: self.pump_stop_button(11))

        # 阀门1和2的控制

        self.value1_dial.valueChanged.connect(lambda: self.value_tran(31))
        # self.value2_dial.valueChanged.connect(lambda: self.value_tran(102))

        # 开始溶胀
        # self.unit1_wash_start_button.clicked.connect(self.swellstart)

        # 开始脱保护单元的控制
        self.unit1_depro_start_button.clicked.connect(
            lambda: self.deprotect(1))
        self.unit2_depro_start_button.clicked.connect(
            lambda: self.deprotect(2))
        self.unit3_depro_start_button.clicked.connect(
            lambda: self.deprotect(3))


        # 开始脱保护单元的控制
        self.unit1_depro_stop_button.clicked.connect(lambda: self.unit_stop(1))
        self.unit2_depro_stop_button.clicked.connect(lambda: self.unit_stop(2))
        self.unit3_depro_stop_button.clicked.connect(lambda: self.unit_stop(3))


        # 开始耦合单元的控制
        self.unit1_couple_start_button.clicked.connect(
            lambda: self.couple_unit(1))
        self.unit2_couple_start_button.clicked.connect(
            lambda: self.couple_unit(2))
        self.unit3_couple_start_button.clicked.connect(
            lambda: self.couple_unit(3))


        # 开始耦合单元的停止
        self.unit1_couple__stop_button.clicked.connect(
            lambda: self.unit_stop(1))
        self.unit2_couple__stop_button.clicked.connect(
            lambda: self.unit_stop(2))
        self.unit3_couple__stop_button.clicked.connect(
            lambda: self.unit_stop(3))


        # 开始第二个单元控制
        self.unit1_wash_start_button.clicked.connect(self.washstart)
        # 压力传感器的控制
        self.pressure_start.clicked.connect(self.pressurestart_thread)
        # 压力数值的显示
        # self.pressure_display.clicked.connect(self.pressure_stop)
        # 文本框清除按钮
        self.clear_button.clicked.connect(self.clear_result_text)
        self.pressure_stop.clicked.connect(self.stop_timer)

        # self.F = MyFigure(width=3, height=2, dpi=100)
        # self.F.plotcos()

    # 点击开始溶胀操作
    # def swellstart(self):
    #     pump_model.swell(5, 3, 200)

    # 点击开始单元脱保护
    def deprotect(self, add):
        unit1 = threading.Thread(target=self.depro_start_thread, args={add})
        unit1.start()

    def depro_start_thread(self, unit_add):
        self.unit_add = unit_add
        # print(self.slave_add)/
        unit_info = {
            1: {
                'start_pump': [3, 4, 5, [4, 17, 1], [12, 17, 1]],
                'nextwaste': [13, 17, 2]
            },
            2: {
                'start_pump': [6, 7, 8, [7, 17, 2], [13, 17, 2]],
                'nextwaste': [14, 17, 3]
            },
            3: {
                'start_pump': [9, 10, 11, [10, 17, 3], [14, 17, 3]],
                'nextwaste': [12, 17, 1]
            }
        }

        if self.unit_add == 4:
            for i in range(3):
                self.unit_add = i + 1
                unit_start_pump = unit_info[self.unit_add]
                adds = unit_start_pump['start_pump']
                next_waste = unit_start_pump['nextwaste']
                pump_model.deprotect_unit(adds, next_waste=next_waste)
        else:
            if self.unit_add in unit_info:
                unit_start_pump = unit_info[self.unit_add]
            adds = unit_start_pump['start_pump']
            next_waste = unit_start_pump['nextwaste']
            pump_model.deprotect_unit(adds,
                                      reaction_time=120,
                                      next_waste=next_waste)

    # 点击开始单元耦合
    def couple_unit(self, add):
        unit1 = threading.Thread(target=self.couple_start_thread, args={add})
        unit1.start()

    def couple_start_thread(self, unit_add):
        self.unit_add = unit_add
        # print(self.slave_add)/
        unit_info = {
            1: {
                'start_pump': [3, 4, 5, [4, 17, 1], [12, 17, 1]],
                'nextwaste': [13, 17, 2]
            },
            2: {
                'start_pump': [6, 7, 8, [7, 17, 2], [13, 17, 2]],
                'nextwaste': [14, 17, 3]
            },
            3: {
                'start_pump': [9, 10, 11, [10, 17, 3], [14, 17, 3]],
                'nextwaste': [12, 17, 1]
            }
        }
        if self.unit_add in unit_info:
            unit_start_pump = unit_info[self.unit_add]
        adds = unit_start_pump['start_pump']
        next_waste = unit_start_pump['nextwaste']
        pump_model.deprotect_unit(adds,
                                  reaction_time=600,
                                  next_waste=next_waste)

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

    def clear_layout(self):
        # 清除groupBox现有的布局及其内容
        existing_layout = self.groupBox.layout()
        if existing_layout:
            # 移除布局中的所有部件
            while existing_layout.count():
                item = existing_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
            # 删除布局本身
            existing_layout.deleteLater()

    def pressurestart_thread(self):
        self.clear_layout()  # 清除旧布局
        # self.file = str(self.file_name.text())
        # self.press_runtime = int(self.pressure_time.text())
        self.ti = QTimer()
        self.F = MyFigure(width=3, height=2, dpi=100)
        self.F.plotcos(self.ti, 30)
        # 创建新布局并添加到groupBox
        self.gridlayout = QGridLayout(self.groupBox)
        self.gridlayout.addWidget(self.F, 0, 1)

    
    def stop_timer(self):
        self.ti.stop()

    def start(self):        
        startReaction = threading.Thread(target=self.start_thread)
        startReaction.start()
    
    def start_thread(self):
        while not self.stop_event.is_set():  # 检查事件是否被设置
            teproAdd = [3, 4, 5, [4, 17, 1], [12, 17, 1]]
            coupleAdd = [6, 7, 8, [7, 17, 2], [13, 17, 2]]
            nextTepro = [13, 17,2]
            nextCouple = [14, 17,3]
            teproVol = int(self.tepro_vol_spinBox.text())
            coupleVol = int(self.couple_vol_spinBox.text())
            teproTime = int(self.tepro_time_spinBox.text())
            coupleTime = int(self.couple_time_spinBox.text())
            washFrequence = int(self.wash_frequence_spinBox.text())
            pump_model.deprotect_unit(teproAdd, teproTime, teproVol, washFrequence, nextTepro)
            pump_model.deprotect_unit(coupleAdd, coupleTime, coupleVol, washFrequence, nextCouple)

    def stop(self):
        self.stop_event.set()  # 设置事件，通知线程停止
        for i in range(3, 14):
            pump_ever.pump_run(i, 0, 0)
    
    def kill(self, pid):
        # 本函数用于中止传入pid所对应的进程
        if os.name == 'nt':
            # Windows系统
            cmd = 'taskkill /pid ' + str(self.pid) + ' /f'
            try:
                os.system(cmd)
                print(pid, 'killed')
            except Exception as e:
                print(e)
        elif os.name == 'posix':
            # Linux系统
            cmd = 'kill ' + str(pid)
            try:
                os.system(cmd)
                print(pid, 'killed')
            except Exception as e:
                print(e)
        else:
            print('Undefined os.name')
        # def pressure_starts(self):
        #     pressure = threading.Thread(target=self.pressurestart_thread)
        #     pressure.start()

        # def pressure_stop(self):
        #     self.a = 0

    def unit_stop(self, unit_add):
        self.unit_add = unit_add
        # print(self.slave_add)
        unit_info = {
            1: {
                'start_pump': [3, 4, 5]
            },
            2: {
                'start_pump': [6, 7, 8]
            },
            3: {
                'start_pump': [9, 10, 11]
            },
            4: {
                'start_pump': [12, 13, 14]
            },
            5: {
                'start_pump': [15, 16, 17]
            },
        }
        if self.unit_add in unit_info:
            unit_start_pump = unit_info[self.unit_add]
        for i in (unit_start_pump['start_pump']):
            pump_ever.pump_run(i, 0, 0, 0)

    # 点击开始第一种泵的运转
    def pump_open_button(self, add):

        self.slave_add = add
        # print(self.slave_add)
        self.speed = 0
        pump_info = {
            3: {
                'spinbox': self.pump3_spinbox,
                'suffix': '3 pump open'
            },
            4: {
                'spinbox': self.pump4_spinbox,
                'suffix': '4 pump open'
            },
            5: {
                'spinbox': self.pump5_spinbox,
                'suffix': '5 pump open'
            },
            6: {
                'spinbox': self.pump6_spinbox,
                'suffix': '6 pump open'
            },
            7: {
                'spinbox': self.pump7_spinbox,
                'suffix': '7 pump open'
            },
            8: {
                'spinbox': self.pump8_spinbox,
                'suffix': '8 pump open'
            },
            9: {
                'spinbox': self.pump9_spinbox,
                'suffix': '9 pump open'
            },
            10: {
                'spinbox': self.pump10_spinbox,
                'suffix': '10 pump open'
            },
            11: {
                'spinbox': self.pump11_spinbox,
                'suffix': '11 pump open'
            }
        }

        if self.slave_add in pump_info:
            pump_data = pump_info[self.slave_add]
            self.speed = int(int(pump_data['spinbox'].text()) * 140)
            self.first = pump_data['suffix']

        self.newline(self.first)
        # 第一个泵的开启和命令展示
        # pump_ever.pump_run(self.slave_add, 1, 1, self.speed)

    def pump_open_reverse(self, add):

        self.slave_add = add
        # print(self.slave_add)
        self.speed = 0
        pump_info = {
            3: {
                'spinbox': self.pump3_spinbox,
                'suffix': '3 pump reverse'
            },
            4: {
                'spinbox': self.pump4_spinbox,
                'suffix': '4 pump reverse'
            },
            5: {
                'spinbox': self.pump5_spinbox,
                'suffix': '5 pump reverse'
            },
            6: {
                'spinbox': self.pump6_spinbox,
                'suffix': '6 pump reverse'
            },
            7: {
                'spinbox': self.pump7_spinbox,
                'suffix': '7 pump reverse'
            },
            8: {
                'spinbox': self.pump8_spinbox,
                'suffix': '8 pump reverse'
            },
            9: {
                'spinbox': self.pump9_spinbox,
                'suffix': '9 pump reverse'
            },
            10: {
                'spinbox': self.pump10_spinbox,
                'suffix': '10 pump reverse'
            }
        }

        if self.slave_add in pump_info:
            pump_data = pump_info[self.slave_add]
            self.speed = int(int(pump_data['spinbox'].text()) * 140)
            self.first = pump_data['suffix']

        self.newline(self.first)
        # 第一个泵的开启和命令展示
        # pump_ever.pump_run(self.slave_add, 1, 0, self.speed)

    # 点击开始第二种泵的停止
    def pump_stop_button(self, add):
        self.slave_add = add
        pump_info = {
            3: '3 pump stop',
            4: '4 pump stop',
            5: '5 pump stop',
            6: '6 pump stop',
            7: '7 pump stop',
            8: '8 pump stop',
            9: '9 pump stop',
            11: '11 pump stop',
            10: '10 pump stop'            
        }
        self.pump_data = pump_info[self.slave_add]

        # 第一个泵的开启和命令展示
        # pump_ever.pump_run(self.slave_add, 0, 0, 0)
        self.newline(self.pump_data)

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

    # 多通阀阀门通道的转换
    def value_tran(self, add):
        self.slave_add = add
        value_info = {
            31: {
                'passage': self.value1_dial,
                'label': self.value1_passage_label
            },
            32: {
                'passage': self.value2_dial,
                'label': self.valeu2_passage_label
            }
        }
        self.value_value = value_info[self.slave_add]
        self.value_passage = int(self.value_value['passage'].value())
        if self.value_passage == 0:
            pump_ever.value_change(self.slave_add, self.value_passage)
            self.hole = pump_ever.value_change(self.slave_add,
                                               self.value_passage)
            self.value_value['label'].setText(str(self.hole))
        if self.value_passage <= 10:
            self.value_value['label'].setText(str(self.value_passage))
            pump_ever.value_change(self.slave_add, self.value_passage)
        else:
            self.hole = pump_ever.value_change(self.slave_add,
                                               self.value_passage)
            self.value_value['label'].setText(str(self.hole))

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
        self.press = p.PressUnit()
        self.m = 1

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
        # self.axes.spines['left'].set_position(('data', 0))  # 设置x轴线原点数据为 0
        self.axes.set_ylabel("kPa")
        self.axes.set_xlabel("s")
        # 获取 x 轴和 y 轴的标签对象
        x_label = self.axes.xaxis.label
        y_label = self.axes.yaxis.label

        # 设置 x 轴标签的位置（在 x 轴的最右边）
        x_label.set_position((1.0, 0.3))  # (x, y) 坐标，x=1.0 表示最右边
        x_label.set_horizontalalignment('right')  # 水平对齐方式为右对齐
        # 设置 y 轴标签的位置（在 y 轴的最上端）
        y_label.set_position((0.0, 1.0))  # (x, y) 坐标，y=1.0 表示最上端
        y_label.set_verticalalignment('top')  # 垂直对齐方式为上对齐


        self.axes.plot(t, s, linewidth=0.5)
        self.fig.canvas.draw()  # 这里注意是画布重绘，self.figs.canvas
        self.fig.canvas.flush_events()  # 画布刷新self.figs.canvas

    def plotcos(self, ti, stop):
        # self.file = file
        # self.time1 = time1
        # self.x = np.arange(0.0, 3.0, 0.1)
        # a = [0,0,0,0,0,0,0,0,0,0]
        # self.y = np.array(a*3)
        self.axes.cla()  # 清除绘图区
        self.stop = stop
        self.x = [1]
        self.y = [0]
        self.axes.plot(self.x, self.y)
        self.fig.suptitle("pressure")  # 设置标题
        self.timer = ti
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # 1秒钟更新一次图表

    def stop_timer(self):
        self.timer.stop()

    def update_plot(self):
        # self.press.slaves([3], self.time1, self.file)
        self.m += 1
        self.data = round(random.uniform(0.45, 0.55), 2)
        self.x.append(self.m)
        self.y.append(self.data)
        # self.y = np.random.random(1)
        # if self.m < self.stop:
        self.mat_plot_drow_axes(self.x, self.y)
        if self.m > self.stop:
            self.stop_timer()

# def main():
#     global b
#     app = QApplication([])
#     stats = Stats()
#     stats.show()
#     app.exec()

# if __name__ == "__main__":

#     main()
