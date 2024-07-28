'''
Author: wang w1838978548@126.com
Date: 2024-07-28 19:52:24
LastEditors: wang w1838978548@126.com
LastEditTime: 2024-07-28 20:19:15
FilePath: \Automation2\test\autoGui.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pyautogui
import time

# 移动鼠标到屏幕中心并点击
time.sleep(1)
# pyautogui.moveTo(100, 200)
# pyautogui.click()
# pyautogui.click()


# 输入文本 "Hello, world!"
# pyautogui.typewrite('Hello, world!')

# # 按下 Ctrl+C
# pyautogui.hotkey('ctrl', 'c')

# # 在屏幕上查找一个图片，并点击它
button_location = pyautogui.locateOnScreen('腾讯会议.exe')
pyautogui.click(button_location)
pyautogui.click(button_location)
