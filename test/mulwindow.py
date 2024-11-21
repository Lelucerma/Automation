'''
Author: wang w1838978548@126.com
Date: 2024-11-21 13:49:54
LastEditors: wang w1838978548@126.com
LastEditTime: 2024-11-21 13:50:00
FilePath: \Automation\test\mulwindow.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from random import randint

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

import sys


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window %d"% randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 临时解决窗口的出现
        self.w = None
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        # 检查窗口是否被重复创建，防止覆盖原来的窗口
        if self.w is None:
            self.w = AnotherWindow()
        self.w.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()