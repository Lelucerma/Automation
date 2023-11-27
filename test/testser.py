'''
Author: wang w1838978548@126.com
Date: 2023-11-27 16:07:10
LastEditors: wang w1838978548@126.com
LastEditTime: 2023-11-27 16:18:40
FilePath: \Automation\test\testser.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import serial.tools.list_ports
import time


def ser_list():
    port_list = list(serial.tools.list_ports.comports())
    if len (port_list) == 0:
        print('无可用串口')
    else:
        for port in port_list:
            print(port.device)
            ser = serial.Serial(port.device, 9600, timeout=0.5)
            while True:
                try:
                    data = ser.readline().decode().strip()
                    if data:
                        print(data)
                    else:
                        print("无数据传输")
                        break
                except serial.SerialException:
                    print("串口断开连接")
                    break
            time.sleep(0.1)
            ser.close()


ser_list()
