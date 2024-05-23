'''
Author: wang w1838978548@126.com
Date: 2023-12-04 10:26:32
LastEditors: wang w1838978548@126.com
LastEditTime: 2024-04-18 17:30:19
FilePath: \Automation\REVERSE.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import motor
import time

a = motor.Pump()
motor.ser_open('com6')
# a.pump_run(5,1,0,200)
for i in range(3,16):
    a.pump_run(i, 0, 0, 60)
# a.pump_run(11, 0, 0, 60)
# time.sleep(3)
# # a.pump_run(8, 1, 1, 200)
# time.sleep(5)
# # a.pump_run(8, 0, 0, 200)
motor.ser_close()  