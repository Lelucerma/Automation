import time

import serial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from datetime import datetime



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
            self.baudrate = {1200: 0, 2400: 1, 4800: 2, 9600: 3,
                             19200: 4, 38400: 5, 57600: 6,
                             115200: 7}
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


"""def main():

    global ser
    ser = serial.Serial('com5', 9600, timeout=1)

    # 数据位为8位
    ser.bytesize = serial.EIGHTBITS
    # 停止位为1位
    ser.stopbits = serial.STOPBITS_ONE
    # 无奇偶校验位
    ser.parity = serial.PARITY_NONE

    com = Pump_com()
    cmd = com.write_bits(4, '001', 0)
    print(cmd)
    ser.write(cmd)
    resp = ser.read(32)
    print(list(resp))
    cmd = com.write_registers(4, '009', 12345)
    print(cmd)
    ser.write(cmd)
    resp = ser.read(32)
    print(list(resp))

    # 关闭串口
    ser.close()

"""
class Stats:

    def __init__(self):
        self.connected = False

        # 从文件中加载UI定义
        qfile_stats = QFile("D:\\2code\\control-motor\\ui\\Kamor pump.ui")
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()

        self.ui = QUiLoader().load(qfile_stats)

        # 6、第一个泵的控制
        self.ui.pump1_open_button.clicked.connect(lambda: self.pump_open_button(2))
        self.ui.pump1_stop_button.clicked.connect(lambda: self.pump_stop_button(2))
        # 7、第二个泵的控制
        self.ui.pump2_open_button.clicked.connect(lambda: self.pump_open_button(3))
        self.ui.pump2_stop_button.clicked.connect(lambda: self.pump_stop_button(3))
        # 8、第三个泵的控制
        self.ui.pump3_open_button.clicked.connect(lambda: self.pump_open_button(4))
        self.ui.pump3_stop_button.clicked.connect(lambda: self.pump_stop_button(4))
        # 9、第四个泵的控制
        self.ui.pump4_open_button.clicked.connect(lambda: self.pump_open_button(5))
        self.ui.pump4_stop_button.clicked.connect(lambda: self.pump_stop_button(5))
        # 10、第五个泵的控制
        self.ui.pump5_open_button.clicked.connect(lambda: self.pump_open_button(6))
        self.ui.pump5_stop_button.clicked.connect(lambda: self.pump_stop_button(6))
        # 文本框清除按钮
        self.ui.clear_button.clicked.connect(self.clear_result_text)

    # 点击开始第一种泵的运转
    def pump_open_button(self, add):
        self.slave_add = add
        if self.slave_add == 2:
            self.speed = int(self.ui.pump1_spinbox.text()) * 100
        elif self.slave_add == 3:
            self.speed = int(self.ui.pump2_spinbox.text()) * 100
        elif self.slave_add == 4:
            self.speed = int(self.ui.pump3_spinbox.text()) * 100
        elif self.slave_add == 5:
            self.speed = int(self.ui.pump4_spinbox.text()) * 100
        elif self.slave_add == 6:
            self.speed = int(self.ui.pump5_spinbox.text()) * 100

        com = Pump_com()
        com.write_bits(self.slave_add, '001', 3)
        self.t1 = False
        if self.speed != 0:
            com.write_registers(self.slave_add, '009', self.speed)
            self.t1 = time.time()
        newline = f"{datetime.now().strftime('%H:%M:%S.%f')[:-3]}→'start'\n"
        self.ui.display_text.append(newline)

    # 点击开始第二种泵的停止
    def pump_stop_button(self, add):
        self.slave_add = add
        com = Pump_com()
        com.write_bits(self.slave_add, '001', 0)
        self.t2 = time.time()
        if self.t1:
            self.t = self.t2 - self.t1
            newline2 = f"总共运行时间为{self.t:.2f}s"
            self.ui.display_text.append(newline2)
        else:
            pass
        newline1 = f"{datetime.now().strftime('%H:%M:%S.%f')[:-3]}→'stop'\n"
        self.ui.display_text.append(newline1)


    # 清除文本框内容
    def clear_result_text(self):
        self.ui.display_text.clear()


def main():
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.exec()


if __name__ == "__main__":
    main()
