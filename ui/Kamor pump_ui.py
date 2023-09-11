# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Kamor pump.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QTextBrowser, QToolButton,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(723, 571)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(300, 20, 400, 521))
        self.widget.setMinimumSize(QSize(400, 500))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.clear_button = QPushButton(self.widget)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setLayoutDirection(Qt.LeftToRight)
        self.clear_button.setAutoFillBackground(False)
        self.clear_button.setFlat(False)

        self.gridLayout_2.addWidget(self.clear_button, 0, 1, 1, 1)

        self.output_label = QLabel(self.widget)
        self.output_label.setObjectName(u"output_label")

        self.gridLayout_2.addWidget(self.output_label, 0, 0, 1, 1)

        self.display_text = QTextBrowser(self.widget)
        self.display_text.setObjectName(u"display_text")
        self.display_text.setMinimumSize(QSize(198, 0))
        self.display_text.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.gridLayout_2.addWidget(self.display_text, 1, 0, 1, 2)

        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 291, 521))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame1 = QFrame(self.layoutWidget)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setMinimumSize(QSize(277, 246))
        self.frame1.setMaximumSize(QSize(277, 246))
        self.frame1.setSizeIncrement(QSize(277, 246))
        self.frame1.setBaseSize(QSize(277, 246))
        self.frame1.setLineWidth(0)
        self.gridLayout = QGridLayout(self.frame1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.wash_frequence = QSpinBox(self.frame1)
        self.wash_frequence.setObjectName(u"wash_frequence")
        self.wash_frequence.setMaximum(10)

        self.gridLayout.addWidget(self.wash_frequence, 4, 1, 1, 1)

        self.pressure_start = QPushButton(self.frame1)
        self.pressure_start.setObjectName(u"pressure_start")

        self.gridLayout.addWidget(self.pressure_start, 5, 2, 1, 1)

        self.unit2_stop = QPushButton(self.frame1)
        self.unit2_stop.setObjectName(u"unit2_stop")

        self.gridLayout.addWidget(self.unit2_stop, 3, 2, 1, 1)

        self.unit2_start = QPushButton(self.frame1)
        self.unit2_start.setObjectName(u"unit2_start")

        self.gridLayout.addWidget(self.unit2_start, 3, 1, 1, 1)

        self.first_pressure_label = QLabel(self.frame1)
        self.first_pressure_label.setObjectName(u"first_pressure_label")

        self.gridLayout.addWidget(self.first_pressure_label, 8, 0, 1, 1)

        self.unit2_label = QLabel(self.frame1)
        self.unit2_label.setObjectName(u"unit2_label")

        self.gridLayout.addWidget(self.unit2_label, 3, 0, 1, 1)

        self.wash_label = QLabel(self.frame1)
        self.wash_label.setObjectName(u"wash_label")

        self.gridLayout.addWidget(self.wash_label, 4, 0, 1, 1)

        self.unit1_label = QLabel(self.frame1)
        self.unit1_label.setObjectName(u"unit1_label")

        self.gridLayout.addWidget(self.unit1_label, 2, 0, 1, 1)

        self.swell_label = QLabel(self.frame1)
        self.swell_label.setObjectName(u"swell_label")

        self.gridLayout.addWidget(self.swell_label, 0, 0, 1, 1)

        self.unit1_stop = QPushButton(self.frame1)
        self.unit1_stop.setObjectName(u"unit1_stop")

        self.gridLayout.addWidget(self.unit1_stop, 2, 2, 1, 1)

        self.unit1_start = QPushButton(self.frame1)
        self.unit1_start.setObjectName(u"unit1_start")

        self.gridLayout.addWidget(self.unit1_start, 2, 1, 1, 1)

        self.wash_start = QPushButton(self.frame1)
        self.wash_start.setObjectName(u"wash_start")

        self.gridLayout.addWidget(self.wash_start, 4, 2, 1, 1)

        self.second_pressure_label = QLabel(self.frame1)
        self.second_pressure_label.setObjectName(u"second_pressure_label")

        self.gridLayout.addWidget(self.second_pressure_label, 9, 0, 1, 1)

        self.file_name = QLineEdit(self.frame1)
        self.file_name.setObjectName(u"file_name")

        self.gridLayout.addWidget(self.file_name, 6, 1, 1, 1)

        self.file_name_label = QLabel(self.frame1)
        self.file_name_label.setObjectName(u"file_name_label")

        self.gridLayout.addWidget(self.file_name_label, 6, 0, 1, 1)

        self.pressure_time = QLineEdit(self.frame1)
        self.pressure_time.setObjectName(u"pressure_time")

        self.gridLayout.addWidget(self.pressure_time, 5, 1, 1, 1)

        self.pressure_time_label = QLabel(self.frame1)
        self.pressure_time_label.setObjectName(u"pressure_time_label")

        self.gridLayout.addWidget(self.pressure_time_label, 5, 0, 1, 1)

        self.pressure_display = QPushButton(self.frame1)
        self.pressure_display.setObjectName(u"pressure_display")

        self.gridLayout.addWidget(self.pressure_display, 6, 2, 1, 1)

        self.swell_start = QPushButton(self.frame1)
        self.swell_start.setObjectName(u"swell_start")

        self.gridLayout.addWidget(self.swell_start, 0, 2, 1, 1)

        self.swell_frequence = QSpinBox(self.frame1)
        self.swell_frequence.setObjectName(u"swell_frequence")
        self.swell_frequence.setMaximum(10)

        self.gridLayout.addWidget(self.swell_frequence, 0, 1, 1, 1)

        self.first_pressure = QTextBrowser(self.frame1)
        self.first_pressure.setObjectName(u"first_pressure")

        self.gridLayout.addWidget(self.first_pressure, 8, 1, 1, 2)

        self.second_pressure = QTextBrowser(self.frame1)
        self.second_pressure.setObjectName(u"second_pressure")

        self.gridLayout.addWidget(self.second_pressure, 9, 1, 1, 2)


        self.verticalLayout.addWidget(self.frame1)

        self.frame2 = QFrame(self.layoutWidget)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setMinimumSize(QSize(277, 246))
        self.frame2.setMaximumSize(QSize(277, 246))
        self.frame2.setSizeIncrement(QSize(277, 246))
        self.frame2.setBaseSize(QSize(277, 246))
        self.frame2.setFrameShape(QFrame.NoFrame)
        self.frame2.setFrameShadow(QFrame.Plain)
        self.frame2.setLineWidth(0)
        self.gridLayout_4 = QGridLayout(self.frame2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pump6_stop_button = QPushButton(self.frame2)
        self.pump6_stop_button.setObjectName(u"pump6_stop_button")

        self.gridLayout_4.addWidget(self.pump6_stop_button, 3, 3, 1, 1)

        self.pump3_label = QLabel(self.frame2)
        self.pump3_label.setObjectName(u"pump3_label")

        self.gridLayout_4.addWidget(self.pump3_label, 0, 0, 1, 1)

        self.pump6_spinbox = QSpinBox(self.frame2)
        self.pump6_spinbox.setObjectName(u"pump6_spinbox")
        self.pump6_spinbox.setMaximum(300)

        self.gridLayout_4.addWidget(self.pump6_spinbox, 3, 1, 1, 1)

        self.toolButton_6 = QToolButton(self.frame2)
        self.toolButton_6.setObjectName(u"toolButton_6")

        self.gridLayout_4.addWidget(self.toolButton_6, 3, 4, 1, 1)

        self.pump8_spinbox = QSpinBox(self.frame2)
        self.pump8_spinbox.setObjectName(u"pump8_spinbox")
        self.pump8_spinbox.setMaximum(300)

        self.gridLayout_4.addWidget(self.pump8_spinbox, 5, 1, 1, 1)

        self.toolButton_4 = QToolButton(self.frame2)
        self.toolButton_4.setObjectName(u"toolButton_4")

        self.gridLayout_4.addWidget(self.toolButton_4, 1, 4, 1, 1)

        self.pump10_open_button = QPushButton(self.frame2)
        self.pump10_open_button.setObjectName(u"pump10_open_button")

        self.gridLayout_4.addWidget(self.pump10_open_button, 7, 2, 1, 1)

        self.pump5_stop_button = QPushButton(self.frame2)
        self.pump5_stop_button.setObjectName(u"pump5_stop_button")

        self.gridLayout_4.addWidget(self.pump5_stop_button, 2, 3, 1, 1)

        self.pump8_open_button = QPushButton(self.frame2)
        self.pump8_open_button.setObjectName(u"pump8_open_button")

        self.gridLayout_4.addWidget(self.pump8_open_button, 5, 2, 1, 1)

        self.pump7_spinbox = QSpinBox(self.frame2)
        self.pump7_spinbox.setObjectName(u"pump7_spinbox")
        self.pump7_spinbox.setMaximum(300)

        self.gridLayout_4.addWidget(self.pump7_spinbox, 4, 1, 1, 1)

        self.pump6_open_button = QPushButton(self.frame2)
        self.pump6_open_button.setObjectName(u"pump6_open_button")

        self.gridLayout_4.addWidget(self.pump6_open_button, 3, 2, 1, 1)

        self.toolButton_8 = QToolButton(self.frame2)
        self.toolButton_8.setObjectName(u"toolButton_8")

        self.gridLayout_4.addWidget(self.toolButton_8, 5, 4, 1, 1)

        self.pump6_label = QLabel(self.frame2)
        self.pump6_label.setObjectName(u"pump6_label")

        self.gridLayout_4.addWidget(self.pump6_label, 3, 0, 1, 1)

        self.pump10_stop_button = QPushButton(self.frame2)
        self.pump10_stop_button.setObjectName(u"pump10_stop_button")

        self.gridLayout_4.addWidget(self.pump10_stop_button, 7, 3, 1, 1)

        self.pump10_label = QLabel(self.frame2)
        self.pump10_label.setObjectName(u"pump10_label")

        self.gridLayout_4.addWidget(self.pump10_label, 7, 0, 1, 1)

        self.toolButton_9 = QToolButton(self.frame2)
        self.toolButton_9.setObjectName(u"toolButton_9")

        self.gridLayout_4.addWidget(self.toolButton_9, 6, 4, 1, 1)

        self.toolButton_7 = QToolButton(self.frame2)
        self.toolButton_7.setObjectName(u"toolButton_7")

        self.gridLayout_4.addWidget(self.toolButton_7, 4, 4, 1, 1)

        self.pump4_spinbox = QSpinBox(self.frame2)
        self.pump4_spinbox.setObjectName(u"pump4_spinbox")
        self.pump4_spinbox.setMaximum(300)

        self.gridLayout_4.addWidget(self.pump4_spinbox, 1, 1, 1, 1)

        self.toolButton_10 = QToolButton(self.frame2)
        self.toolButton_10.setObjectName(u"toolButton_10")

        self.gridLayout_4.addWidget(self.toolButton_10, 7, 4, 1, 1)

        self.pump8_label = QLabel(self.frame2)
        self.pump8_label.setObjectName(u"pump8_label")

        self.gridLayout_4.addWidget(self.pump8_label, 5, 0, 1, 1)

        self.toolButton_3 = QToolButton(self.frame2)
        self.toolButton_3.setObjectName(u"toolButton_3")

        self.gridLayout_4.addWidget(self.toolButton_3, 0, 4, 1, 1)

        self.pump7_label = QLabel(self.frame2)
        self.pump7_label.setObjectName(u"pump7_label")

        self.gridLayout_4.addWidget(self.pump7_label, 4, 0, 1, 1)

        self.pump9_spinbox = QSpinBox(self.frame2)
        self.pump9_spinbox.setObjectName(u"pump9_spinbox")
        self.pump9_spinbox.setMaximum(300)

        self.gridLayout_4.addWidget(self.pump9_spinbox, 6, 1, 1, 1)

        self.pump5_label = QLabel(self.frame2)
        self.pump5_label.setObjectName(u"pump5_label")

        self.gridLayout_4.addWidget(self.pump5_label, 2, 0, 1, 1)

        self.pump3_spinbox = QSpinBox(self.frame2)
        self.pump3_spinbox.setObjectName(u"pump3_spinbox")
        self.pump3_spinbox.setMaximum(300)

        self.gridLayout_4.addWidget(self.pump3_spinbox, 0, 1, 1, 1)

        self.pump4_label = QLabel(self.frame2)
        self.pump4_label.setObjectName(u"pump4_label")

        self.gridLayout_4.addWidget(self.pump4_label, 1, 0, 1, 1)

        self.pump9_label = QLabel(self.frame2)
        self.pump9_label.setObjectName(u"pump9_label")

        self.gridLayout_4.addWidget(self.pump9_label, 6, 0, 1, 1)

        self.pump9_stop_button = QPushButton(self.frame2)
        self.pump9_stop_button.setObjectName(u"pump9_stop_button")

        self.gridLayout_4.addWidget(self.pump9_stop_button, 6, 3, 1, 1)

        self.pump7_stop_button = QPushButton(self.frame2)
        self.pump7_stop_button.setObjectName(u"pump7_stop_button")

        self.gridLayout_4.addWidget(self.pump7_stop_button, 4, 3, 1, 1)

        self.pump5_spinbox = QSpinBox(self.frame2)
        self.pump5_spinbox.setObjectName(u"pump5_spinbox")
        self.pump5_spinbox.setMaximum(300)

        self.gridLayout_4.addWidget(self.pump5_spinbox, 2, 1, 1, 1)

        self.toolButton_5 = QToolButton(self.frame2)
        self.toolButton_5.setObjectName(u"toolButton_5")

        self.gridLayout_4.addWidget(self.toolButton_5, 2, 4, 1, 1)

        self.pump10_spinbox = QSpinBox(self.frame2)
        self.pump10_spinbox.setObjectName(u"pump10_spinbox")
        self.pump10_spinbox.setMaximum(300)

        self.gridLayout_4.addWidget(self.pump10_spinbox, 7, 1, 1, 1)

        self.pump5_open_button = QPushButton(self.frame2)
        self.pump5_open_button.setObjectName(u"pump5_open_button")

        self.gridLayout_4.addWidget(self.pump5_open_button, 2, 2, 1, 1)

        self.pump3_open_button = QPushButton(self.frame2)
        self.pump3_open_button.setObjectName(u"pump3_open_button")

        self.gridLayout_4.addWidget(self.pump3_open_button, 0, 2, 1, 1)

        self.pump8_stop_button = QPushButton(self.frame2)
        self.pump8_stop_button.setObjectName(u"pump8_stop_button")

        self.gridLayout_4.addWidget(self.pump8_stop_button, 5, 3, 1, 1)

        self.pump4_open_button = QPushButton(self.frame2)
        self.pump4_open_button.setObjectName(u"pump4_open_button")

        self.gridLayout_4.addWidget(self.pump4_open_button, 1, 2, 1, 1)

        self.pump3_stop_button = QPushButton(self.frame2)
        self.pump3_stop_button.setObjectName(u"pump3_stop_button")

        self.gridLayout_4.addWidget(self.pump3_stop_button, 0, 3, 1, 1)

        self.pump4_stop_button = QPushButton(self.frame2)
        self.pump4_stop_button.setObjectName(u"pump4_stop_button")

        self.gridLayout_4.addWidget(self.pump4_stop_button, 1, 3, 1, 1)

        self.pump7_open_button = QPushButton(self.frame2)
        self.pump7_open_button.setObjectName(u"pump7_open_button")

        self.gridLayout_4.addWidget(self.pump7_open_button, 4, 2, 1, 1)

        self.pump9_open_button = QPushButton(self.frame2)
        self.pump9_open_button.setObjectName(u"pump9_open_button")

        self.gridLayout_4.addWidget(self.pump9_open_button, 6, 2, 1, 1)

        self.pump11_label = QLabel(self.frame2)
        self.pump11_label.setObjectName(u"pump11_label")

        self.gridLayout_4.addWidget(self.pump11_label, 8, 0, 1, 1)

        self.pump11_spinbox = QSpinBox(self.frame2)
        self.pump11_spinbox.setObjectName(u"pump11_spinbox")
        self.pump11_spinbox.setMaximum(300)

        self.gridLayout_4.addWidget(self.pump11_spinbox, 8, 1, 1, 1)

        self.pump11_open_button = QPushButton(self.frame2)
        self.pump11_open_button.setObjectName(u"pump11_open_button")

        self.gridLayout_4.addWidget(self.pump11_open_button, 8, 2, 1, 1)

        self.pump11_stop_button = QPushButton(self.frame2)
        self.pump11_stop_button.setObjectName(u"pump11_stop_button")

        self.gridLayout_4.addWidget(self.pump11_stop_button, 8, 3, 1, 1)

        self.toolButton_11 = QToolButton(self.frame2)
        self.toolButton_11.setObjectName(u"toolButton_11")

        self.gridLayout_4.addWidget(self.toolButton_11, 8, 4, 1, 1)


        self.verticalLayout.addWidget(self.frame2)


        self.retranslateUi(Form)

        self.clear_button.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Kamor\u6cf5\u7684\u63a7\u5236", None))
        self.clear_button.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.output_label.setText(QCoreApplication.translate("Form", u"Output & Result", None))
        self.pressure_start.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u538b\u529b\u6d4b\u91cf", None))
        self.unit2_stop.setText(QCoreApplication.translate("Form", u"\u6682\u505c", None))
        self.unit2_start.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.first_pressure_label.setText(QCoreApplication.translate("Form", u"\u7b2c\u4e00\u4e2a\u538b\u529b\u6570\u503c:", None))
        self.unit2_label.setText(QCoreApplication.translate("Form", u"\u7b2c\u4e8c\u4e2a\u5355\u5143:", None))
        self.wash_label.setText(QCoreApplication.translate("Form", u"\u6e05\u6d17\uff1a", None))
        self.unit1_label.setText(QCoreApplication.translate("Form", u"\u7b2c\u4e00\u4e2a\u5355\u5143\uff1a", None))
        self.swell_label.setText(QCoreApplication.translate("Form", u"\u6eb6\u80c0\uff1a", None))
        self.unit1_stop.setText(QCoreApplication.translate("Form", u"\u6682\u505c", None))
        self.unit1_start.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.wash_start.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.second_pressure_label.setText(QCoreApplication.translate("Form", u"\u7b2c\u4e8c\u4e2a\u538b\u529b\u6570\u503c:", None))
        self.file_name_label.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u540d\uff1a", None))
        self.pressure_time_label.setText(QCoreApplication.translate("Form", u"\u538b\u529b\u6d4b\u91cf\u65f6\u95f4\uff1a", None))
        self.pressure_display.setText(QCoreApplication.translate("Form", u"\u538b\u529b\u663e\u793a", None))
        self.swell_start.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.pump6_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump3_label.setText(QCoreApplication.translate("Form", u"pump3:", None))
        self.toolButton_6.setText(QCoreApplication.translate("Form", u"...", None))
        self.toolButton_4.setText(QCoreApplication.translate("Form", u"...", None))
        self.pump10_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump5_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump8_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump6_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.toolButton_8.setText(QCoreApplication.translate("Form", u"...", None))
        self.pump6_label.setText(QCoreApplication.translate("Form", u"pump6:", None))
        self.pump10_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump10_label.setText(QCoreApplication.translate("Form", u"Pump10:", None))
        self.toolButton_9.setText(QCoreApplication.translate("Form", u"...", None))
        self.toolButton_7.setText(QCoreApplication.translate("Form", u"...", None))
        self.toolButton_10.setText(QCoreApplication.translate("Form", u"...", None))
        self.pump8_label.setText(QCoreApplication.translate("Form", u"pump8:", None))
        self.toolButton_3.setText(QCoreApplication.translate("Form", u"...", None))
        self.pump7_label.setText(QCoreApplication.translate("Form", u"pump7:", None))
        self.pump5_label.setText(QCoreApplication.translate("Form", u"pump5:", None))
        self.pump4_label.setText(QCoreApplication.translate("Form", u"pump4:", None))
        self.pump9_label.setText(QCoreApplication.translate("Form", u"Pump9:", None))
        self.pump9_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump7_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.toolButton_5.setText(QCoreApplication.translate("Form", u"...", None))
        self.pump5_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump3_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump8_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump4_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump3_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump4_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump7_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump9_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump11_label.setText(QCoreApplication.translate("Form", u"Pump11:", None))
        self.pump11_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump11_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.toolButton_11.setText(QCoreApplication.translate("Form", u"...", None))
    # retranslateUi

