'''
Author: wang w1838978548@126.com
Date: 2024-07-28 19:52:24
LastEditors: wang w1838978548@126.com
LastEditTime: 2024-08-28 19:06:53
FilePath: \Automation2\test\autoGui.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pyautogui
from pywinauto.application import Application
import time
import datetime


# 移动鼠标到屏幕中心并点击
# time.sleep(2)
class Instrument():
    def __init__(self, width, height) -> None:
        self.widthRate = width / 2560
        self.heightRate = height / 1440

    def open_app(self):        
        # 软件位置
        pyautogui.moveTo((100*self.widthRate), (200*self.heightRate))
        pyautogui.click()
        pyautogui.click()
        time.sleep(3)
        # print(pyautogui.position())
        # 输入密码
        pyautogui.moveTo((1345*self.widthRate), (738*self.heightRate))
        pyautogui.click()
        pyautogui.typewrite('Admin')
        # print(pyautogui.position())
        # 点击登录
        pyautogui.moveTo((1397*self.widthRate), (775*self.heightRate))
        pyautogui.click()
        # print(pyautogui.position())
        time.sleep(5)

    def connetInstrument(self):
        # 连接仪器
        # pyautogui.moveTo(799, 91)
        print(pyautogui.position())

    def runInstrument(self):
        # 单次运行
        pyautogui.moveTo(406*self.widthRate, 92*self.heightRate)

    def stopInstrument(self):
        # 点击停止
        pyautogui.moveTo(516*self.widthRate, 95*self.heightRate)

    def dataSave(self):
        # 样品管理
        pyautogui.moveTo(612*self.widthRate, 35*self.heightRate)
        pyautogui.click()
        # # # 第一个样品的管理
        # # pyautogui.moveTo(786*self.widthRate, 249*self.heightRate)
        # # # pyautogui.click(button='right')
        # # pyautogui.doubleClick()

        # 连接到目标应用程序
        # app = Application(backend="uia").connect(title_re=".*Admin*.")
        # 获取目标窗口(Admin)
        # print(1)
        # print(app.window(title_re=".*Admin*.").window_text())
        # dlg = app.window(title_re=".*Admin*.")
        # print(1)
        # # 移动鼠标到窗口中的某个控件上
        # dlg.child_window(title="样品ID 行 0").click_input(button='right')
        # 移动鼠标到样品管理按钮
        pyautogui.moveTo(823*self.widthRate, 289*self.heightRate)
        time.sleep(1)
        pyautogui.moveTo(951*self.widthRate, 289*self.heightRate)
        pyautogui.click()

        # pyautogui.moveTo(1379*self.widthRate, 737*self.heightRate)
        # pyautogui.click()
        # pyautogui.moveTo(1409*self.widthRate, 773*self.heightRate)
        # pyautogui.click()
        # time.sleep(1)
        # pyautogui.click()
        # pyautogui.moveTo(1280*self.widthRate, 792*self.heightRate)
        # pyautogui.click()
        # pyautogui.click()

        # 原始数据输出
        # pyautogui.moveTo(729, 284)
        # time.sleep(1)
        # pyautogui.moveTo(875, 284)
        # pyautogui.click()

        # pyautogui.moveTo(1090, 556)
        # pyautogui.click()
        # pyautogui.moveTo(1090, 586)
        # pyautogui.click()
        # pyautogui.moveTo(1079, 593)
        # pyautogui.click()
        # time.sleep(1)
        # pyautogui.moveTo(990, 614)
        # pyautogui.click()
        # pyautogui.click()
        # pyautogui.click()
        # time.sleep(1)


screen_width, screen_height = pyautogui.size()
# print(screen_width, screen_height)
a = Instrument(screen_width, screen_height)
a.dataSave()
