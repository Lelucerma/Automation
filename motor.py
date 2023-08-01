import math
import time
import serial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from datetime import datetime
import threading
import pressure as p
import analysis


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
        self.begin = True

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
            # 将数值调整成相应的电机转速数值，根据实际测试，约为140，采用140作为冗余
            self.run_speed = speed * 140


        if self.run:
            if self.motor_direction:
                self.data = 3
            else:
                self.data = 2
        else:
            self.data = 0
        # print(self.data)
        self.begin_cmd = self.cm.write_bits(slave_add, '001', self.data)
        # print(self.begin_cmd)
        self.resp1 = self.answer(self.begin_cmd)

        # print(self.resp1)
        if run and self.run_speed:
            self.speed_cmd = self.cm.write_registers(slave_add, '009',
                                                     self.run_speed)
            # print(self.speed_cmd)
            self.resp2 = self.answer(self.speed_cmd)
            # print(self.resp2)



    def speed_change(self, slave_add):
        self.speed_change_cmd = self.cm.write_registers(slave_add, '009',
                                                 self.run_speed)
        # print(self.speed_cmd)
        self.resp3 = self.answer(self.speed_change_cmd)
        # print(self.resp3)

    def answer(self, cmd):
        self.cmd = cmd
        t = 0
        ser_pump.write(self.cmd)
        try:
            self.resp = list(ser_pump.read(32))
            return self.resp
        except:
            return 0


        # while True:
        #     ser_pump.write(self.cmd)
        #     self.resp = list(ser_pump.read(32))
        #     if self.resp != []:
        #         return self.resp
        #     if t > 10:
        #         return '无法通信，请查找问题'
        #     t += 1




    # 流量矫正


