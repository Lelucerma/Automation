'''
Author: wang w1838978548@126.com
Date: 2024-03-13 18:24:22
LastEditors: wang w1838978548@126.com
LastEditTime: 2024-05-23 16:40:40
FilePath: \Automation\setadd.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

from minimalmodbus import minimalmodbus

# 设置从机地址
slave_address = 1

# 创建通讯对象
instrument = minimalmodbus.Instrument('com6', slaveaddress=slave_address)
# 设置串口通信参数
instrument.serial.baudrate = 9600
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 0.05

instrument.write_register(0x4001, 16)
instrument.write_bit(0x0004, 1)
# instrument.write_register(0x4009, 160)
# print(0x40)
