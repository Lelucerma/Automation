import motor

c = motor.Module()
motor.ser_open('com5')
for i in range(3):
    c.wash_ever(7, 200)
motor.ser_close()
