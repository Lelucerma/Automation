import time
import minimalmodbus
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
        print(self.data)
        self.begin_cmd = self.cm.write_bits(slave_add, '001', self.data)
        print(self.begin_cmd)
        while True:
            ser.write(self.begin_cmd)
            self.resp1 = list(ser.read(32))
            if self.resp1 != []:
                break
        print(self.resp1)
        if run and self.run_speed:
            self.speed_cmd = self.cm.write_registers(slave_add, '009', self.run_speed)
            print(self.speed_cmd)
            while True:
                ser.write(self.speed_cmd)
                self.resp12 = list(ser.read(32))
                if self.resp2 != []:
                    break
            print(self.resp2)

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
        self.time1 = self.time_tube + (self.volume / self.flow_rate()) + self.redundancy
        return self.time1
    
    # 流量矫正
    def flow_rate(self):
        """"
        对速度值进行相应的矫正，返回一个具体的流量数值
        目前只是一个粗略的设置，需要通过实验进行相应的速度矫正模块
        """
        self.rate = self.run_speed / 5000
        return self.rate


# 一个单元泵的运行
class Module():

    def __init__(self) -> None:
        pass

    def reactor_unit(self, slave_add1, speed1, slave_add2=None, speed2=None):
        """"
        对于反应器的蠕动泵进行相应的控制，超过控制时间后蠕动泵停止工作
        首个反应单元有两个蠕动泵，因此有两个设备地址。

        Args:
            * slave_add1 第一个泵
            * slave_add2 第二个泵
            * speed 泵的运行速度

        """
        self.time_starts = time.time()
        self.time_start = time.time()
        self.time2 = 0
        self.pump_ever = Pump()
        self.speed2 = speed2
        self.pump_ever.pump_run(slave_add1, 1, 1, speed=speed1)
        # 如果未传入第二个泵的地址，则不发送相关指令。
        if slave_add2 is None:
            pass
        else:
            self.pump_ever.pump_run(slave_add2, True, True, speed=speed2)
        # print(self.pump_ever.run_time(20))
        time.sleep(self.pump_ever.run_time(20))
        self.pump_ever.pump_run(slave_add1, 0, 0)
        if slave_add2 is None:
            pass
        else:
            self.pump_ever.pump_run(slave_add2, False, False)
        
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
        time.sleep(self.pump_ever.run_time(20))
        self.pump_ever.pump_run(slave_add1, False, False, speed1)
        self.pump_ever.pump_run(slave_add2, False, False, speed2)
        




def main(com):
    t1 = time.time()
    global ser
    ser = serial.Serial(com, 9600, timeout=1)

    # 数据位为8位
    ser.bytesize = serial.EIGHTBITS
    # 停止位为1位
    ser.stopbits = serial.STOPBITS_ONE
    # 无奇偶校验位
    ser.parity = serial.PARITY_NONE

    c = Module()
    c.reactor_unit(4, 12345)
    # c.wash_unit(5, 12345, 6, 12345)

    # 关闭串口
    ser.close()
    t2 = time.time()
    print((t2 - t1))


if __name__ == "__main__":

    main('com5')


