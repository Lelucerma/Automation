'''
Author: wang w1838978548@126.com
Date: 2023-09-11 20:41:44
LastEditors: wang w1838978548@126.com
LastEditTime: 2024-08-30 18:00:20
FilePath: \Automation\auto.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import auto_ui
import motor
import serial.tools.list_ports
import sys
from PySide6.QtWidgets import QApplication


def pump_ui():
    app = QApplication([])
    stats = auto_ui.Stats()
    stats.show()
    sys.exit(app.exec())


def ser_list():
    port_list = list(serial.tools.list_ports.comports())
    if len (port_list) == 0:
        print('无可用串口')
    else:
        for port in port_list:
            return port.device

if __name__ == "__main__":
    port = ser_list()
    motor.ser_open(port)
    pump_ui()
    motor.ser_close()
