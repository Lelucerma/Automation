import motor
import serial
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
    speeds = []
    speed = input("请输入速度值：").split(',')
    for i in speed:
        speeds.append(int(i))
    volumes = []
    volume = input("请输入体积值：").split(',')
    for i in volume:
        volumes.append(int(i))
    c.deprotection_unit(3, speeds, volumes)
    print('1')
    c.deprotection_unit(7, speeds, volumes, True)
    print('2')
    # c.wash_unit(5, 12345, 6, 12345)

    c.close_serial()
    # t2 = time.time()
    # print(f'{t2 - t1}s')


def press_gain(com_press, path, file):
    slave_press = p.PressUnit()
    press_runtime = int(input("请输入压力程序运行的时间："))
    slave_press.slave(com_press, 1, press_runtime, path, file)
    # for i in range(4):
    #     slave_press.slave(i + 2)  # slave_add从第二个开始使用，保留第一个的从机地址


if __name__ == "__main__":
    print(dir(p), p.__name__, p.__doc__)
    path = 'D:\\2 code\\Automation\\data\\230801\\'
    file_name = str(input("请输入文件名："))
    auto_thread = threading.Thread(target=pump_automation,
                                   kwargs={'com_pump': 'com6'})
    ui_pump_thread = threading.Thread(target=pump_ui)
    press_thread = threading.Thread(target=press_gain,
                                    kwargs={
                                        'com_press': 'com6',
                                        'path': f'{path}',
                                        'file': f'{file_name}'
                                    })

    auto_thread.start()
    ui_pump_thread.start()
    press_thread.start()
    auto_thread.join()
    press_thread.join()
    print('1')
    analysis.plt_picture(file_name)