# 一个单元泵的运行
class Module():
    def __init__(self) -> None:

        self.pump_ever = Pump()




    def reactor_unit(self, slave_add1, speed, volume):
        """"
        对于反应器的蠕动泵进行相应的控制，超过控制时间后蠕动泵停止工作
        首个反应单元有两个蠕动泵，因此有两个设备地址。

        Args:
            * slave_add1 第一个泵
            * slave_add2 第二个泵
            * speed 泵的运行速度

        """
        self.slave_add1, self.slave_add2 = slave_add1, slave_add1+1
        self.slave_add3, self.slave_add4 = slave_add1+2, slave_add1+3
        self.speed1, self.speed2 = speed[0], speed[1]
        self.speed3, self.speed4 = speed[2], speed[3]
        

        # 进行各个时间的计算程序
        self.run_time()

        # 这个时间是主物料开始到洗涤单元的时间（应该以数值的进度作为判断）
        self.time1 = self.pump1_intime + self.pump1_outtime
        + self.reactor_intime + self.reactor_outtime + self.reactor_time

        # 这个时间是副物料开始到洗涤单元的时间（应该以数值的进度作为判断）
        self.time2 = self.pump1_intime + self.pump1_outtime
        + self.reactor_intime + self.reactor_outtime + self.reactor_time

        # 这个应该是洗涤泵到洗涤单元的时间
        self.time3 = self.pump3_intime + self.pump3_outtime

        # 第三个泵的开启时间为time1-time3
        self.time4 = self.time1 - self.time3

        # 开始计时
        self.time_starts = time.time()  # 这个是总计时，不能更改
        self.time_start = time.time()  # 这个是可以作为部分计时，可以更改

        # 判断哪一个运行时间长，先开启哪一个泵
        if self.time4 >= 0:
            self.pump_ever.pump_run(self.slave_add1, 1, 1, self.speed1)
            self.pump_ever.pump_run(self.slave_add2, 1, 1, self.speed2)
            time.sleep(self.time4)
            # if (time.time() - self.time_start) >= self.time4:
            # print('1')
            self.pump_ever.pump_run(self.slave_add3, 1, 1, self.speed3)                
        else:
            self.pump_ever.pump_run(self.slave_add3, 1, 1, self.speed3)            
            time.sleep(-self.time4)
            # if (time.time() - self.time_start) > (-self.time4):
            # print('2')
            self.pump_ever.pump_run(self.slave_add1, 1, 1, self.speed1)
            self.pump_ever.pump_run(self.slave_add2, 1, 1, self.speed2)
        
        # 当物料进入洗涤单元时，开启洗涤单元废料泵
        # time.sleep(self.time1-self.time4-8) # 3是冗余时间
        self.pump_ever.pump_run(self.slave_add4, 1, 1, self.speed4)

        time.sleep(10) # 3是冗余时间
        
        # 计算各个泵需要的运行时间
        self.pump1_runtime = self.volume_time(volume[0], self.speed1) + self.time1
        self.pump2_runtime = self.volume_time(volume[1], self.speed2) + self.time2
        self.pump3_runtime = self.volume_time(volume[2], self.speed3) + self.time2

        # 等物料输入结束后，关闭各个泵
        time.sleep(self.pump1_runtime)
        # if (time.time() - self.time_start) > (self.pump1_runtime):
        #     print('3')
        self.pump_ever.pump_run(self.slave_add1, 0, 0)
        self.pump_ever.pump_run(self.slave_add2, 0, 0)
        time.sleep(self.pump3_runtime - 10)
        self.pump_ever.pump_run(self.slave_add4, 0, 0)
        time.sleep(10)
        # if (time.time() - self.time_start) > (self.pump3_runtime):
        # print('4')
        self.pump_ever.pump_run(self.slave_add3, 0, 0)


    def wash_unit(self, slave_add1, speed1, slave_add2, speed2):
        """"
        对于洗涤的蠕动泵进行相应的控制，超过控制时间后蠕动泵停止工作
        每个洗涤单元有两个蠕动泵，有两个设备地址。

        Args:
            * slave_add1 第一个泵
            * slave_add2 第二个泵
            * speed 泵的运行速度D

        """
        self.time_starts = time.time()
        self.time_start = time.time()
        self.time2 = 0
        self.pump_ever = Pump()
        self.pump_ever.pump_run(slave_add1, True, True, speed1)
        self.pump_ever.pump_run(slave_add2, True, True, speed2)
        # print(self.pump_ever.run_time(20))
        # time.sleep(self.pump_ever.run_time(20))
        self.pump_ever.pump_run(slave_add1, False, False, speed1)
        self.pump_ever.pump_run(slave_add2, False, False, speed2)

    def tube_time(self, length, speed, diameter=0.5):

        """"
        根据泵的速度和需要进液的容量确定泵的运行时间，需要设置一定的时间冗余，
        对于泵停止所需要的时间需要进行相应的调整。需做出一个统计
        Args:
            * direction 泵的运行方向
            * speed 泵的运行速度

        """

        self.length = length  # 管道的长度
        # self.diameter = diameter   # 管道的直径
        # self.speed = speed
        # self.tube_volume = self.length * \
        #                    math.pow((self.diameter/4), 2) * math.pi
        self.tube_time1 = self.length * 0.23
        return self.tube_time1

    def run_time(self):
        """"
        对速度值进行相应的矫正，返回一个具体的流量数值
        目前只是一个粗略的设置，需要通过实验进行相应的速度矫正模块
        """
        self.pump1_intime = self.tube_time(46, self.speed1)
        self.pump1_outtime = self.tube_time(23, self.speed1)
        self.pump2_intime = self.tube_time(46, self.speed2)
        self.pump2_outtime = self.tube_time(23, self.speed2)
        self.pump3_intime = self.tube_time(56, self.speed3)
        self.pump3_outtime = self.tube_time(70, self.speed3)
        self.pump4_intime = self.tube_time(67, self.speed4)
        self.pump4_outtime = self.tube_time(40, self.speed4)
        self.reactor_intime = self.tube_time(10,self.speed2)
        self.reactor_outtime = self.tube_time(56, self.speed2)
        self.reactor_time = self.tube_time(30, self.speed2)

    def volume_time(self, volume, speed):
        self.volume = volume
        self.speed = speed
        self.pump_runtime = (self.volume / self.speed)*60 + 10
        # print(f'体积为:{self.volume}, 速度为：{self.speed},时间为：{self.pump_runtime}')
        return self.pump_runtime

