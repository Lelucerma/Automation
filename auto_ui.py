from PySide6.QtWidgets import QApplication,QMainWindow, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import QTimer, QThread
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from datetime import datetime
import pressure as p
import motor
from Kamor_pump_ui import Ui_Form

pump_ever = motor.Pump()
motor_module = motor.Module()

class Stats(QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(Stats, self).__init__(parent)
        self.setupUi(self)
        self.init_signal_and_slot()

    def init_signal_and_slot(self):

        for pump_number in range(3, 10):
            open_button = getattr(self, f"pump{pump_number}_open_button")
            stop_button = getattr(self, f"pump{pump_number}_stop_button")

            open_button.clicked.connect(lambda number=pump_number: self.pump_open_button(number))
            stop_button.clicked.connect(lambda number=pump_number: self.pump_stop_button(number))

        # 开始溶胀
        self.swell_start.clicked.connect(self.swellstart)
        # 开始第一个单元控制
        self.unit1_start.clicked.connect(self.deprotect)
        # 开始第二个单元控制
        self.unit2_start.clicked.connect(self.couple_unit)
        # 开始第二个单元控制
        self.wash_start.clicked.connect(self.washstart)
        # 压力传感器的控制
        self.pressure_start.clicked.connect(self.pressurestart)
        # 压力数值的显示
        self.pressure_display.clicked.connect(self.pressuredisplay)
        # 文本框清除按钮
        self.clear_button.clicked.connect(self.clear_result_text)

    # 点击开始溶胀操作
    def swellstart(self):
        self.swell = Couple_unit()
        self.swell.start()
    
    # 点击开始第一个单元脱保护
    def deprotect(self):
        self.depro = Couple_unit()
        self.depro.start()

    # 点击开始第二个单元耦合
    def couple_unit(self):
        self.unit2 = Couple_unit()
        self.unit2.start()

    # 点击开始清洗
    def washstart(self):
        self.wash = Couple_unit()
        self.wash.start()

    # 点击开始压力传感器获得相应的数值
    def pressurestart(self):
        self.file = str(self.file_name.text())
        self.press_runtime = int(self.pressure_time.text())
        self.press_window = Great()
        self.press_window.show()
        self.press_window.presss_start(self.file, self.press_runtime)
    
    # 显示压力
    def pressuredisplay(self):
        self.press_window = p.Pre_ui()
        self.press_window.show()
    
    # 点击开始第一种泵的运转
    def pump_open_button(self, add):
        self.slave_add = add
        self.speed = 0
        pump_info = {
        3: {'spinbox': self.pump3_spinbox, 'suffix': '3 pump open'},
        4: {'spinbox': self.pump4_spinbox, 'suffix': '4 pump open'},
        3: {'spinbox': self.pump5_spinbox, 'suffix': '5 pump open'},
        6: {'spinbox': self.pump6_spinbox, 'suffix': '6 pump open'},
        7: {'spinbox': self.pump7_spinbox, 'suffix': '7 pump open'},
        8: {'spinbox': self.pump8_spinbox, 'suffix': '8 pump open'},
        9: {'spinbox': self.pump9_spinbox, 'suffix': '9 pump open'},
        10: {'spinbox': self.pump10_spinbox, 'suffix': '10 pump open'},
        }

        if self.slave_add in pump_info:
            pump_data = pump_info[self.slave_add]
            self.speed = int(int(pump_data['spinbox'].text()) * 140)
            self.first = pump_data['suffix']


        # 第一个泵的开启和命令展示
        pump_ever.pump_run(self.slave_add, 1, 1, self.speed)
        self.newline(self.first)

    # 点击开始第二种泵的停止
    def pump_stop_button(self, add):
        self.slave_add = add
        pump_info = {
        3: '3 pump stop',
        4: '4 pump stop',
        3: '5 pump stop',
        6: '6 pump stop',
        7: '7 pump stop',
        8: '8 pump stop',
        9: '9 pump stop',
        10: '10 pump stop',
        }

        if self.slave_add in pump_info:
            pump_data = pump_info[self.slave_add]
            self.pump_info = pump_data['suffix']


        # 第一个泵的开启和命令展示
        pump_ever.pump_run(self.slave_add, 1, 1, self.speed)
        self.newline(self.fpump_info)

    # 清除文本框内容
    def clear_result_text(self):
        self.display_text.clear()

    # 添加一行新的内容
    def newline(self, cmd):
        newline = f"{datetime.now().strftime('%H:%M:%S.%f')[:-3]}→{cmd}\n"
        self.display_text.append(newline)


class Swell(QThread, Ui_Form):

    def __init__(self) -> None:
        super().__init__()

    def run(self): 
        self.swell_frequence = int(self.swell_frequence.text())
        if self.swell_frequence == 0:
            self.swell_frequence = 3
        motor_module.swell(self.swell_frequence, 7, 200)


class Wash(QThread, Ui_Form):

    def __init__(self) -> None:
        super().__init__()

    def run(self): 
        self.wash_frequence = int(self.wash_frequence.text())
        if self.wash_frequence == 0:
            self.wash_frequence = 3
        for i in range(self.wash_frequence):
            motor_module.wash_ever(7, 200)     


class Depro_unit(QThread, Ui_Form):

    def __init__(self) -> None:
        super().__init__()

    def run(self):
        speeds = [60, 60, 60, 120, 200]
        volumes = [40, 70]
        motor_module.deprotect_unit4(3, speeds, volumes, True)


class Couple_unit(QThread, Ui_Form):
    
    def __init__(self) -> None:
        super().__init__()

    def run(self):
        speeds = [60, 60, 60, 120, 200]
        volumes = [40, 70]
        motor_module.couple_unit4(4, speeds, volumes, True)


class Great(QWidget):
    def __init__(self):
        super().__init__()
        self.slave_press = p.PressUnit()
        self.setWindowTitle('压力变化')
        self.setGeometry(100, 100, 640, 500)

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
        self.ax.set_ylim(0, 10)
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
        p1 = self.slave_press.data[3]
        p2 = self.slave_press.data[4]
        self.p1 = int(p1[:1])
        self.p2 = int(p2[:1]) + 2
        text1 = f"压力1: {self.p1} kpa"
        text2 = f"压力2: {self.p2} kpa"
        self.text1_label.setText(text1)
        self.text2_label.setText(text2)
        # self.data_x.pop(0)
        self.data_y1.pop(0)
        self.data_y2.pop(0)
        # 模拟实时数据，这里使用随机数
        self.data_y1.append(self.p1)
        self.data_y2.append(self.p2)
        self.line1.set_data(self.data_x, self.data_y1)
        self.line2.set_data(self.data_x, self.data_y2)
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()
    def presss_start(self, file_name, runtime):
        self.path = 'D:\\2 code\\Automation\\data\\230926\\'
        self.file = file_name
        if self.file is None:
            self.file = 'test'
        p.serOpen('com6')
        self.press_runtime = runtime
        self.slave_addb, self.slave_adde = 3, 4
        self.slave_adds = []
        if self.slave_adde != 0:
            for i in range(self.slave_addb, self.slave_adde+1):
                self.slave_adds.append(i)
        else:
            self.slave_adds = [self.slave_addb]
        self.slave_press.slaves(self.slave_adds, self.press_runtime, self.path, self.file)
        p.serClose()



def main():
    global b
    app = QApplication([])
    stats = Stats()
    stats.show()
    app.exec()


if __name__ == "__main__":

    main()
