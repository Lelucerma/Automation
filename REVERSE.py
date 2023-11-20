import motor
import time

a = motor.Pump()
motor.ser_open('com5')
# a.pump_run(5,1,0,200)
a.pump_run(8, 1, 0, 200)
# time.sleep(3)
# # a.pump_run(8, 1, 1, 200)
# time.sleep(5)
# # a.pump_run(8, 0, 0, 200)
motor.ser_close()