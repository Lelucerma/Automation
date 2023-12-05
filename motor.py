#!/usr/bin/python3

'''
Author: wang w1838978548@126.com
Date: 2023-09-25 20:54:24
LastEditors: wang w1838978548@126.com
LastEditTime: 2023-11-20 11:07:34
FilePath: \Automation\motor.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 
进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import math
import time
import serial
import relay


# 泵的命令行组成
class PumpCom:
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
class Pump:
    # 初始化操作
    def __init__(self) -> None:

        self.cm = PumpCom()
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
                self.data = 1
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
        self.speed_change_cmd = self.cm.write_registers(
            slave_add, '009', self.run_speed)
        # print(self.speed_cmd)
        self.resp3 = self.answer(self.speed_change_cmd)
        # print(self.resp3)

    def answer(self, cmd):
        self.cmd = cmd
        # t = 0
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

    # 关闭串口


# 一个单元泵的运行
class Module:
    def __init__(self) -> None:

        self.slave_add1, self.slave_add2 = None, None
        self.slave_add3, self.slave_add4 = None, None

        self.speed1, self.speed2 = 60, 60
        self.speed3, self.speed4 = 60, 200

        self.volume1, self.volume2 = 50, 50
        self.volume3 = 200

        self.time1, self.time2 = None, None
        self.time3, self.time4 = None, None
        self.speed_before = None

        self.time_starts = time.time()  # 这个是总计时，不能更改
        self.time_start = time.time()  # 这个是可以作为部分计时，可以更改

        self.length, self.diameter = None, None
        self.tube_area, self.tube_volume = None, None

        self.pump_ever = Pump()
        self.first_value = relay.Value(11)
        self.second_value = relay.Value(12)

    def deprotect_unit(self,
                      slave_add1=1,
                      speed=None,
                      volume=None,
                      next_unit=None,
                      speed_before=0):
        """"
        直接控制一个反应单元，整体的逻辑是先判断那个管路长，依托于设别的构建相应的管路，
        使用

        Args:

            * slave_add1 第一个泵
            * slave_add2 第二个泵
            * speed 四个泵的运行速度
            * volume 两个反应物的投料量

        """
        if speed is None:
            speed = []
        if volume is None:
            volume = []
        if slave_add1 == 0:
            pass
        else:
            self.slave_add1, self.slave_add2 = slave_add1, slave_add1+1
            self.slave_add3, self.slave_add4 = slave_add1+2, slave_add1+3
            self.slave_add5 = slave_add1 + 4
        if not speed:
            pass
        else:
            self.speed1, self.speed2 = speed[0], speed[1]
            self.speed3, self.speed4 = speed[2], speed[3]
            self.speed5 = speed[4]
        if not volume:
            pass
        else:
            self.volume1, self.volume4 = volume[0], volume[1]

        if next_unit:
            self.speed_before = speed_before
            self.pump_ever.pump_run(7, 1, 1,
                                    200)
            time.sleep(1)
            self.pump_ever.pump_run(7, 0, 0,
                                    self.speed_before)

        # 计算各个泵需要的运行时间,不同的进料体积需要不同的进料速度
        self.volume5_time()

        # 进行各个时间的计算程序
        self.run_time()

        # 开始计时
        self.time_starts = time.time()  # 这个是总计时，不能更改
        self.time_start = time.time()  # 这个是可以作为部分计时，可以更改

        # 溶胀后进行鼓泡操作
        self.pump_ever.pump_run(8, 1, 0, self.speed1*2)
        self.pump_ever.pump_run(3, 1, 1, self.speed1)

        time.sleep(self.time3-2)
        print(f"self.time3：{self.time3-2}")

        # 开启阀门
        print('开启阀门')
        self.first_value.value_start()
        # winsound.Beep(400, 1000)
        # 开启第三个泵
        self.pump_ever.pump_run(4, 1, 1, self.speed3)

        # 计算物料输送结束的时间t3
        time.sleep(self.pump1_runtime)
        self.pump_ever.pump_run(3, 0, 0, self.speed1)

        # 耦合反应时间
        self.time = self.pump3_runtime-self.pump1_runtime + 120
        time.sleep(self.time)
        print(f"self.time：{self.time}")

        # 关闭阀门
        print('关闭阀门')
        self.first_value.value_stop()
        self.pump_ever.pump_run(3, 1, 1, self.speed5)
        # winsound.Beep(400, 2000)
        # 开启第五个泵
        self.pump_ever.pump_run(8, 1, 1, self.speed5)
        
        # self.second_value.value_start()
        # time.sleep(2)
        # self.pump_ever.pump_run(7, 1, 1, self.speed3)
        # time.sleep(5)
        # self.pump_ever.pump_run(7, 0, 0, self.speed3)
        # self.second_value.value_stop()
        
        time.sleep(self.time6+self.pump1_runtime)
        
        # 关闭前三个泵（因为如果前两个泵提前关闭，那么会有溶液在前两个泵的出口管道中进行堆积）
        self.pump_ever.pump_run(3, 0, 0, self.speed3)

        # 关闭第五个泵
        time.sleep(3)
        self.pump_ever.pump_run(8, 0, 0, self.speed5)
        self.first_value.value_end()


    def couple_unit(self,
                      slave_add1=1,
                      speed=None,
                      volume=None,
                      next_unit=None,
                      speed_before=0):
        """"
        直接控制一个反应单元，整体的逻辑是先判断那个管路长，依托于设别的构建相应的管路，
        使用

        Args:

            * slave_add1 第一个泵
            * slave_add2 第二个泵
            * speed 四个泵的运行速度
            * volume 两个反应物的投料量

        """
        if speed is None:
            speed = []
        if volume is None:
            volume = []
        if slave_add1 == 0:
            pass
        else:
            self.slave_add1, self.slave_add2 = slave_add1, slave_add1+1
            self.slave_add3, self.slave_add4 = slave_add1+2, slave_add1+3
            self.slave_add5 = slave_add1 + 4
        if not speed:
            pass
        else:
            self.speed1, self.speed2 = speed[0], speed[1]
            self.speed3, self.speed4 = speed[2], speed[3]
            self.speed5 = speed[4]
        if not volume:
            pass
        else:
            self.volume1, self.volume4 = volume[0], volume[1]

        if next_unit:
            self.speed_before = speed_before
            # self.pump_ever.pump_run(self.slave_add1 - 2, 1, 1,
            #                         self.speed_before)
            self.pump_ever.pump_run(7, 1, 1,
                                    200)
            time.sleep(1)
            self.pump_ever.pump_run(7, 0, 0,
                                    self.speed_before)

        # 计算各个泵需要的运行时间,不同的进料体积需要不同的进料速度
        self.volume5_time()

        # 进行各个时间的计算程序
        self.run_time()

        # 开始计时
        self.time_starts = time.time()  # 这个是总计时，不能更改
        self.time_start = time.time()  # 这个是可以作为部分计时，可以更改

        # 溶胀后进行鼓泡操作
        self.pump_ever.pump_run(8, 1, 0, self.speed1*3)
        # 因为要循环，因此肯定是前两个泵进行循环操作，而后洗涤的泵就开启时间较晚
        self.pump_ever.pump_run(5, 1, 1, self.speed1)

        time.sleep(self.time3-2)
        # time.sleep(10)
        print(f"self.time3：{self.time3-2}")

        # 开启阀门
        print('开启阀门')
        # self.first_value.value_start()
        # winsound.Beep(400, 1000)
        # 开启第三个泵
        self.pump_ever.pump_run(6, 1, 1, self.speed3)

        # 计算物料输送结束的时间t3
        time.sleep(self.pump1_runtime)
        # time.sleep(10)
        print(f"self.pump1_runtime：{self.pump1_runtime}")
        # 关闭氨基酸泵
        self.pump_ever.pump_run(5, 0, 0, self.speed1)

        # 耦合反应时间
        self.time = self.pump3_runtime-self.pump1_runtime + 240
        time.sleep(self.time)
        # time.sleep(10)
        print(f"self.time：{self.time}")

        # 关闭阀门
        print('关闭阀门')
        # self.first_value.value_stop()
        # open wash value
        
        self.pump_ever.pump_run(6, 1, 1, self.speed5)
        # winsound.Beep(400, 2000)
        # 开启第五个泵
        self.pump_ever.pump_run(8, 1, 1, self.speed5)
        
        # self.second_value.value_start()
        # time.sleep(2)
        # self.pump_ever.pump_run(7, 1, 1, self.speed3)
        # time.sleep(10)
        # self.pump_ever.pump_run(7, 0, 0, self.speed3)
        
        
        # time.sleep(3)
        
        time.sleep(self.time6+self.pump1_runtime)
        
        # 关闭前三个泵（因为如果前两个泵提前关闭，那么会有溶液在前两个泵的出口管道中进行堆积）
        self.pump_ever.pump_run(6, 0, 0, self.speed3)
        # self.second_value.value_stop()
        # 循环装置鼓泡guanbi
        # self.pump_ever.pump_run(self.slave_add5, 0, 0, self.speed3)
     
        # 关闭第五个泵
        time.sleep(3)
        self.pump_ever.pump_run(8, 0, 0, self.speed5)
        # self.first_value.value_end()


    def wash(self, m):
        for i in range(m):
            self.swell_ever()

    # 单个溶胀过程
    def swell_ever(self, slave_add, speed):
        self.pump_ever.pump_run(slave_add, 1, 1, speed)
        time.sleep(2)  # 添加溶液的时间
        self.pump_ever.pump_run(slave_add, 0, 0, speed)
        self.pump_ever.pump_run(slave_add + 1, 1, 0, speed)
        time.sleep(5)  # 鼓动混合的时间
        self.pump_ever.pump_run(slave_add + 1, 1, 1, speed)
        time.sleep(15)  # 抽干溶液的时间
        self.pump_ever.pump_run(slave_add + 1, 0, 0, speed)

    # 单个洗涤过程
    def wash_ever(self, slave_add, speed):
        self.pump_ever.pump_run(slave_add, 1, 1, speed)
        time.sleep(2)  # 添加溶液的时间
        self.pump_ever.pump_run(slave_add, 0, 0, speed)
        self.pump_ever.pump_run(slave_add + 1, 1, 0, speed)
        time.sleep(5)  # 鼓动混合的时间
        self.pump_ever.pump_run(slave_add + 1, 1, 1, speed)
        time.sleep(15)  # 抽干溶液的时间
        self.pump_ever.pump_run(slave_add + 1, 0, 0, speed)

    def tube_time(self, length, speed, diameter=0.5):
        """"
        根据泵的速度和需要进液的容量确定泵的运行时间，需要设置一定的时间冗余，
        对于泵停止所需要的时间需要进行相应的调整。需做出一个统计
        Args:
            * direction 泵的运行方向
            * speed 泵的运行速度

        """

        self.length = length  # 管道的长度
        self.diameter = diameter  # 管道的直径
        self.speed = speed
        self.tube_area = math.pi * math.pow((self.diameter / 2), 2)
        self.tube_volume = self.tube_area * self.length
        self.tube_time1 = self.tube_volume / self.speed / 0.8027 * 60
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
        self.pump3_intime = self.tube_time(40, self.speed3)
        self.pump3_outtime = self.tube_time(23, self.speed3)
        self.pump4_intime = self.tube_time(67, self.speed4)
        self.pump4_outtime = self.tube_time(40, self.speed4)
        self.reactor_intime = self.tube_time(10, self.speed1)
        self.reactor_outtime = self.tube_time(10, self.speed1)
        self.reactor_time = self.tube_time(10, self.speed1)
        self.wash_intime = self.tube_time(40, self.speed3)
        self.pump_3_intime = self.tube_time(10, self.speed3)

        # 这个时间是主物料开始到洗涤单元的时间（应该以数值的进度作为判断）
        self.time3 = self.pump1_intime + self.pump1_outtime + \
                     self.reactor_intime + self.reactor_outtime + \
                     self.reactor_time + self.wash_intime

        # 这个时间是主物料开始到循环泵的时间（应该以数值的进度作为判断）
        self.time4 = self.pump1_intime + self.pump1_outtime + \
                     self.reactor_intime + self.reactor_outtime + \
                     self.reactor_time + self.pump_3_intime

        # 这个时间是主物料从循环泵到洗涤的时间（应该以数值的进度作为判断）
        self.time6 = self.pump1_intime + self.pump1_outtime + \
                     self.reactor_intime + self.reactor_outtime + \
                     self.reactor_time + self.wash_intime

        # 这个应该是洗涤泵到洗涤单元的时间
        self.time7 = self.pump4_intime + self.pump4_outtime

    def volume_time(self):
        if self.volume1 < self.volume2:
            self.pump1_runtime = (self.volume1 / self.speed1) * 60 + 3
            self.speed2 = self.volume2 / (self.pump1_runtime / 60)
            self.pump2_runtime = self.pump1_runtime
        else:
            self.pump2_runtime = (self.volume1 / self.speed1) * 60 + 3
            self.speed1 = self.volume2 / (self.pump2_runtime / 60)
            self.pump1_runtime = self.pump2_runtime
        # print(f'体积为:{self.volume}, 速度为：{self.speed},时间为：{self.pump_runtime}')
        self.pump4_runtime = (self.volume4 / self.speed3) * 60 + 3

    def volume5_time(self):
        self.pump1_runtime = (self.volume1 / self.speed1) * 60 + 3
        # self.speed2 = self.volume2 / (self.pump1_runtime / 60)
        self.pump2_runtime = (self.volume1 / self.speed1) * 60 + 3
        self.pump3_runtime = 120
        self.pump4_runtime = (self.volume4 / self.speed4) * 60 + 3

    def wash_reaction(self):
        self.pump_ever.pump_run(5, 1, 1, 60)
        self.pump_ever.pump_run(6, 1, 1, 60)
        self.pump_ever.pump_run(8, 1, 1, 180)
        time.sleep(40)
        self.pump_ever.pump_run(5, 0, 0)
        self.pump_ever.pump_run(6, 0, 0)
        self.pump_ever.pump_run(8, 0, 0)


def ser_open(com_pump):
    global ser_pump
    ser_pump = serial.Serial(com_pump, 9600, timeout=1)

    # 数据位为8位
    ser_pump.bytesize = serial.EIGHTBITS
    # 停止位为1位
    ser_pump.stopbits = serial.STOPBITS_ONE
    # 无奇偶校验位
    ser_pump.parity = serial.PARITY_NONE


def ser_close():
    ser_pump.close()


# ser_open("com5")
# a = Pump()
# a.pump_run(8,0,0)
# pump = Module()
# # for i in range(3):
# #     pump.wash_ever(7, 200)
# ser_close()
