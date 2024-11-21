# 这是一个测试定量阀的软件

import serial
import time

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
    
class A():    
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
    
    def cmd_get(self,i):
        i = int(i)
        # self.cmd = [i, 0x05,0x00,0x01,0xff,0x00]
        if i < 6:
            self.cmd = [0x11, 0x05,0x00,i,0xff,0x00]
        elif i == 7:
            self.cmd = [0x11, 0x05,0x00,0x10,0xff,0x00]
        elif i == 8:
            self.cmd = [0x11, 0x05,0x00,0x20,0xff,0x00]
        elif i == 9:
            self.cmd = [0x11, 0x05,0x00,0x30,0xff,0x00]
        elif i == 10:
            self.cmd = [0x11, 0x04,0x00,0x00,0x00,0x02]
        # else: 
        #     self.cmd = [0x33, 0x06,0x00,0x0a,0x00,i]
        self.cmd = self.crc16(self.cmd)
        return self.cmd
    
    def answer(self, cmds):
        self.cmds = cmds
        print(self.cmds)
        # t = 0
        ser_pump.write(self.cmds)
        try:
            self.resp = list(ser_pump.read(32))
            print(self.resp)
            return self.resp
        except:
            return 0


ser_open('com5')
m = 1
# while (m != 11):
#     print("0：复位，1-6孔道切换,7-9低中高切换，10查询，11:退出")
#     m = int(input("是否结束程序："))
#     if m == 11:
#         pass
#     else:
#         a = A()
#         cmd = a.cmd(m)
#         resp = a.answer(cmd)
#         print(resp)
time1 = 1
# a = A()
# for i in range(1,52):   
#     resp = a.answer(a.cmd_get(i))
a = A()
cmd1 = a.cmd_get(2)
resp = a.answer(cmd1)
time.sleep(5)
cmd2 = a.cmd_get(1)
resp = a.answer(cmd2)
# cmd3 = a.cmd_get(3)
# resp = a.answer(cmd3)
# time1= int(input("请输入是否停止："))
# time.sleep(time1)
ser_close()