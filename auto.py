import motor
from PySide6.QtWidgets import QApplication
import threading
import pressure as p
import analysis


def pump_ui():
    app = QApplication([])
    stats = motor.Stats()
    stats.ui.show()
    app.exec()


def pump_automation(com_pump):
    # t1 = time.time()

    c = motor.Module(com_pump)
    # speeds = []
    # speed = input("请输入速度值：").split(',')
    # for i in speed:
    #     speeds.append(int(i))
    # volumes = []
    # volume = input("请输入体积值：").split(',')
    # for i in volume:
    #     volumes.append(int(i))
    # c.swell(5, 3, 120)
    speeds = [60,60,60,120,200]
    volumes = [20,100]
    c.reaction_unit5(4, speeds, volumes)
    # c.reaction_unit5_time(4, speeds, volumes)
    # print('1')
    # c.reaction_unit(7, speeds, volumes, True)
    # print('2')
    c.close_serial()


def press_gain(com_press, path, file, slave_addb, slave_adde=0):
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
    path = 'D:\\2 code\\Automation\\data\\230801\\'
    file_name = str(input("请输入文件名："))
    auto_thread = threading.Thread(target=pump_automation,
                                   kwargs={'com_pump': 'com5'})
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
    # auto_thread.join()
    press_thread.join()
    print('end')
    # analysis.plt_picture(file_name)
