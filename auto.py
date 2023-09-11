import motor
from PySide6.QtWidgets import QApplication
import threading
import pressure as p
import time


def pump_ui():
    
    app = QApplication([])
    stats = motor.Stats()
    stats.ui.show()
    app.exec()


def pump_automation():

    c = motor.Module()
    t1 = time.time()
    # speeds = []
    # speed = input("请输入速度值：").split(',')
    # for i in speed:
    #     speeds.append(int(i))
    # volumes = []
    # volume = input("请输入体积值：").split(',')
    # for i in volume:
    #     volumes.append(int(i))
    # c.swell(5, 3, 200)
    # speeds = [60, 60, 60, 120, 200]
    # volumes = [40, 70]
    # c.deprotect_unit5(4, speeds, volumes)
    # for i in range(3):
    #     c.wash_ever(7, 200)
    # time.sleep(3)
    # c.deprotect_unit(4, speeds, volumes, True)
    # c.wash_reaction()
    # c.couple_unit(4, speeds, volumes, True)
    # c.wash_reaction()
    t2 = time.time() - t1
    print(f'all times:{t2}')



def press_gain(com_press, path, file, slave_addb, slave_adde=0):
    # time.sleep(140)
    p.serOpen(com_press)
    slave_press = p.PressUnit()
    # press_runtime = int(input("请输入压力程序运行的时间："))
    press_runtime = 300
    slave_addb, slave_adde = int(slave_addb), int(slave_adde)
    slave_adds = []
    
    if slave_adde != 0:
        for i in range(slave_addb, slave_adde+1):
            slave_adds.append(i)
    else:
        slave_adds = [slave_addb]
    print(slave_adds)
    slave_press.slaves(slave_adds, press_runtime, path, file)
    p.serClose()


if __name__ == "__main__":
    motor.ser_open('com5')
    path = 'D:\\2 code\\Automation\\data\\230830\\'
    file_name = str(input("请输入文件名："))
    auto_thread = threading.Thread(target=pump_automation)
    ui_pump_thread = threading.Thread(target=pump_ui)
    press_thread = threading.Thread(target=press_gain,
                                    kwargs={
                                        'com_press': 'com3',
                                        'path': f'{path}',
                                        'file': f'{file_name}',
                                        'slave_addb': '3',
                                        'slave_adde': '4'
                                    })

    auto_thread.start()
    ui_pump_thread.start()
    press_thread.start()
    auto_thread.join()
    # press_thread.join()  
    print('end')
    ui_pump_thread.join()
    motor.ser_close()
    # analysis.plt_pictures(path, file_name)
