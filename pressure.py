import os.path
import threading
import serial
import time
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout
from PyQt5.QtCore import QTimer,pyqtSignal
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import sys
import numpy as np
from ui.Kamor_pump_ui import Ui_Form

import matplotlib
matplotlib.use("agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# 生成命令
class PressCom():
    """dict_press_func = {'000': '获取丛机地址', '001':'获取波特率',
                  '002':'获取单位', '003':'获取小数位数',
                  '004':'获取输出值', '005':'获取量程零点',
                  '006':'获取量程满点', '009':'获取仪表状态',
                  '010':'获取校验位范围', '012':'获取零位偏移值',
                  '013':'获取滤波系数', '014':'获取增益系数',
                  '100':'改变丛机地址', '101':'改变波特率',
                  '112':'改变零位偏移值', '113':'改变滤波系数',
                  '114':'改变增益系数', '115':'保存改变功能',
                  '116':'零点清零',  '117':'回复出厂设置'}
    """

    # 定义初始值
    def __init__(self) -> None:
        pass

    # crc循环校验
    def crc16(self, data):
        """
        传入需要校验的指令值，我们对这个指令进行校验并返回校验后含crc校验码的指令代码
        Args:
            data: 传入需要校验的数据值，对这个指令进行crc校验。
        """
        self.crc = 0xFFFF
        self.polynomial = 0xA001
        self.data = data

        for byte in data:
            self.crc ^= byte
            for _ in range(8):
                if self.crc & 0x0001:
                    self.crc = (self.crc >> 1) ^ self.polynomial
                else:
                    self.crc >>= 1

        self.crc_bytes = self.crc.to_bytes(2, byteorder='little')
        self.data += list(self.crc_bytes)
        return data

    # 读取相关功能函数
    def read(self, slave_add, func):
        """
        读取一个具体的数值，通过具体的功能码实现读取不同的东西。
        :param slave_add: 从机地址
        :param func: 功能码
        :return: 返回一个命令值
        """
        self.slave_add = [slave_add]
        self.func_read = int(func[1:])
        self.func = [0x03]
        self.addh = [0x00]
        self.addl = [self.func_read]
        self.datah = [0x00]
        self.datal = [0x01]
        self.cmd = self.slave_add + self.func + self.addh + self.addl
        self.cmd = self.cmd + self.datah + self.datal
        self.cmd = self.crc16(self.cmd)
        return self.cmd

    # 写入相关功能函数
    def write(self, slave_add, func, data):
        """
        通过写入一个数据改变数据的数值，改变相应的功能。
        :param slave_add: 从机地址
        :param func: 功能码，与写入的数据值一起之后再确定
        :param data: 写入的数据值，这个数据需要待定，等到时候在验证与改变
        :return:返回的相应的命令
        """
        self.slave_add = slave_add
        self.func_read = int(func[1:])
        self.datal = [int(data)]
        if self.func_read == 16:
            self.func_read = 15
            self.datal = [0x55]
        if self.func_read == 17:
            self.func_read = 15
            self.datal = [0xAA]
        self.func = [0x05]
        self.addh = [0x00]
        self.addl = [self.func_read]
        self.datah = [0x00]
        self.cmd = self.slave_add + self.func + self.addh + self.addl
        self.cmd = self.cmd + self.datah + self.datal
        self.cmd = self.crc16(self.cmd)
        return self.cmd


class PressGet():
    def __init__(self):
        self.cm = PressCom()

    def press_uint(self, slave_add):
        # 确定这个仪器返回数值的单位是什么
        self.unit = self.cm.read(slave_add, '002')
        ser_press.write(self.unit)
        resp = ser_press.read(32)
        self.unit_resp = list(resp)[4]

        # 确定一个这个仪器的返回的数值后面有几位小数
        self.demical = self.cm.read(slave_add, '003')
        ser_press.write(self.demical)
        resp = ser_press.read(32)
        self.demiacal_resp = list(resp)[4]
        return self.unit_resp

    def read_pressure(self, slave_add):
        # 获取压力的数值
        self.press_cmd = self.cm.read(slave_add, '004')
        # print(self.press_cmd)
        ser_press.write(self.press_cmd)
        resp = ser_press.read(32)
        # print(resp)
        self.pressure_resp = list(resp)[3:5]
        return self.pressure_resp

    def trans(self, ever_data):
        """
        通过将返回的数据值转换成二进制，通过对提取出来的两个数字转换成二进制，
        然后通过将两个二进制的数据进行拼接，在将其转换成一个有效的数字，并将这个数字转换成有效的位数。

        :param ever_data: 这个是经过提取过的数据，只有8个字节
        :return:返回的是一个确定的压力数值
        """
        # 给与一个初始值，将这个初始值进行转换
        self.bins = bin(0)
        for i in self.pressure_resp:
            # 除去二进制数中的开头
            self.bins = self.bins[:-1]
            # 转换成二进制的数值
            self.ps = bin(i)
            self.ps = self.ps[2:]
            self.bins += self.ps
        self.press = int(self.bins, 2) / (10**self.demiacal_resp)
        return self.press


class DataSave():
    def save(self, data, file_name):
        """
        通过将获得的数据值存入具体的文件内
        :param data: 需要写入的具体的数值
        :param file_name: 需要将文件保存的位置，以及具体的文件名
        :param unit: 传入的压力的单位的数值
        :return:
        """
        self.data = data
        file_a = open(file_name, 'a+')
        self.num = 1
        for key in self.data:
            file_a.write(f'{self.num}: {key}\n')
            self.num += 1
        file_a.close()


class PressUnit():
    dataEmit = pyqtSignal() #创建槽信号

    def __init__(self) -> None:

        self.time2 = 0
        self.save1 = DataSave()
        self.c1 = PressGet()
        self.slave_adds = []
        self.data = {3: '0kpa', 4: "0kpa"}
        self.unit_data = {}
        self.units = {
            0: 'Mpa',
            1: 'Kpa',
            2: 'Pa',
            3: 'Bar',
            4: 'mbar',
            5: 'kg/cm3',
            6: 'Psi',
            7: 'mh2',
            8: 'mmh2'
        }

        pass

    def slaves(self, slave_adds, runtime, floder_path, file_name_tran):
        # 开始时间
        self.time_starts = time.time()
        self.slave_adds = slave_adds
        self.runtime = runtime
        self.datas = []
        for ever_slave in self.slave_adds:
            self.unit = self.c1.press_uint(int(ever_slave))
            self.unit_data[ever_slave] = self.units[self.unit]
        while True:
            for ever_slave in slave_adds:
                self.press_thread = threading.Thread(
                    target=self.slaveWrite,
                    kwargs={'slave_add': f'{ever_slave}'})
                self.press_thread.start()
                self.press_thread.join()
                # self.data
            if self.time2 > self.runtime:
                break
            self.time2 = time.time() - self.time_starts
        floder = os.path.exists(floder_path)
        if not floder:
            os.mkdir(floder_path)
        self.file_name = floder_path + '\\' + file_name_tran + '.txt'
        self.save1.save(self.datas, self.file_name)
        # print(f"结束了，时间为：{time.time()-self.time_starts}")

    def slaveWrite(self, slave_add):
        """"
        就是数据写入与读取
        """
        self.slave_add = int(slave_add)
        self.press_true = self.c1.read_pressure(self.slave_add)
        self.press_tran = str(self.c1.trans(self.press_true))
        self.press_tran += self.unit_data[self.slave_add]
        self.data[self.slave_add] = self.press_tran
        self.datas.append(self.data)
        self.data = random.randint(0, 100)
        # print(self.data)
        self.dataEmit.emit(self.data)


# 创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    def __init__(self,width=5, height=4, dpi=100):
        # 第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # 第二步：在父类中激活Figure窗口
        super(MyFigure,self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)
        self.pr = PressUnit()
        self.pr.dataEmit.connect()
        
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
        self.x = [1,2,3,4,5,6,7,8,9,10]
        self.y = [0,0,0,0,0,0,0,0,0,0]
        self.axes.plot(self.x, self.y)
        self.fig.suptitle("uv")  # 设置标题
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(100)  # 1秒钟更新一次图表

    def update_plot(self, data):
        self.p = data
        self.y.pop(0)
        self.mat_plot_drow_axes(self.x, self.y)


class MainDialogImgBW(QDialog, Ui_Form):
    def __init__(self):
        super(MainDialogImgBW,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("显示matplotlib绘制图形")
        self.setMinimumSize(0,0)

        # 第五步：定义MyFigure类的一个实例
        self.F = MyFigure(width=3, height=2, dpi=100)
        self.F.plotcos()
        self.gridlayout = QGridLayout(self.groupBox)  # 继承容器groupBox
        self.gridlayout.addWidget(self.F,0,1)


    def plotcos(self):
        self.t = np.arange(100)
        self.s = np.random.random(100)
        self.F.fig.suptitle("sin")  # 设置标题
        self.F.mat_plot_drow_axes(self.t, self.s)
        

def serOpen(compress):
    global ser_press
    ser_press = serial.Serial(compress, 9600, timeout=1)

    # 数据位为8位
    ser_press.bytesize = serial.EIGHTBITS
    # 停止位为1位
    ser_press.stopbits = serial.STOPBITS_ONE
    # 无奇偶校验位
    ser_press.parity = serial.PARITY_NONE


def serClose():
    # 关闭串口
    ser_press.close()


# def main():
#     slave_press = PressUnit()
#     file_name = 'D:\\2 code\\Automation\\data\\230801\\1.txt'
#     slave_press.slaves('com6', 1, 10,
#                        file_name)  # slave_add从第二个开始使用，保留第一个的从机地址
#     print(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainDialogImgBW()
    main.show()
    #app.installEventFilter(main)
    sys.exit(app.exec())