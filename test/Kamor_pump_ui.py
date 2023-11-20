# -*- coding: utf-8 -*-
 
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import *
 
 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Form")
        MainWindow.resize(715, 225)
        self.controlsGroup = QtWidgets.QGroupBox(MainWindow)
        self.controlsGroup.setGeometry(QtCore.QRect(10, 20, 451, 151))
        self.controlsGroup.setObjectName("controlsGroup")
        self.widget = QtWidgets.QWidget(self.controlsGroup)
        self.widget.setGeometry(QtCore.QRect(10, 40, 411, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.numberSpinBox = QtWidgets.QSpinBox(self.widget)
        self.numberSpinBox.setObjectName("numberSpinBox")
        self.horizontalLayout.addWidget(self.numberSpinBox)
        self.styleCombo = QtWidgets.QComboBox(self.widget)
        self.styleCombo.setObjectName("styleCombo")
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.horizontalLayout.addWidget(self.styleCombo)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.printButton = QtWidgets.QPushButton(self.widget)
        self.printButton.setObjectName("printButton")
        self.horizontalLayout.addWidget(self.printButton)
        self.widget1 = QtWidgets.QWidget(self.controlsGroup)
        self.widget1.setGeometry(QtCore.QRect(10, 100, 201, 30))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previewStatus = QtWidgets.QCheckBox(self.widget1)
        self.previewStatus.setObjectName("previewStatus")
        self.horizontalLayout_2.addWidget(self.previewStatus)
        self.previewButton = QtWidgets.QPushButton(self.widget1)
        self.previewButton.setObjectName("previewButton")
        self.horizontalLayout_2.addWidget(self.previewButton)
        self.resultGroup = QtWidgets.QGroupBox(MainWindow)
        self.resultGroup.setGeometry(QtCore.QRect(470, 20, 231, 151))
        self.resultGroup.setObjectName("resultGroup")
        self.resultLabel = QtWidgets.QLabel(self.resultGroup)
        self.resultLabel.setGeometry(QtCore.QRect(20, 30, 191, 101))
        self.resultLabel.setObjectName("resultLabel")
 
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Form", "打印控件"))
        self.controlsGroup.setTitle(_translate("Form", "打印控制"))
        self.label.setText(_translate("Form", "打印份数:"))
        self.styleCombo.setItemText(0, _translate("Form", "A3"))
        self.styleCombo.setItemText(1, _translate("Form", "A4"))
        self.styleCombo.setItemText(2, _translate("Form", "A5"))
        self.label_2.setText(_translate("Form", "纸张类型:"))
        self.printButton.setText(_translate("Form", "打印"))
        self.previewStatus.setText(_translate("Form", "全屏预览"))
        self.previewButton.setText(_translate("Form", "预览"))
        self.resultGroup.setTitle(_translate("Form", "操作结果"))
        self.resultLabel.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
 
 
class MyMainWindow(QMainWindow, Ui_MainWindow):
    help_signal = QtCore.Signal(str)
    print_signal = QtCore.Signal(list)
    # 声明一个多重载版本的信号，包括了一个带int和str类型参数的信号，以及带str参数的信号
    preview_signal = QtCore.Signal([int, str], [str])
 
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.init_signal_and_slot()
 
    def init_signal_and_slot(self):
        self.help_signal.connect(self.show_help_message)
        self.print_signal.connect(self.print_paper)
        self.preview_signal[str].connect(self.preview_paper)
        self.preview_signal[int, str].connect(self.preview_paper_with_args)
 
        self.printButton.clicked.connect(self.emit_print_signal)
        self.previewButton.clicked.connect(self.emit_preview_signal)
 
    # 发射预览信号
    def emit_preview_signal(self):
        if self.previewStatus.isChecked():
            self.preview_signal[int, str].emit(1080, " Full Screen")
        elif not self.previewStatus.isChecked():
            self.preview_signal[str].emit("Preview")
 
    # 发射打印信号
    def emit_print_signal(self):
        print_info = [self.numberSpinBox.value(), self.styleCombo.currentText()]
        self.print_signal.emit(print_info)
 
    def print_paper(self, print_info):
        self.resultLabel.setText("打印: " + "份数：" + str(print_info[0]) + " 纸张：" + str(print_info[1]))
 
    def preview_paper_with_args(self, style, text):
        self.resultLabel.setText(str(style) + text)
 
    def preview_paper(self, text):
        self.resultLabel.setText(text)
 
    # 重载点击键盘事件
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F1:
            self.help_signal.emit("help message")
 
    # 显示帮助消息
    def show_help_message(self, message):
        self.resultLabel.setText(message)
        self.statusBar().showMessage(message)
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec())