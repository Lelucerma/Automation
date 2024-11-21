import time
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from datetime import datetime
import serial


# 泵的命令行组成
class Pump_com():
    """dict_func_bit = {'001': '启停控制', '002':'电机方向',
                  '003':'运行模式', '004':'FLASH保存',
                  '005':'恢复默认值'}
        dict_func_register = {'001': '通讯地址', '002':'获取波特率',
                  '003':'细分单位', '004':'电位器最大速度',
                  '006':'错误码', '007':'起始速度',
                  '009':'目标速度', '011':'加速度',
                  '013':'减速度', '015':'目标位置增量'}
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
    def read_bit(self, slave_add, func):
        """
        读取一个具体的数值，通过具体的功能码实现读取不同的东西。
        :param slave_add: 从机地址
        :param func: 功能码
        :return: 返回一个命令值
        """
        self.slave_add = [slave_add]
        self.func_bit = int(func[1:])
        self.func = [5]
        self.addh = [10]
        self.addl = [self.func_bit]
        self.datah = [0]
        self.datal = [1]
        self.cmd = self.slave_add + self.func + self.addh + self.addl
        self.cmd = self.cmd + self.datah + self.datal
        self.cmd = self.crc16(self.cmd)
        return self.cmd

    # 写入相关功能函数
    def write_bit(self, slave_add, func, data):
        """
        通过写入一个数据改变数据的数值，改变相应的功能。
        :param slave_add: 从机地址
        :param func: 功能码，与写入的数据值一起之后再确定
        :param data: 写入的数据值，这个数据需要待定，等到时候在验证与改变
        :return:返回的相应的命令
        """
        self.slave_add = [slave_add]
        self.func_bit = int(func[1:])
        self.datah = [data]
        self.func = [5]
        self.addh = [0]
        self.addl = [self.func_bit]
        self.datal = [0]
        self.cmd = self.slave_add + self.func + self.addh + self.addl
        self.cmd = self.cmd + self.datah + self.datal
        self.cmd = self.crc16(self.cmd)
        return self.cmd

    # 需调整
    def write_bits(self, slave_add, func, data):
        """
        通过写入一个数据改变数据的数值，改变相应的功能。
        :param slave_add: 从机地址
        :param func: 功能码，与写入的数据值一起之后再确定
        :param data: 写入的数据值，这个数据需要待定，等到时候在验证与改变
        :return:返回的相应的命令
        """
        self.slave_add = [slave_add]
        self.func_bit = int(func[1:])
        self.func = [15]
        self.addh = [0]
        self.addl = [1]
        self.datalenth = [0, 2]
        self.data_byte = [1]
        self.data = [data]
        self.cmd = self.slave_add + self.func + self.addh + self.addl
        self.cmd = self.cmd + self.datalenth + self.data_byte + self.data
        self.cmd = self.crc16(self.cmd)
        return self.cmd

    def read_register(self, slave_add, func, data):
        """
        通过写入一个数据改变数据的数值，改变相应的功能。
        :param slave_add: 从机地址
        :param func: 功能码，与写入的数据值一起之后再确定
        :param data: 写入的数据值，这个数据需要待定，等到时候在验证与改变
        :return:返回的相应的命令
        """
        self.slave_add = [slave_add]
        self.func_read = int(func[1:])
        self.datah = [data]
        self.func = [5]
        self.addh = [0x00]
        self.addl = [self.func_register]
        self.datah = [0x00]
        self.cmd = self.slave_add + self.func + self.addh + self.addl
        self.cmd = self.cmd + self.datah + self.datal
        self.cmd = self.crc16(self.cmd)
        return self.cmd

    def write_register(self, slave_add, func, data):
        """
        通过写入一个数据改变数据的数值，改变相应的功能。
        :param slave_add: 从机地址
        :param func: 功能码，与写入的数据值一起之后再确定
        :param data: 写入的数据值，这个数据需要待定，等到时候在验证与改变
        :return:返回的相应的命令
        """
        self.slave_add = [slave_add]
        self.data = data
        self.func_register = int(func[1:])
        self.func = [6]
        self.addh = [0]
        self.addl = [self.func_register]
        self.datah = [0]
        self.function()
        self.cmd = self.slave_add + self.func + self.addh + self.addl
        self.cmd = self.cmd + self.datal + self.datah
        self.cmd = self.crc16(self.cmd)
        return self.cmd

    def write_registers(self, slave_add, func, data):
        """
        通过写入一个数据改变数据的数值，改变相应的功能。
        :param slave_add: 从机地址
        :param func: 功能码，与写入的数据值一起之后再确定
        :param data: 写入的数据值，这个数据需要待定，等到时候在验证与改变
        :return:返回的相应的命令
        """
        self.slave_add = [slave_add]
        self.data = data
        self.func_register = int(func[1:])
        self.func = [16]
        self.addh = [64]
        self.addl = [self.func_register]
        self.datah = [0]
        self.data_lenthh = [0]
        self.data_lenthl = [2]
        self.data_byte = [4]
        self.function()
        self.cmd = self.slave_add + self.func + self.addh + self.addl
        self.cmd = self.cmd + self.data_lenthh + self.data_lenthl
        self.cmd = self.cmd + self.data_byte + self.datah + self.datal
        self.cmd = self.crc16(self.cmd)
        return self.cmd

    # 保持寄存器的功能函数
    def function(self):
        if self.func_register == 1:
            self.datal = [self.data]
        elif self.func_register == 2:
            self.baudrate = {
                1200: 0,
                2400: 1,
                4800: 2,
                9600: 3,
                19200: 4,
                38400: 5,
                57600: 6,
                115200: 7
            }
            self.datal = [self.baudrate[self.data]]
        elif self.func_register == 3:
            self.datal = [self.data]
        elif self.func_register == 4:
            self.trans()
        elif self.func_register == 6:
            self.datal = [0]
        elif 7 <= self.func_register <= 13:
            self.trans()
        else:
            self.datal = [0]

    # 将速度值转换成命令行
    def trans(self):
        # 转换陈十六进制的数据
        self.data = hex(self.data)
        # 数据高位为0，因为没有超过这个限制
        self.datah = [0, 0]
        # 数据低位为上述转换后的数据，通过提取和转换成十进制的数据
        if len(self.data) > 4:
            self.datal = [int(self.data[2:4], 16), int(self.data[4:6], 16)]
        else:
            self.datal = [0, int(self.data[2:4], 16)]


# 泵的具体运转
class Pump():
    # 初始化操作
    def __init__(self) -> None:

        self.cm = Pump_com()

    # 开启泵的运行
    def pump_run(self, slave_add, run, direction, speed=None):
        """"
        设计泵的开启，分别传入三个参数对泵的初始值进行设置

        Args:
            * slave_add:蠕动泵的地址
            * run:泵的运行状态
            * direction:泵的运行方向
            * speed:泵的运行速度

        """
        self.run = run  # 启动电机数值
        self.motor_direction = direction  # 电机方向,0为为顺时针，1为逆时针
        if speed is None:
            self.run_speed = 0
        else:
            self.run_speed = speed

        if self.run:
            if self.motor_direction:
                self.data = 3
            else:
                self.data = 2
        else:
            self.data = 0
        self.begin_cmd = self.cm.write_bits(slave_add, '001', self.data)
        self.time1 = time.time()
        while True:
            self.time2 = time.time()
            ser.write(self.begin_cmd)
            self.resp1 = list(ser.read(32))
            if self.resp1 != []:
                break
            self.time = self.time2 - self.time1
            if self.time > 10:
                break
        if run and self.run_speed:
            self.speed_cmd = self.cm.write_registers(slave_add, '009',
                                                     self.run_speed)
            self.time1 = time.time()
            while True:
                self.time2 = time.time()
                ser.write(self.speed_cmd)
                self.resp2 = list(ser.read(32))
                if self.resp2 != []:
                    break
                # 加一个时间的报错
                if self.time > 10:
                    break
            return self.begin_cmd, self.resp1, self.speed_cmd, self.resp2
        return self.begin_cmd, self.resp1

    def run_time(self, volume):
        """"
        根据泵的速度和需要进液的容量确定泵的运行时间，需要设置一定的时间冗余，
        对于泵停止所需要的时间需要进行相应的调整。需做出一个统计
        Args:
            * direction 泵的运行方向
            * speed 泵的运行速度

        """

        self.volume = volume  # 需要进液的体积
        self.time_tube = 0  # 从泵开启在管道中运输过程中所需要的时间
        self.redundancy = 0  # 泵的运行冗余时间
        # print(self.volume / self.flow_rate())
        self.time1 = self.time_tube + (self.volume /
                                       self.flow_rate()) + self.redundancy
        return self.time1

    # 流量矫正
    def flow_rate(self):
        """"
        对速度值进行相应的矫正，返回一个具体的流量数值
        目前只是一个粗略的设置，需要通过实验进行相应的速度矫正模块
        """
        self.rate = self.run_speed / 5000
        return self.rate


class Stats:
    def __init__(self):

        global ser
        ser = serial.Serial('com5', 9600, timeout=1)

        # 数据位为8位
        ser.bytesize = serial.EIGHTBITS
        # 停止位为1位
        ser.stopbits = serial.STOPBITS_ONE
        # 无奇偶校验位
        ser.parity = serial.PARITY_NONE

        self.pump_ever = Pump()

        # 从文件中加载UI定义
        qfile_stats = QFile("D:\\2 code\\Automation\\ui\\Kamor pump.ui")
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()

        self.ui = QUiLoader().load(qfile_stats)

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
        # 文本框清除按钮
        self.ui.clear_button.clicked.connect(self.clear_result_text)

    # 点击开始第一种泵的运转
    def pump_open_button(self, add):
        self.slave_add = add
        if self.slave_add == 3:
            self.speed = int(int(self.ui.pump3_spinbox.text()) * 140)
            self.time3 = time.time()
            self.first = '3 pump open'
        elif self.slave_add == 4:
            self.speed = int(int(self.ui.pump4_spinbox.text()) * 140)
            self.time4 = time.time()
            self.first = '4 pump open'
        elif self.slave_add == 5:
            self.speed = int(int(self.ui.pump5_spinbox.text()) * 140)
            self.time5 = time.time()
            self.first = '5 pump open'
        elif self.slave_add == 6:
            self.speed = int(int(self.ui.pump6_spinbox.text()) * 140)
            self.time6 = time.time()
            self.first = '6 pump open'
            self.newline(self.speed)
        elif self.slave_add == 7:
            self.speed = int(int(self.ui.pump7_spinbox.text()) * 140)
            self.time7 = time.time()
            self.first = '7 pump open'
            self.newline(self.speed)
        elif self.slave_add == 8:
            self.speed = int(int(self.ui.pump8_spinbox.text()) * 140)
            self.time8 = time.time()
            self.first = '8 pump open'
            self.newline(self.speed)
        elif self.slave_add == 9:
            self.speed = int(int(self.ui.pump9_spinbox.text()) * 140)
            self.time9 = time.time()
            self.first = '9 pump open'
            self.newline(self.speed)
        elif self.slave_add == 10:
            self.speed = int(int(self.ui.pump10_spinbox.text()) * 140)
            self.time10 = time.time()
            self.first = '10 pump open'
            self.newline(self.speed)
        elif self.slave_add == 11:
            self.speed = int(int(self.ui.pump11_spinbox.text()) * 140)
            self.time11 = time.time()
            self.first = '11 pump open'
            self.newline(self.speed)

        # 第一个泵的开启和命令展示
        self.pump_ever.pump_run(self.slave_add, 1, 1, self.speed)
        self.newline(self.first)
        # self.newline(self.cmd1)
        # self.newline(self.cmd2)
        # self.newline(self.cmd1)
        # self.newline(self.cmd2)
        # self.newline(self.cmd3)
        # self.newline(self.cmd4)
        """# 第二个泵的开启和命令展示
        if self.speed == 0:
            self.cmd1, self.cmd2 = self.pump_ever.pump_run(
                self.slave_add+1, 1, 1, self.speed)
            self.newline(self.second)
            self.newline(self.cmd1)
            self.newline(self.cmd2)
        else:
            self.cmd1, self.cmd2,
            self.cmd3, self.cmd4, = self.pump_ever.pump_run(
                self.slave_add+1, 1, 1, self.speed)
            self.newline(self.second)
            self.newline(self.cmd1)
            self.newline(self.cmd2)
            self.newline(self.cmd3)
            self.newline(self.cmd4)
            """

    # 点击开始第二种泵的停止
    def pump_stop_button(self, add):
        self.slave_add = add
        if self.slave_add == 3:
            self.time303 = time.time()
            self.first = '3 pump stop'
            self.newline(self.time303 - self.time3)
        elif self.slave_add == 4:
            self.time304 = time.time()
            self.first = '4 pump stop'
            self.newline(self.time304 - self.time4)
        elif self.slave_add == 5:
            self.time305 = time.time()
            self.first = '5 pump stop'
            self.newline(self.time305 - self.time5)
        elif self.slave_add == 6:
            self.time306 = time.time()
            self.first = '6 pump stop'
            self.newline(self.time306 - self.time6)
        elif self.slave_add == 7:
            self.time307 = time.time()
            self.first = '7 pump stop'
            self.newline(self.time307 - self.time7)
        elif self.slave_add == 8:
            self.time308 = time.time()
            self.first = '8 pump stop'
            self.newline(self.time308 - self.time8)
        elif self.slave_add == 9:
            self.time309 = time.time()
            self.first = '9 pump stop'
            self.newline(self.time309 - self.time9)
        elif self.slave_add == 10:
            self.time310 = time.time()
            self.first = '10 pump stop'
            self.newline(self.time310 - self.time10)
        elif self.slave_add == 11:
            self.time311 = time.time()
            self.first = '11 pump stop'
            self.newline(self.time311 - self.time11)
        # self.first = 'first pump stop'
        # self.second = 'second pump stop'
        self.newline(self.first)
        self.pump_ever.pump_run(self.slave_add, 0, 0)
        # self.newline(self.cmd1)
        # self.newline(self.cmd2)
        """self.cmd1, self.cmd2 = self.pump_ever.pump_run(
            self.slave_add + 1, 0, 0)
        self.newline(self.second)
        self.newline(self.cmd1)
        self.newline(self.cmd2)"""

    # 清除文本框内容
    def clear_result_text(self):
        self.ui.display_text.clear()

    def newline(self, cmd):
        newline = f"{datetime.now().strftime('%H:%M:%S.%f')[:-3]}→{cmd}\n"
        self.ui.display_text.append(newline)


# def main():
#     app = QApplication([])
#     stats = Stats()
#     stats.ui.show()
#     app.exec()

# if __name__ == "__main__":

#     main()
