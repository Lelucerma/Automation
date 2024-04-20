'''
Author: wang w1838978548@126.com
Date: 2024-01-11 16:37:58
LastEditors: wang w1838978548@126.com
LastEditTime: 2024-01-11 16:41:57
FilePath: \Automation\test\signal.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QApplication, QFormLayout, QDialog
import sys
 
 
class sub(QDialog): #创建一个dialog,用作被调用类
    changeValue = pyqtSignal() #创建槽信号
    def __init__(self, parent=None):
        super(sub, self).__init__(parent)
        self.initUi()
 
    def initUi(self):
        self.setWindowTitle('子窗口')
        self.lineEdit = QLineEdit()
        self.formlayout = QFormLayout()
        self.formlayout.addRow('输入', self.lineEdit)
        self.lineEdit.textChanged.connect(self.setValue)
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.formlayout)
        self.setLayout(self.vbox)
        self.resize(200, 200)
        self.show()
    def setValue(self):
        self.changeValue.emit()
class mainwin(QWidget):
    def __init__(self):
        super(mainwin, self).__init__()
        self.ex = sub(self) #实例化子类dialog,这一步一定要在self.initUi前面,不然initUi中不能调用没有实例化的changeValue这个槽信号
        self.initUi()
        
    def initUi(self):
        self.setWindowTitle('主窗口')
        self.lineEdit = QLineEdit()
        self.formlayout = QFormLayout()
        self.formlayout.addRow('输出', self.lineEdit)
        self.ex.changeValue.connect(self.getValue) #调用sub类中的changeValue槽信号并绑定信号到getValue这个方法
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.formlayout)
        self.setLayout(self.vbox)
        self.resize(400, 400)
        self.show()
 
    def getValue(self):
        self.lineEdit.setText(self.ex.lineEdit.text()) #将sub的lineEdit中的内容传递给mainwin本类中的lineEdit中
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = mainwin()
    sys.exit(app.exec_())