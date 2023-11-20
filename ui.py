from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore, QtGui, QtWidgets
from Kamor_pump_ui import Ui_Form
import sys

class mywindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(mywindow(),self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
