'''
Author: wang w1838978548@126.com
Date: 2024-07-29 17:18:30
LastEditors: wang w1838978548@126.com
LastEditTime: 2024-08-01 17:11:22
FilePath: \Automation\test\rightclick.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pyautogui
from pywinauto.application import Application
import time
import datetime

screen_width, screen_height = pyautogui.size()
print(screen_width, screen_height)
# 连接到目标应用程序
# app = Application(backend="uia").connect(title_re=".*Admin*.")
# # 获取目标窗口(Admin)
# print(1)
# # print(app.window(title_re=".*Admin*.").window_text())
# dlg = app.window(title_re=".*Admin*.")
# print(1)
# # # 移动鼠标到窗口中的某个控件上
# dlg.child_window(title="样品ID 行 0").click_input(button='right')

# pyautogui.moveTo(823, 289)
# time.sleep(0.5)
# pyautogui.moveTo(951, 289)
# pyautogui.click()

# pyautogui.moveTo(1379, 737)
# pyautogui.click()
# pyautogui.moveTo(1409, 773)
# pyautogui.click()
# pyautogui.moveTo(1409, 773)
# pyautogui.click()
# pyautogui.moveTo(1280, 792)
# time.sleep(1)
# pyautogui.click()
# pyautogui.click()
# pyautogui.moveTo(812, 250)
# # time.sleep(1)
# pyautogui.doubleClick()

time.sleep(3)
print(pyautogui.position())
# # 模拟右键点击
# pyautogui.rightClick()
