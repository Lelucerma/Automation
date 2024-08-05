import serial
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
    
    # 定量阀的通道控制命令
    def value_cmd(self, slave_add, passage):
        """
        这是多通道阀的控制命令
        paraments:
            slave_add : 这个阀门的通讯地址
            passage : 0:复位，1-6:孔位1-6，11:查询当前孔位
        """
        
        if passage < 10:
            self.cmd = [slave_add, 5, 0, passage, 255, 0]
            self.cmd = self.crc16(self.cmd)
        else:
            self.cmd = [slave_add, 5, 0, passage, 255, 0,]
            self.cmd = self.crc16(self.cmd)
        return self.cmd


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

if __name__ == "__main__":
    ser_open("com10")
    a = PumpCom()
    a.value_cmd(17,1)
    ser_close()