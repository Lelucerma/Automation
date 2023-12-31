import os.path
import threading
import serial
import time
from PySide6.QtWidgets import QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import numpy as np

global b
b = {}


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
        self.data[self.slave_add] = self.press_tranW
        self.datas.append(self.data)
        # print(self.data)
        try:
            b = self.data
        except (TypeError):
            pass


def data_tran(a):
    b = a


class Pre_ui(QWidget):
    def __init__(self):
        super().__init__()
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
        self.ax.set_ylim(0, 100)
        self.line1, = self.ax.plot([], [])
        self.line2, = self.ax.plot([], [])

        self.data_x = np.arange(10)
        self.data_y1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.data_y2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # 1秒钟更新一次图表

    def update_plot(self):
        # 这里可以替换为你自己的文本数据生成逻辑
        # print(self.slaves.data)
        p1 = random.randint(1, 100)
        p2 = random.randint(1, 100)
        print(b)
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

    def data(self, a):
        print(a)


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


def main():
    slave_press = PressUnit()
    file_name = 'D:\\2 code\\Automation\\data\\230801\\1.txt'
    slave_press.slaves('com6', 1, 10,
                       file_name)  # slave_add从第二个开始使用，保留第一个的从机地址
    print(1)


# if __name__ == "__main__":
#     t1 = time.time()
#     main()
#     t2 = time.time()
#     print((t2 - t1) / 60)