class Stats:

    def __init__(self):

        self.pump_ever = Pump()

        # 从文件中加载UI定义
        qfile_stats = QFile("D:\\2 code\\control-motor\\ui\\Kamor pump.ui")
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()

        self.ui = QUiLoader().load(qfile_stats)

        # 6、第一个泵的控制
        self.ui.pump1_open_button.clicked.connect(
            lambda: self.pump_open_button(3))
        self.ui.pump1_stop_button.clicked.connect(
            lambda: self.pump_stop_button(3))
        # 7、第二个泵的控制
        self.ui.pump2_open_button.clicked.connect(
            lambda: self.pump_open_button(4))
        self.ui.pump2_stop_button.clicked.connect(
            lambda: self.pump_stop_button(4))
        # 8、第三个泵的控制
        self.ui.pump3_open_button.clicked.connect(
            lambda: self.pump_open_button(5))
        self.ui.pump3_stop_button.clicked.connect(
            lambda: self.pump_stop_button(5))
        # 9、第四个泵的控制
        self.ui.pump4_open_button.clicked.connect(
            lambda: self.pump_open_button(6))
        self.ui.pump4_stop_button.clicked.connect(
            lambda: self.pump_stop_button(6))
        # 10、第五个泵的控制
        self.ui.pump5_open_button.clicked.connect(
            lambda: self.pump_open_button(6))
        self.ui.pump5_stop_button.clicked.connect(
            lambda: self.pump_stop_button(6))
        # 文本框清除按钮
        self.ui.clear_button.clicked.connect(self.clear_result_text)

    # 点击开始第一种泵的运转
    def pump_open_button(self, add):
        self.slave_add = add
        if self.slave_add == 3:
            self.speed = int(int(self.ui.pump1_spinbox.text()) * 140)
            self.time1 = time.time()
            self.first = '3 pump open'
        elif self.slave_add == 4:
            self.speed = int(int(self.ui.pump2_spinbox.text()) * 140)
            self.time2 = time.time()
            self.first = '4 pump open'
        elif self.slave_add == 5:
            self.speed = int(int(self.ui.pump3_spinbox.text()) * 140)
            self.time3 = time.time()
            self.first = '5 pump open'
        elif self.slave_add == 6:
            self.speed = int(int(self.ui.pump4_spinbox.text()) * 140)
            self.time4 = time.time()
            self.first = '6 pump open'
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
            self.cmd1, self.cmd2, self.cmd3, self.cmd4, = self.pump_ever.pump_run(
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
            self.time5 = time.time()
            self.first = '3 pump stop'
            self.newline(self.time5-self.time1)
        elif self.slave_add == 4:
            self.time6 = time.time()
            self.first = '4 pump stop'
            self.newline(self.time6-self.time2)
        elif self.slave_add == 5:
            self.time7 = time.time()
            self.first = '5 pump stop'
            self.newline(self.time7-self.time3)
        elif self.slave_add == 6:
            self.time8 = time.time()
            self.first = '6 pump stop'
            self.newline(self.time8-self.time4)
        # self.first = 'first pump stop'
        # self.second = 'second pump stop'
        self.newline(self.first)
        self.pump_ever.pump_run(self.slave_add, 0, 0)
        # self.newline(self.cmd1)
        # self.newline(self.cmd2)


        """self.cmd1, self.cmd2 = self.pump_ever.pump_run(self.slave_add + 1, 0,
                                                       0)
        self.newline(self.second)
        self.newline(self.cmd1)
        self.newline(self.cmd2)"""

    # 清除文本框内容
    def clear_result_text(self):
        self.ui.display_text.clear()

    def newline(self, cmd):
        newline = f"{datetime.now().strftime('%H:%M:%S.%f')[:-3]}→{cmd}\n"
        self.ui.display_text.append(newline)


def pump_ui():
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.exec()

def pump_automation(com_pump):
    t1 = time.time()
    global ser_pump
    ser_pump = serial.Serial(com_pump, 9600, timeout=1)

    # 数据位为8位
    ser_pump.bytesize = serial.EIGHTBITS
    # 停止位为1位
    ser_pump.stopbits = serial.STOPBITS_ONE
    # 无奇偶校验位
    ser_pump.parity = serial.PARITY_NONE

    c = Module()
    speeds = []
    speed = input("请输入速度值：").split(',')
    for i in speed:
        speeds.append(int(i))
    volumes = []
    volume = input("请输入体积值：").split(',')
    for i in volume:
        volumes.append(int(i))
    c.reactor_unit(3, speeds, volumes)
    # c.wash_unit(5, 12345, 6, 12345)

    # 关闭串口
    ser_pump.close()
    t2 = time.time()
    # print(f'{t2 - t1}s')

def press_gain(com_press, file):
    slave_press = p.PressUnit()
    press_runtime = int(input("请输入压力程序运行的时间："))
    slave_press.slave(com_press, 1, press_runtime, file)
    # for i in range(4):
    #     slave_press.slave(i + 2)  # slave_add从第二个开始使用，保留第一个的从机地址


if __name__ == "__main__":
    # print(dir(p), p.__name__, p.__doc__)
    file_name_start = 'D:\\2 code\\Automation\\data\\230801\\'
    filename = str(input("请输入文件名："))
    file_name = file_name_start + filename + '.txt'
    auto_thread = threading.Thread(target=pump_automation, kwargs={'com_pump':'com5'})
    ui_pump_thread = threading.Thread(target=pump_ui,daemon = True)
    press_thread = threading.Thread(target=press_gain, kwargs={'com_press':'com3', 'file':f'{file_name}'})

    auto_thread.start()
    ui_pump_thread.start()
    press_thread.start()
    auto_thread.join()
    press_thread.join(1)
    # print('1')
    analysis.plt_picture(file_name)
