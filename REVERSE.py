import motor

a = motor.Pump()
motor.ser_open('com5')
# a.pump_run(5,1,0,200)
a.pump_run(8,0,0,200)
motor.ser_close()