# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Kamor_pump.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDial, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTextBrowser, QToolBox, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(863, 602)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(380, 230))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.toolBox = QToolBox(self.frame)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 399, 359))
        self.layoutWidget = QWidget(self.page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 11, 340, 244))
        self.verticalLayout_100 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.pump3_label = QLabel(self.layoutWidget)
        self.pump3_label.setObjectName(u"pump3_label")

        self.horizontalLayout_101.addWidget(self.pump3_label)

        self.pump3_spinbox = QSpinBox(self.layoutWidget)
        self.pump3_spinbox.setObjectName(u"pump3_spinbox")
        self.pump3_spinbox.setMaximum(300)

        self.horizontalLayout_101.addWidget(self.pump3_spinbox)

        self.pump3_open_button = QPushButton(self.layoutWidget)
        self.pump3_open_button.setObjectName(u"pump3_open_button")

        self.horizontalLayout_101.addWidget(self.pump3_open_button)

        self.pump3_stop_button = QPushButton(self.layoutWidget)
        self.pump3_stop_button.setObjectName(u"pump3_stop_button")

        self.horizontalLayout_101.addWidget(self.pump3_stop_button)

        self.pump3_reverse = QPushButton(self.layoutWidget)
        self.pump3_reverse.setObjectName(u"pump3_reverse")

        self.horizontalLayout_101.addWidget(self.pump3_reverse)


        self.verticalLayout_100.addLayout(self.horizontalLayout_101)

        self.horizontalLayout_102 = QHBoxLayout()
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.pump4_label = QLabel(self.layoutWidget)
        self.pump4_label.setObjectName(u"pump4_label")

        self.horizontalLayout_102.addWidget(self.pump4_label)

        self.pump4_spinbox = QSpinBox(self.layoutWidget)
        self.pump4_spinbox.setObjectName(u"pump4_spinbox")
        self.pump4_spinbox.setMaximum(300)

        self.horizontalLayout_102.addWidget(self.pump4_spinbox)

        self.pump4_open_button = QPushButton(self.layoutWidget)
        self.pump4_open_button.setObjectName(u"pump4_open_button")

        self.horizontalLayout_102.addWidget(self.pump4_open_button)

        self.pump4_stop_button = QPushButton(self.layoutWidget)
        self.pump4_stop_button.setObjectName(u"pump4_stop_button")

        self.horizontalLayout_102.addWidget(self.pump4_stop_button)

        self.pump4_reverse = QPushButton(self.layoutWidget)
        self.pump4_reverse.setObjectName(u"pump4_reverse")

        self.horizontalLayout_102.addWidget(self.pump4_reverse)


        self.verticalLayout_100.addLayout(self.horizontalLayout_102)

        self.horizontalLayout_103 = QHBoxLayout()
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.pump5_label = QLabel(self.layoutWidget)
        self.pump5_label.setObjectName(u"pump5_label")

        self.horizontalLayout_103.addWidget(self.pump5_label)

        self.pump5_spinbox = QSpinBox(self.layoutWidget)
        self.pump5_spinbox.setObjectName(u"pump5_spinbox")
        self.pump5_spinbox.setMaximum(300)

        self.horizontalLayout_103.addWidget(self.pump5_spinbox)

        self.pump5_open_button = QPushButton(self.layoutWidget)
        self.pump5_open_button.setObjectName(u"pump5_open_button")

        self.horizontalLayout_103.addWidget(self.pump5_open_button)

        self.pump5_stop_button = QPushButton(self.layoutWidget)
        self.pump5_stop_button.setObjectName(u"pump5_stop_button")

        self.horizontalLayout_103.addWidget(self.pump5_stop_button)

        self.pump5_reverse = QPushButton(self.layoutWidget)
        self.pump5_reverse.setObjectName(u"pump5_reverse")

        self.horizontalLayout_103.addWidget(self.pump5_reverse)


        self.verticalLayout_100.addLayout(self.horizontalLayout_103)

        self.horizontalLayout_104 = QHBoxLayout()
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.unit1_wash = QLabel(self.layoutWidget)
        self.unit1_wash.setObjectName(u"unit1_wash")

        self.horizontalLayout_104.addWidget(self.unit1_wash)

        self.unit1_wash_spinbox = QSpinBox(self.layoutWidget)
        self.unit1_wash_spinbox.setObjectName(u"unit1_wash_spinbox")
        self.unit1_wash_spinbox.setMaximum(300)

        self.horizontalLayout_104.addWidget(self.unit1_wash_spinbox)

        self.unit1_wash_open_button = QPushButton(self.layoutWidget)
        self.unit1_wash_open_button.setObjectName(u"unit1_wash_open_button")

        self.horizontalLayout_104.addWidget(self.unit1_wash_open_button)

        self.unit1_wahs_stop_button = QPushButton(self.layoutWidget)
        self.unit1_wahs_stop_button.setObjectName(u"unit1_wahs_stop_button")

        self.horizontalLayout_104.addWidget(self.unit1_wahs_stop_button)

        self.unit1_reverse = QPushButton(self.layoutWidget)
        self.unit1_reverse.setObjectName(u"unit1_reverse")

        self.horizontalLayout_104.addWidget(self.unit1_reverse)


        self.verticalLayout_100.addLayout(self.horizontalLayout_104)

        self.horizontalLayout_105 = QHBoxLayout()
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.unit1_waste_label = QLabel(self.layoutWidget)
        self.unit1_waste_label.setObjectName(u"unit1_waste_label")

        self.horizontalLayout_105.addWidget(self.unit1_waste_label)

        self.unit1_waste_spinbox = QSpinBox(self.layoutWidget)
        self.unit1_waste_spinbox.setObjectName(u"unit1_waste_spinbox")
        self.unit1_waste_spinbox.setMaximum(300)

        self.horizontalLayout_105.addWidget(self.unit1_waste_spinbox)

        self.unit1_waste_open_button = QPushButton(self.layoutWidget)
        self.unit1_waste_open_button.setObjectName(u"unit1_waste_open_button")

        self.horizontalLayout_105.addWidget(self.unit1_waste_open_button)

        self.unit1_waste_stop_button = QPushButton(self.layoutWidget)
        self.unit1_waste_stop_button.setObjectName(u"unit1_waste_stop_button")

        self.horizontalLayout_105.addWidget(self.unit1_waste_stop_button)

        self.unit1_waste_reverse = QPushButton(self.layoutWidget)
        self.unit1_waste_reverse.setObjectName(u"unit1_waste_reverse")

        self.horizontalLayout_105.addWidget(self.unit1_waste_reverse)


        self.verticalLayout_100.addLayout(self.horizontalLayout_105)

        self.horizontalLayout_106 = QHBoxLayout()
        self.horizontalLayout_106.setSpacing(10)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.unit1_depro_label = QLabel(self.layoutWidget)
        self.unit1_depro_label.setObjectName(u"unit1_depro_label")

        self.horizontalLayout_106.addWidget(self.unit1_depro_label)

        self.unit1_depro_start_button = QPushButton(self.layoutWidget)
        self.unit1_depro_start_button.setObjectName(u"unit1_depro_start_button")

        self.horizontalLayout_106.addWidget(self.unit1_depro_start_button)

        self.unit1_depro_stop_button = QPushButton(self.layoutWidget)
        self.unit1_depro_stop_button.setObjectName(u"unit1_depro_stop_button")

        self.horizontalLayout_106.addWidget(self.unit1_depro_stop_button)

        self.horizontalLayout_106.setStretch(0, 3)
        self.horizontalLayout_106.setStretch(1, 2)
        self.horizontalLayout_106.setStretch(2, 2)

        self.verticalLayout_100.addLayout(self.horizontalLayout_106)

        self.horizontalLayout_107 = QHBoxLayout()
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.unit1_couple_label = QLabel(self.layoutWidget)
        self.unit1_couple_label.setObjectName(u"unit1_couple_label")

        self.horizontalLayout_107.addWidget(self.unit1_couple_label)

        self.unit1_couple_start_button = QPushButton(self.layoutWidget)
        self.unit1_couple_start_button.setObjectName(u"unit1_couple_start_button")

        self.horizontalLayout_107.addWidget(self.unit1_couple_start_button)

        self.unit1_couple__stop_button = QPushButton(self.layoutWidget)
        self.unit1_couple__stop_button.setObjectName(u"unit1_couple__stop_button")

        self.horizontalLayout_107.addWidget(self.unit1_couple__stop_button)

        self.horizontalLayout_107.setStretch(0, 3)
        self.horizontalLayout_107.setStretch(1, 2)
        self.horizontalLayout_107.setStretch(2, 2)

        self.verticalLayout_100.addLayout(self.horizontalLayout_107)

        self.horizontalLayout_108 = QHBoxLayout()
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.unit1_wash_label = QLabel(self.layoutWidget)
        self.unit1_wash_label.setObjectName(u"unit1_wash_label")

        self.horizontalLayout_108.addWidget(self.unit1_wash_label)

        self.unit1_wash_frequence_sppinbox = QSpinBox(self.layoutWidget)
        self.unit1_wash_frequence_sppinbox.setObjectName(u"unit1_wash_frequence_sppinbox")
        self.unit1_wash_frequence_sppinbox.setMaximum(10)

        self.horizontalLayout_108.addWidget(self.unit1_wash_frequence_sppinbox)

        self.unit1_wash_start_button = QPushButton(self.layoutWidget)
        self.unit1_wash_start_button.setObjectName(u"unit1_wash_start_button")

        self.horizontalLayout_108.addWidget(self.unit1_wash_start_button)

        self.horizontalLayout_108.setStretch(0, 3)
        self.horizontalLayout_108.setStretch(1, 2)
        self.horizontalLayout_108.setStretch(2, 2)

        self.verticalLayout_100.addLayout(self.horizontalLayout_108)

        self.toolBox.addItem(self.page, u"unit 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 399, 359))
        self.layoutWidget1 = QWidget(self.page_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 340, 244))
        self.verticalLayout_200 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_200.setObjectName(u"verticalLayout_200")
        self.verticalLayout_200.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_201 = QHBoxLayout()
        self.horizontalLayout_201.setObjectName(u"horizontalLayout_201")
        self.pump6_label = QLabel(self.layoutWidget1)
        self.pump6_label.setObjectName(u"pump6_label")

        self.horizontalLayout_201.addWidget(self.pump6_label)

        self.pump6_spinbox = QSpinBox(self.layoutWidget1)
        self.pump6_spinbox.setObjectName(u"pump6_spinbox")
        self.pump6_spinbox.setMaximum(300)

        self.horizontalLayout_201.addWidget(self.pump6_spinbox)

        self.pump6_open_button = QPushButton(self.layoutWidget1)
        self.pump6_open_button.setObjectName(u"pump6_open_button")

        self.horizontalLayout_201.addWidget(self.pump6_open_button)

        self.pump6_stop_button = QPushButton(self.layoutWidget1)
        self.pump6_stop_button.setObjectName(u"pump6_stop_button")

        self.horizontalLayout_201.addWidget(self.pump6_stop_button)

        self.pump6_reverse = QPushButton(self.layoutWidget1)
        self.pump6_reverse.setObjectName(u"pump6_reverse")

        self.horizontalLayout_201.addWidget(self.pump6_reverse)


        self.verticalLayout_200.addLayout(self.horizontalLayout_201)

        self.horizontalLayout_202 = QHBoxLayout()
        self.horizontalLayout_202.setObjectName(u"horizontalLayout_202")
        self.pump7_label = QLabel(self.layoutWidget1)
        self.pump7_label.setObjectName(u"pump7_label")

        self.horizontalLayout_202.addWidget(self.pump7_label)

        self.pump7_spinbox = QSpinBox(self.layoutWidget1)
        self.pump7_spinbox.setObjectName(u"pump7_spinbox")
        self.pump7_spinbox.setMaximum(300)

        self.horizontalLayout_202.addWidget(self.pump7_spinbox)

        self.pump7_open_button = QPushButton(self.layoutWidget1)
        self.pump7_open_button.setObjectName(u"pump7_open_button")

        self.horizontalLayout_202.addWidget(self.pump7_open_button)

        self.pump7_stop_button = QPushButton(self.layoutWidget1)
        self.pump7_stop_button.setObjectName(u"pump7_stop_button")

        self.horizontalLayout_202.addWidget(self.pump7_stop_button)

        self.pump7_reverse = QPushButton(self.layoutWidget1)
        self.pump7_reverse.setObjectName(u"pump7_reverse")

        self.horizontalLayout_202.addWidget(self.pump7_reverse)


        self.verticalLayout_200.addLayout(self.horizontalLayout_202)

        self.horizontalLayout_203 = QHBoxLayout()
        self.horizontalLayout_203.setObjectName(u"horizontalLayout_203")
        self.pump8_label = QLabel(self.layoutWidget1)
        self.pump8_label.setObjectName(u"pump8_label")

        self.horizontalLayout_203.addWidget(self.pump8_label)

        self.pump8_spinbox = QSpinBox(self.layoutWidget1)
        self.pump8_spinbox.setObjectName(u"pump8_spinbox")
        self.pump8_spinbox.setMaximum(300)

        self.horizontalLayout_203.addWidget(self.pump8_spinbox)

        self.pump8_open_button = QPushButton(self.layoutWidget1)
        self.pump8_open_button.setObjectName(u"pump8_open_button")

        self.horizontalLayout_203.addWidget(self.pump8_open_button)

        self.pump8_stop_button = QPushButton(self.layoutWidget1)
        self.pump8_stop_button.setObjectName(u"pump8_stop_button")

        self.horizontalLayout_203.addWidget(self.pump8_stop_button)

        self.pump8_reverse = QPushButton(self.layoutWidget1)
        self.pump8_reverse.setObjectName(u"pump8_reverse")

        self.horizontalLayout_203.addWidget(self.pump8_reverse)


        self.verticalLayout_200.addLayout(self.horizontalLayout_203)

        self.horizontalLayout_204 = QHBoxLayout()
        self.horizontalLayout_204.setObjectName(u"horizontalLayout_204")
        self.unit2_wash = QLabel(self.layoutWidget1)
        self.unit2_wash.setObjectName(u"unit2_wash")

        self.horizontalLayout_204.addWidget(self.unit2_wash)

        self.unit2_wash_spinbox = QSpinBox(self.layoutWidget1)
        self.unit2_wash_spinbox.setObjectName(u"unit2_wash_spinbox")
        self.unit2_wash_spinbox.setMaximum(300)

        self.horizontalLayout_204.addWidget(self.unit2_wash_spinbox)

        self.unit2_wash_open_button = QPushButton(self.layoutWidget1)
        self.unit2_wash_open_button.setObjectName(u"unit2_wash_open_button")

        self.horizontalLayout_204.addWidget(self.unit2_wash_open_button)

        self.unit2_wahs_stop_button = QPushButton(self.layoutWidget1)
        self.unit2_wahs_stop_button.setObjectName(u"unit2_wahs_stop_button")

        self.horizontalLayout_204.addWidget(self.unit2_wahs_stop_button)

        self.unit2_reverse = QPushButton(self.layoutWidget1)
        self.unit2_reverse.setObjectName(u"unit2_reverse")

        self.horizontalLayout_204.addWidget(self.unit2_reverse)


        self.verticalLayout_200.addLayout(self.horizontalLayout_204)

        self.horizontalLayout_205 = QHBoxLayout()
        self.horizontalLayout_205.setObjectName(u"horizontalLayout_205")
        self.unit2_waste_label = QLabel(self.layoutWidget1)
        self.unit2_waste_label.setObjectName(u"unit2_waste_label")

        self.horizontalLayout_205.addWidget(self.unit2_waste_label)

        self.unit2_waste_spinbox = QSpinBox(self.layoutWidget1)
        self.unit2_waste_spinbox.setObjectName(u"unit2_waste_spinbox")
        self.unit2_waste_spinbox.setMaximum(300)

        self.horizontalLayout_205.addWidget(self.unit2_waste_spinbox)

        self.unit2_waste_open_button = QPushButton(self.layoutWidget1)
        self.unit2_waste_open_button.setObjectName(u"unit2_waste_open_button")

        self.horizontalLayout_205.addWidget(self.unit2_waste_open_button)

        self.unit2_waste_stop_button = QPushButton(self.layoutWidget1)
        self.unit2_waste_stop_button.setObjectName(u"unit2_waste_stop_button")

        self.horizontalLayout_205.addWidget(self.unit2_waste_stop_button)

        self.unit2_waste_reverse = QPushButton(self.layoutWidget1)
        self.unit2_waste_reverse.setObjectName(u"unit2_waste_reverse")

        self.horizontalLayout_205.addWidget(self.unit2_waste_reverse)


        self.verticalLayout_200.addLayout(self.horizontalLayout_205)

        self.horizontalLayout_206 = QHBoxLayout()
        self.horizontalLayout_206.setSpacing(10)
        self.horizontalLayout_206.setObjectName(u"horizontalLayout_206")
        self.unit2_depro_label = QLabel(self.layoutWidget1)
        self.unit2_depro_label.setObjectName(u"unit2_depro_label")

        self.horizontalLayout_206.addWidget(self.unit2_depro_label)

        self.unit2_depro_start_button = QPushButton(self.layoutWidget1)
        self.unit2_depro_start_button.setObjectName(u"unit2_depro_start_button")

        self.horizontalLayout_206.addWidget(self.unit2_depro_start_button)

        self.unit2_depro_stop_button = QPushButton(self.layoutWidget1)
        self.unit2_depro_stop_button.setObjectName(u"unit2_depro_stop_button")

        self.horizontalLayout_206.addWidget(self.unit2_depro_stop_button)

        self.horizontalLayout_206.setStretch(0, 3)
        self.horizontalLayout_206.setStretch(1, 2)
        self.horizontalLayout_206.setStretch(2, 2)

        self.verticalLayout_200.addLayout(self.horizontalLayout_206)

        self.horizontalLayout_207 = QHBoxLayout()
        self.horizontalLayout_207.setObjectName(u"horizontalLayout_207")
        self.horizontalLayout_207.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.unit2_couple_label = QLabel(self.layoutWidget1)
        self.unit2_couple_label.setObjectName(u"unit2_couple_label")

        self.horizontalLayout_207.addWidget(self.unit2_couple_label)

        self.unit2_couple_start_button = QPushButton(self.layoutWidget1)
        self.unit2_couple_start_button.setObjectName(u"unit2_couple_start_button")

        self.horizontalLayout_207.addWidget(self.unit2_couple_start_button)

        self.unit2_couple__stop_button = QPushButton(self.layoutWidget1)
        self.unit2_couple__stop_button.setObjectName(u"unit2_couple__stop_button")

        self.horizontalLayout_207.addWidget(self.unit2_couple__stop_button)

        self.horizontalLayout_207.setStretch(0, 3)
        self.horizontalLayout_207.setStretch(1, 2)
        self.horizontalLayout_207.setStretch(2, 2)

        self.verticalLayout_200.addLayout(self.horizontalLayout_207)

        self.horizontalLayout_208 = QHBoxLayout()
        self.horizontalLayout_208.setObjectName(u"horizontalLayout_208")
        self.unit2_wash_label = QLabel(self.layoutWidget1)
        self.unit2_wash_label.setObjectName(u"unit2_wash_label")

        self.horizontalLayout_208.addWidget(self.unit2_wash_label)

        self.unit2_wash_frequence_sppinbox = QSpinBox(self.layoutWidget1)
        self.unit2_wash_frequence_sppinbox.setObjectName(u"unit2_wash_frequence_sppinbox")
        self.unit2_wash_frequence_sppinbox.setMaximum(10)

        self.horizontalLayout_208.addWidget(self.unit2_wash_frequence_sppinbox)

        self.unit2_wash_start_button = QPushButton(self.layoutWidget1)
        self.unit2_wash_start_button.setObjectName(u"unit2_wash_start_button")

        self.horizontalLayout_208.addWidget(self.unit2_wash_start_button)

        self.horizontalLayout_208.setStretch(0, 3)
        self.horizontalLayout_208.setStretch(1, 2)
        self.horizontalLayout_208.setStretch(2, 2)

        self.verticalLayout_200.addLayout(self.horizontalLayout_208)

        self.toolBox.addItem(self.page_2, u"unit 2")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 399, 359))
        self.layoutWidget_4 = QWidget(self.page_3)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 10, 347, 244))
        self.verticalLayout_300 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_300.setObjectName(u"verticalLayout_300")
        self.verticalLayout_300.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_301 = QHBoxLayout()
        self.horizontalLayout_301.setObjectName(u"horizontalLayout_301")
        self.pump9_label = QLabel(self.layoutWidget_4)
        self.pump9_label.setObjectName(u"pump9_label")

        self.horizontalLayout_301.addWidget(self.pump9_label)

        self.pump9_spinbox = QSpinBox(self.layoutWidget_4)
        self.pump9_spinbox.setObjectName(u"pump9_spinbox")
        self.pump9_spinbox.setMaximum(300)

        self.horizontalLayout_301.addWidget(self.pump9_spinbox)

        self.pump9_open_button = QPushButton(self.layoutWidget_4)
        self.pump9_open_button.setObjectName(u"pump9_open_button")

        self.horizontalLayout_301.addWidget(self.pump9_open_button)

        self.pump9_stop_button = QPushButton(self.layoutWidget_4)
        self.pump9_stop_button.setObjectName(u"pump9_stop_button")

        self.horizontalLayout_301.addWidget(self.pump9_stop_button)

        self.pump9_reverse = QPushButton(self.layoutWidget_4)
        self.pump9_reverse.setObjectName(u"pump9_reverse")

        self.horizontalLayout_301.addWidget(self.pump9_reverse)


        self.verticalLayout_300.addLayout(self.horizontalLayout_301)

        self.horizontalLayout_302 = QHBoxLayout()
        self.horizontalLayout_302.setObjectName(u"horizontalLayout_302")
        self.pump10_label = QLabel(self.layoutWidget_4)
        self.pump10_label.setObjectName(u"pump10_label")

        self.horizontalLayout_302.addWidget(self.pump10_label)

        self.pump10_spinbox = QSpinBox(self.layoutWidget_4)
        self.pump10_spinbox.setObjectName(u"pump10_spinbox")
        self.pump10_spinbox.setMaximum(300)

        self.horizontalLayout_302.addWidget(self.pump10_spinbox)

        self.pump10_open_button = QPushButton(self.layoutWidget_4)
        self.pump10_open_button.setObjectName(u"pump10_open_button")

        self.horizontalLayout_302.addWidget(self.pump10_open_button)

        self.pump10_stop_button = QPushButton(self.layoutWidget_4)
        self.pump10_stop_button.setObjectName(u"pump10_stop_button")

        self.horizontalLayout_302.addWidget(self.pump10_stop_button)

        self.pump10_reverse = QPushButton(self.layoutWidget_4)
        self.pump10_reverse.setObjectName(u"pump10_reverse")

        self.horizontalLayout_302.addWidget(self.pump10_reverse)


        self.verticalLayout_300.addLayout(self.horizontalLayout_302)

        self.horizontalLayout_303 = QHBoxLayout()
        self.horizontalLayout_303.setObjectName(u"horizontalLayout_303")
        self.pump11_label = QLabel(self.layoutWidget_4)
        self.pump11_label.setObjectName(u"pump11_label")

        self.horizontalLayout_303.addWidget(self.pump11_label)

        self.pump11_spinbox = QSpinBox(self.layoutWidget_4)
        self.pump11_spinbox.setObjectName(u"pump11_spinbox")
        self.pump11_spinbox.setMaximum(300)

        self.horizontalLayout_303.addWidget(self.pump11_spinbox)

        self.pump11_open_button = QPushButton(self.layoutWidget_4)
        self.pump11_open_button.setObjectName(u"pump11_open_button")

        self.horizontalLayout_303.addWidget(self.pump11_open_button)

        self.pump11_stop_button = QPushButton(self.layoutWidget_4)
        self.pump11_stop_button.setObjectName(u"pump11_stop_button")

        self.horizontalLayout_303.addWidget(self.pump11_stop_button)

        self.pump11_reverse = QPushButton(self.layoutWidget_4)
        self.pump11_reverse.setObjectName(u"pump11_reverse")

        self.horizontalLayout_303.addWidget(self.pump11_reverse)


        self.verticalLayout_300.addLayout(self.horizontalLayout_303)

        self.horizontalLayout_304 = QHBoxLayout()
        self.horizontalLayout_304.setObjectName(u"horizontalLayout_304")
        self.unit3_wash = QLabel(self.layoutWidget_4)
        self.unit3_wash.setObjectName(u"unit3_wash")

        self.horizontalLayout_304.addWidget(self.unit3_wash)

        self.unit3_wash_spinbox = QSpinBox(self.layoutWidget_4)
        self.unit3_wash_spinbox.setObjectName(u"unit3_wash_spinbox")
        self.unit3_wash_spinbox.setMaximum(300)

        self.horizontalLayout_304.addWidget(self.unit3_wash_spinbox)

        self.unit3_wash_open_button = QPushButton(self.layoutWidget_4)
        self.unit3_wash_open_button.setObjectName(u"unit3_wash_open_button")

        self.horizontalLayout_304.addWidget(self.unit3_wash_open_button)

        self.unit3_wahs_stop_button = QPushButton(self.layoutWidget_4)
        self.unit3_wahs_stop_button.setObjectName(u"unit3_wahs_stop_button")

        self.horizontalLayout_304.addWidget(self.unit3_wahs_stop_button)

        self.unit3_reverse = QPushButton(self.layoutWidget_4)
        self.unit3_reverse.setObjectName(u"unit3_reverse")

        self.horizontalLayout_304.addWidget(self.unit3_reverse)


        self.verticalLayout_300.addLayout(self.horizontalLayout_304)

        self.horizontalLayout_305 = QHBoxLayout()
        self.horizontalLayout_305.setObjectName(u"horizontalLayout_305")
        self.unit3_waste_label = QLabel(self.layoutWidget_4)
        self.unit3_waste_label.setObjectName(u"unit3_waste_label")

        self.horizontalLayout_305.addWidget(self.unit3_waste_label)

        self.unit3_waste_spinbox = QSpinBox(self.layoutWidget_4)
        self.unit3_waste_spinbox.setObjectName(u"unit3_waste_spinbox")
        self.unit3_waste_spinbox.setMaximum(300)

        self.horizontalLayout_305.addWidget(self.unit3_waste_spinbox)

        self.unit3_waste_open_button = QPushButton(self.layoutWidget_4)
        self.unit3_waste_open_button.setObjectName(u"unit3_waste_open_button")

        self.horizontalLayout_305.addWidget(self.unit3_waste_open_button)

        self.unit3_waste_stop_button = QPushButton(self.layoutWidget_4)
        self.unit3_waste_stop_button.setObjectName(u"unit3_waste_stop_button")

        self.horizontalLayout_305.addWidget(self.unit3_waste_stop_button)

        self.unit3_waste_reverse = QPushButton(self.layoutWidget_4)
        self.unit3_waste_reverse.setObjectName(u"unit3_waste_reverse")

        self.horizontalLayout_305.addWidget(self.unit3_waste_reverse)


        self.verticalLayout_300.addLayout(self.horizontalLayout_305)

        self.horizontalLayout_306 = QHBoxLayout()
        self.horizontalLayout_306.setSpacing(10)
        self.horizontalLayout_306.setObjectName(u"horizontalLayout_306")
        self.unit3_depro_label = QLabel(self.layoutWidget_4)
        self.unit3_depro_label.setObjectName(u"unit3_depro_label")

        self.horizontalLayout_306.addWidget(self.unit3_depro_label)

        self.unit3_depro_start_button = QPushButton(self.layoutWidget_4)
        self.unit3_depro_start_button.setObjectName(u"unit3_depro_start_button")

        self.horizontalLayout_306.addWidget(self.unit3_depro_start_button)

        self.unit3_depro_stop_button = QPushButton(self.layoutWidget_4)
        self.unit3_depro_stop_button.setObjectName(u"unit3_depro_stop_button")

        self.horizontalLayout_306.addWidget(self.unit3_depro_stop_button)

        self.horizontalLayout_306.setStretch(0, 3)
        self.horizontalLayout_306.setStretch(1, 2)
        self.horizontalLayout_306.setStretch(2, 2)

        self.verticalLayout_300.addLayout(self.horizontalLayout_306)

        self.horizontalLayout_307 = QHBoxLayout()
        self.horizontalLayout_307.setObjectName(u"horizontalLayout_307")
        self.horizontalLayout_307.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.unit3_couple_label = QLabel(self.layoutWidget_4)
        self.unit3_couple_label.setObjectName(u"unit3_couple_label")

        self.horizontalLayout_307.addWidget(self.unit3_couple_label)

        self.unit3_couple_start_button = QPushButton(self.layoutWidget_4)
        self.unit3_couple_start_button.setObjectName(u"unit3_couple_start_button")

        self.horizontalLayout_307.addWidget(self.unit3_couple_start_button)

        self.unit3_couple__stop_button = QPushButton(self.layoutWidget_4)
        self.unit3_couple__stop_button.setObjectName(u"unit3_couple__stop_button")

        self.horizontalLayout_307.addWidget(self.unit3_couple__stop_button)

        self.horizontalLayout_307.setStretch(0, 3)
        self.horizontalLayout_307.setStretch(1, 2)
        self.horizontalLayout_307.setStretch(2, 2)

        self.verticalLayout_300.addLayout(self.horizontalLayout_307)

        self.horizontalLayout_308 = QHBoxLayout()
        self.horizontalLayout_308.setObjectName(u"horizontalLayout_308")
        self.unit3_wash_label = QLabel(self.layoutWidget_4)
        self.unit3_wash_label.setObjectName(u"unit3_wash_label")

        self.horizontalLayout_308.addWidget(self.unit3_wash_label)

        self.unit3_wash_frequence_sppinbox = QSpinBox(self.layoutWidget_4)
        self.unit3_wash_frequence_sppinbox.setObjectName(u"unit3_wash_frequence_sppinbox")
        self.unit3_wash_frequence_sppinbox.setMaximum(10)

        self.horizontalLayout_308.addWidget(self.unit3_wash_frequence_sppinbox)

        self.unit3_start_wash_button = QPushButton(self.layoutWidget_4)
        self.unit3_start_wash_button.setObjectName(u"unit3_start_wash_button")

        self.horizontalLayout_308.addWidget(self.unit3_start_wash_button)

        self.horizontalLayout_308.setStretch(0, 3)
        self.horizontalLayout_308.setStretch(1, 2)
        self.horizontalLayout_308.setStretch(2, 2)

        self.verticalLayout_300.addLayout(self.horizontalLayout_308)

        self.toolBox.addItem(self.page_3, u"unit 3")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 399, 359))
        self.layoutWidget_5 = QWidget(self.page_4)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(10, 10, 347, 244))
        self.verticalLayout_400 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_400.setObjectName(u"verticalLayout_400")
        self.verticalLayout_400.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_401 = QHBoxLayout()
        self.horizontalLayout_401.setObjectName(u"horizontalLayout_401")
        self.pump12_label = QLabel(self.layoutWidget_5)
        self.pump12_label.setObjectName(u"pump12_label")

        self.horizontalLayout_401.addWidget(self.pump12_label)

        self.pump12_spinbox = QSpinBox(self.layoutWidget_5)
        self.pump12_spinbox.setObjectName(u"pump12_spinbox")
        self.pump12_spinbox.setMaximum(300)

        self.horizontalLayout_401.addWidget(self.pump12_spinbox)

        self.pump12_open_button = QPushButton(self.layoutWidget_5)
        self.pump12_open_button.setObjectName(u"pump12_open_button")

        self.horizontalLayout_401.addWidget(self.pump12_open_button)

        self.pump12_stop_button = QPushButton(self.layoutWidget_5)
        self.pump12_stop_button.setObjectName(u"pump12_stop_button")

        self.horizontalLayout_401.addWidget(self.pump12_stop_button)

        self.pump12_reverse = QPushButton(self.layoutWidget_5)
        self.pump12_reverse.setObjectName(u"pump12_reverse")

        self.horizontalLayout_401.addWidget(self.pump12_reverse)


        self.verticalLayout_400.addLayout(self.horizontalLayout_401)

        self.horizontalLayout_402 = QHBoxLayout()
        self.horizontalLayout_402.setObjectName(u"horizontalLayout_402")
        self.pump13_label = QLabel(self.layoutWidget_5)
        self.pump13_label.setObjectName(u"pump13_label")

        self.horizontalLayout_402.addWidget(self.pump13_label)

        self.pump13_spinbox = QSpinBox(self.layoutWidget_5)
        self.pump13_spinbox.setObjectName(u"pump13_spinbox")
        self.pump13_spinbox.setMaximum(300)

        self.horizontalLayout_402.addWidget(self.pump13_spinbox)

        self.pump13_open_button = QPushButton(self.layoutWidget_5)
        self.pump13_open_button.setObjectName(u"pump13_open_button")

        self.horizontalLayout_402.addWidget(self.pump13_open_button)

        self.pump13_stop_button = QPushButton(self.layoutWidget_5)
        self.pump13_stop_button.setObjectName(u"pump13_stop_button")

        self.horizontalLayout_402.addWidget(self.pump13_stop_button)

        self.pump13_reverse = QPushButton(self.layoutWidget_5)
        self.pump13_reverse.setObjectName(u"pump13_reverse")

        self.horizontalLayout_402.addWidget(self.pump13_reverse)


        self.verticalLayout_400.addLayout(self.horizontalLayout_402)

        self.horizontalLayout_403 = QHBoxLayout()
        self.horizontalLayout_403.setObjectName(u"horizontalLayout_403")
        self.pump14_label = QLabel(self.layoutWidget_5)
        self.pump14_label.setObjectName(u"pump14_label")

        self.horizontalLayout_403.addWidget(self.pump14_label)

        self.pump14_spinbox = QSpinBox(self.layoutWidget_5)
        self.pump14_spinbox.setObjectName(u"pump14_spinbox")
        self.pump14_spinbox.setMaximum(300)

        self.horizontalLayout_403.addWidget(self.pump14_spinbox)

        self.pump14_open_button = QPushButton(self.layoutWidget_5)
        self.pump14_open_button.setObjectName(u"pump14_open_button")

        self.horizontalLayout_403.addWidget(self.pump14_open_button)

        self.pump14_stop_button = QPushButton(self.layoutWidget_5)
        self.pump14_stop_button.setObjectName(u"pump14_stop_button")

        self.horizontalLayout_403.addWidget(self.pump14_stop_button)

        self.pump14_reverse = QPushButton(self.layoutWidget_5)
        self.pump14_reverse.setObjectName(u"pump14_reverse")

        self.horizontalLayout_403.addWidget(self.pump14_reverse)


        self.verticalLayout_400.addLayout(self.horizontalLayout_403)

        self.horizontalLayout_404 = QHBoxLayout()
        self.horizontalLayout_404.setObjectName(u"horizontalLayout_404")
        self.unit4_wash = QLabel(self.layoutWidget_5)
        self.unit4_wash.setObjectName(u"unit4_wash")

        self.horizontalLayout_404.addWidget(self.unit4_wash)

        self.unit4_wash_spinbox = QSpinBox(self.layoutWidget_5)
        self.unit4_wash_spinbox.setObjectName(u"unit4_wash_spinbox")
        self.unit4_wash_spinbox.setMaximum(300)

        self.horizontalLayout_404.addWidget(self.unit4_wash_spinbox)

        self.unit4_wash_open_button = QPushButton(self.layoutWidget_5)
        self.unit4_wash_open_button.setObjectName(u"unit4_wash_open_button")

        self.horizontalLayout_404.addWidget(self.unit4_wash_open_button)

        self.unit4_wahs_stop_button = QPushButton(self.layoutWidget_5)
        self.unit4_wahs_stop_button.setObjectName(u"unit4_wahs_stop_button")

        self.horizontalLayout_404.addWidget(self.unit4_wahs_stop_button)

        self.unit4_reverse = QPushButton(self.layoutWidget_5)
        self.unit4_reverse.setObjectName(u"unit4_reverse")

        self.horizontalLayout_404.addWidget(self.unit4_reverse)


        self.verticalLayout_400.addLayout(self.horizontalLayout_404)

        self.horizontalLayout_405 = QHBoxLayout()
        self.horizontalLayout_405.setObjectName(u"horizontalLayout_405")
        self.unit4_waste_label = QLabel(self.layoutWidget_5)
        self.unit4_waste_label.setObjectName(u"unit4_waste_label")

        self.horizontalLayout_405.addWidget(self.unit4_waste_label)

        self.unit4_waste_spinbox = QSpinBox(self.layoutWidget_5)
        self.unit4_waste_spinbox.setObjectName(u"unit4_waste_spinbox")
        self.unit4_waste_spinbox.setMaximum(300)

        self.horizontalLayout_405.addWidget(self.unit4_waste_spinbox)

        self.unit4_waste_open_button = QPushButton(self.layoutWidget_5)
        self.unit4_waste_open_button.setObjectName(u"unit4_waste_open_button")

        self.horizontalLayout_405.addWidget(self.unit4_waste_open_button)

        self.unit4_waste_stop_button = QPushButton(self.layoutWidget_5)
        self.unit4_waste_stop_button.setObjectName(u"unit4_waste_stop_button")

        self.horizontalLayout_405.addWidget(self.unit4_waste_stop_button)

        self.unit4_waste_reverse = QPushButton(self.layoutWidget_5)
        self.unit4_waste_reverse.setObjectName(u"unit4_waste_reverse")

        self.horizontalLayout_405.addWidget(self.unit4_waste_reverse)


        self.verticalLayout_400.addLayout(self.horizontalLayout_405)

        self.horizontalLayout_406 = QHBoxLayout()
        self.horizontalLayout_406.setSpacing(10)
        self.horizontalLayout_406.setObjectName(u"horizontalLayout_406")
        self.unit4_depro_label = QLabel(self.layoutWidget_5)
        self.unit4_depro_label.setObjectName(u"unit4_depro_label")

        self.horizontalLayout_406.addWidget(self.unit4_depro_label)

        self.unit4_depro_start_button = QPushButton(self.layoutWidget_5)
        self.unit4_depro_start_button.setObjectName(u"unit4_depro_start_button")

        self.horizontalLayout_406.addWidget(self.unit4_depro_start_button)

        self.unit4_depro_stop_button = QPushButton(self.layoutWidget_5)
        self.unit4_depro_stop_button.setObjectName(u"unit4_depro_stop_button")

        self.horizontalLayout_406.addWidget(self.unit4_depro_stop_button)

        self.horizontalLayout_406.setStretch(0, 3)
        self.horizontalLayout_406.setStretch(1, 2)
        self.horizontalLayout_406.setStretch(2, 2)

        self.verticalLayout_400.addLayout(self.horizontalLayout_406)

        self.horizontalLayout_407 = QHBoxLayout()
        self.horizontalLayout_407.setObjectName(u"horizontalLayout_407")
        self.horizontalLayout_407.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.unit4_couple_label = QLabel(self.layoutWidget_5)
        self.unit4_couple_label.setObjectName(u"unit4_couple_label")

        self.horizontalLayout_407.addWidget(self.unit4_couple_label)

        self.unit4_couple_start_button = QPushButton(self.layoutWidget_5)
        self.unit4_couple_start_button.setObjectName(u"unit4_couple_start_button")

        self.horizontalLayout_407.addWidget(self.unit4_couple_start_button)

        self.unit4_couple__stop_button = QPushButton(self.layoutWidget_5)
        self.unit4_couple__stop_button.setObjectName(u"unit4_couple__stop_button")

        self.horizontalLayout_407.addWidget(self.unit4_couple__stop_button)

        self.horizontalLayout_407.setStretch(0, 3)
        self.horizontalLayout_407.setStretch(1, 2)
        self.horizontalLayout_407.setStretch(2, 2)

        self.verticalLayout_400.addLayout(self.horizontalLayout_407)

        self.horizontalLayout_408 = QHBoxLayout()
        self.horizontalLayout_408.setObjectName(u"horizontalLayout_408")
        self.unit4_wash_label = QLabel(self.layoutWidget_5)
        self.unit4_wash_label.setObjectName(u"unit4_wash_label")

        self.horizontalLayout_408.addWidget(self.unit4_wash_label)

        self.unit4_wash_frequence_sppinbox = QSpinBox(self.layoutWidget_5)
        self.unit4_wash_frequence_sppinbox.setObjectName(u"unit4_wash_frequence_sppinbox")
        self.unit4_wash_frequence_sppinbox.setMaximum(10)

        self.horizontalLayout_408.addWidget(self.unit4_wash_frequence_sppinbox)

        self.unit4_start_wash_button = QPushButton(self.layoutWidget_5)
        self.unit4_start_wash_button.setObjectName(u"unit4_start_wash_button")

        self.horizontalLayout_408.addWidget(self.unit4_start_wash_button)

        self.horizontalLayout_408.setStretch(0, 3)
        self.horizontalLayout_408.setStretch(1, 2)
        self.horizontalLayout_408.setStretch(2, 2)

        self.verticalLayout_400.addLayout(self.horizontalLayout_408)

        self.toolBox.addItem(self.page_4, u"unit 4")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 399, 359))
        self.layoutWidget_6 = QWidget(self.page_5)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(10, 10, 347, 244))
        self.verticalLayout_500 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_500.setObjectName(u"verticalLayout_500")
        self.verticalLayout_500.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_501 = QHBoxLayout()
        self.horizontalLayout_501.setObjectName(u"horizontalLayout_501")
        self.pump15_label = QLabel(self.layoutWidget_6)
        self.pump15_label.setObjectName(u"pump15_label")

        self.horizontalLayout_501.addWidget(self.pump15_label)

        self.pump15_spinbox = QSpinBox(self.layoutWidget_6)
        self.pump15_spinbox.setObjectName(u"pump15_spinbox")
        self.pump15_spinbox.setMaximum(300)

        self.horizontalLayout_501.addWidget(self.pump15_spinbox)

        self.pump15_open_button = QPushButton(self.layoutWidget_6)
        self.pump15_open_button.setObjectName(u"pump15_open_button")

        self.horizontalLayout_501.addWidget(self.pump15_open_button)

        self.pump15_stop_button = QPushButton(self.layoutWidget_6)
        self.pump15_stop_button.setObjectName(u"pump15_stop_button")

        self.horizontalLayout_501.addWidget(self.pump15_stop_button)

        self.pump15_reverse = QPushButton(self.layoutWidget_6)
        self.pump15_reverse.setObjectName(u"pump15_reverse")

        self.horizontalLayout_501.addWidget(self.pump15_reverse)


        self.verticalLayout_500.addLayout(self.horizontalLayout_501)

        self.horizontalLayout_502 = QHBoxLayout()
        self.horizontalLayout_502.setObjectName(u"horizontalLayout_502")
        self.pump16_label = QLabel(self.layoutWidget_6)
        self.pump16_label.setObjectName(u"pump16_label")

        self.horizontalLayout_502.addWidget(self.pump16_label)

        self.pump16_spinbox = QSpinBox(self.layoutWidget_6)
        self.pump16_spinbox.setObjectName(u"pump16_spinbox")
        self.pump16_spinbox.setMaximum(300)

        self.horizontalLayout_502.addWidget(self.pump16_spinbox)

        self.pump16_open_button = QPushButton(self.layoutWidget_6)
        self.pump16_open_button.setObjectName(u"pump16_open_button")

        self.horizontalLayout_502.addWidget(self.pump16_open_button)

        self.pump16_stop_button = QPushButton(self.layoutWidget_6)
        self.pump16_stop_button.setObjectName(u"pump16_stop_button")

        self.horizontalLayout_502.addWidget(self.pump16_stop_button)

        self.pump16_reverse = QPushButton(self.layoutWidget_6)
        self.pump16_reverse.setObjectName(u"pump16_reverse")

        self.horizontalLayout_502.addWidget(self.pump16_reverse)


        self.verticalLayout_500.addLayout(self.horizontalLayout_502)

        self.horizontalLayout_503 = QHBoxLayout()
        self.horizontalLayout_503.setObjectName(u"horizontalLayout_503")
        self.pump17_label = QLabel(self.layoutWidget_6)
        self.pump17_label.setObjectName(u"pump17_label")

        self.horizontalLayout_503.addWidget(self.pump17_label)

        self.pump17_spinbox = QSpinBox(self.layoutWidget_6)
        self.pump17_spinbox.setObjectName(u"pump17_spinbox")
        self.pump17_spinbox.setMaximum(300)

        self.horizontalLayout_503.addWidget(self.pump17_spinbox)

        self.pump17_open_button = QPushButton(self.layoutWidget_6)
        self.pump17_open_button.setObjectName(u"pump17_open_button")

        self.horizontalLayout_503.addWidget(self.pump17_open_button)

        self.pump17_stop_button = QPushButton(self.layoutWidget_6)
        self.pump17_stop_button.setObjectName(u"pump17_stop_button")

        self.horizontalLayout_503.addWidget(self.pump17_stop_button)

        self.pump17_reverse = QPushButton(self.layoutWidget_6)
        self.pump17_reverse.setObjectName(u"pump17_reverse")

        self.horizontalLayout_503.addWidget(self.pump17_reverse)


        self.verticalLayout_500.addLayout(self.horizontalLayout_503)

        self.horizontalLayout_504 = QHBoxLayout()
        self.horizontalLayout_504.setObjectName(u"horizontalLayout_504")
        self.unit5_wash = QLabel(self.layoutWidget_6)
        self.unit5_wash.setObjectName(u"unit5_wash")

        self.horizontalLayout_504.addWidget(self.unit5_wash)

        self.unit5_wash_spinbox = QSpinBox(self.layoutWidget_6)
        self.unit5_wash_spinbox.setObjectName(u"unit5_wash_spinbox")
        self.unit5_wash_spinbox.setMaximum(300)

        self.horizontalLayout_504.addWidget(self.unit5_wash_spinbox)

        self.unit5_wash_open_button = QPushButton(self.layoutWidget_6)
        self.unit5_wash_open_button.setObjectName(u"unit5_wash_open_button")

        self.horizontalLayout_504.addWidget(self.unit5_wash_open_button)

        self.unit5_wahs_stop_button = QPushButton(self.layoutWidget_6)
        self.unit5_wahs_stop_button.setObjectName(u"unit5_wahs_stop_button")

        self.horizontalLayout_504.addWidget(self.unit5_wahs_stop_button)

        self.unit5_reverse = QPushButton(self.layoutWidget_6)
        self.unit5_reverse.setObjectName(u"unit5_reverse")

        self.horizontalLayout_504.addWidget(self.unit5_reverse)


        self.verticalLayout_500.addLayout(self.horizontalLayout_504)

        self.horizontalLayout_505 = QHBoxLayout()
        self.horizontalLayout_505.setObjectName(u"horizontalLayout_505")
        self.unit5_waste_label = QLabel(self.layoutWidget_6)
        self.unit5_waste_label.setObjectName(u"unit5_waste_label")

        self.horizontalLayout_505.addWidget(self.unit5_waste_label)

        self.unit5_waste_spinbox = QSpinBox(self.layoutWidget_6)
        self.unit5_waste_spinbox.setObjectName(u"unit5_waste_spinbox")
        self.unit5_waste_spinbox.setMaximum(300)

        self.horizontalLayout_505.addWidget(self.unit5_waste_spinbox)

        self.unit5_waste_open_button = QPushButton(self.layoutWidget_6)
        self.unit5_waste_open_button.setObjectName(u"unit5_waste_open_button")

        self.horizontalLayout_505.addWidget(self.unit5_waste_open_button)

        self.unit5_waste_stop_button = QPushButton(self.layoutWidget_6)
        self.unit5_waste_stop_button.setObjectName(u"unit5_waste_stop_button")

        self.horizontalLayout_505.addWidget(self.unit5_waste_stop_button)

        self.unit5_waste_reverse = QPushButton(self.layoutWidget_6)
        self.unit5_waste_reverse.setObjectName(u"unit5_waste_reverse")

        self.horizontalLayout_505.addWidget(self.unit5_waste_reverse)


        self.verticalLayout_500.addLayout(self.horizontalLayout_505)

        self.horizontalLayout_506 = QHBoxLayout()
        self.horizontalLayout_506.setSpacing(10)
        self.horizontalLayout_506.setObjectName(u"horizontalLayout_506")
        self.unit5_depro_label = QLabel(self.layoutWidget_6)
        self.unit5_depro_label.setObjectName(u"unit5_depro_label")

        self.horizontalLayout_506.addWidget(self.unit5_depro_label)

        self.unit5_depro_start_button = QPushButton(self.layoutWidget_6)
        self.unit5_depro_start_button.setObjectName(u"unit5_depro_start_button")

        self.horizontalLayout_506.addWidget(self.unit5_depro_start_button)

        self.unit5_depro_stop_button = QPushButton(self.layoutWidget_6)
        self.unit5_depro_stop_button.setObjectName(u"unit5_depro_stop_button")

        self.horizontalLayout_506.addWidget(self.unit5_depro_stop_button)

        self.horizontalLayout_506.setStretch(0, 3)
        self.horizontalLayout_506.setStretch(1, 2)
        self.horizontalLayout_506.setStretch(2, 2)

        self.verticalLayout_500.addLayout(self.horizontalLayout_506)

        self.horizontalLayout_507 = QHBoxLayout()
        self.horizontalLayout_507.setObjectName(u"horizontalLayout_507")
        self.horizontalLayout_507.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.unit5_couple_label = QLabel(self.layoutWidget_6)
        self.unit5_couple_label.setObjectName(u"unit5_couple_label")

        self.horizontalLayout_507.addWidget(self.unit5_couple_label)

        self.unit5_couple_start_button = QPushButton(self.layoutWidget_6)
        self.unit5_couple_start_button.setObjectName(u"unit5_couple_start_button")

        self.horizontalLayout_507.addWidget(self.unit5_couple_start_button)

        self.unit5_couple__stop_button = QPushButton(self.layoutWidget_6)
        self.unit5_couple__stop_button.setObjectName(u"unit5_couple__stop_button")

        self.horizontalLayout_507.addWidget(self.unit5_couple__stop_button)

        self.horizontalLayout_507.setStretch(0, 3)
        self.horizontalLayout_507.setStretch(1, 2)
        self.horizontalLayout_507.setStretch(2, 2)

        self.verticalLayout_500.addLayout(self.horizontalLayout_507)

        self.horizontalLayout_508 = QHBoxLayout()
        self.horizontalLayout_508.setObjectName(u"horizontalLayout_508")
        self.unit5_wash_label = QLabel(self.layoutWidget_6)
        self.unit5_wash_label.setObjectName(u"unit5_wash_label")

        self.horizontalLayout_508.addWidget(self.unit5_wash_label)

        self.unit5_wash_frequence_sppinbox = QSpinBox(self.layoutWidget_6)
        self.unit5_wash_frequence_sppinbox.setObjectName(u"unit5_wash_frequence_sppinbox")
        self.unit5_wash_frequence_sppinbox.setMaximum(10)

        self.horizontalLayout_508.addWidget(self.unit5_wash_frequence_sppinbox)

        self.unit5_wash_start_button = QPushButton(self.layoutWidget_6)
        self.unit5_wash_start_button.setObjectName(u"unit5_wash_start_button")

        self.horizontalLayout_508.addWidget(self.unit5_wash_start_button)

        self.horizontalLayout_508.setStretch(0, 3)
        self.horizontalLayout_508.setStretch(1, 2)
        self.horizontalLayout_508.setStretch(2, 2)

        self.verticalLayout_500.addLayout(self.horizontalLayout_508)

        self.toolBox.addItem(self.page_5, u"unit5")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setGeometry(QRect(0, 0, 399, 359))
        self.layoutWidget2 = QWidget(self.page_6)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 21, 313, 120))
        self.verticalLayout = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.value1_label = QLabel(self.layoutWidget2)
        self.value1_label.setObjectName(u"value1_label")

        self.horizontalLayout_7.addWidget(self.value1_label)

        self.value1_spinbox = QSpinBox(self.layoutWidget2)
        self.value1_spinbox.setObjectName(u"value1_spinbox")
        self.value1_spinbox.setMinimum(1)
        self.value1_spinbox.setMaximum(7)

        self.horizontalLayout_7.addWidget(self.value1_spinbox)

        self.value1_open_button = QPushButton(self.layoutWidget2)
        self.value1_open_button.setObjectName(u"value1_open_button")

        self.horizontalLayout_7.addWidget(self.value1_open_button)

        self.value1_stop_button = QPushButton(self.layoutWidget2)
        self.value1_stop_button.setObjectName(u"value1_stop_button")

        self.horizontalLayout_7.addWidget(self.value1_stop_button)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.value2_label = QLabel(self.layoutWidget2)
        self.value2_label.setObjectName(u"value2_label")

        self.horizontalLayout_8.addWidget(self.value2_label)

        self.value2_spinbox = QSpinBox(self.layoutWidget2)
        self.value2_spinbox.setObjectName(u"value2_spinbox")
        self.value2_spinbox.setMinimum(1)
        self.value2_spinbox.setMaximum(7)

        self.horizontalLayout_8.addWidget(self.value2_spinbox)

        self.value2_open_button = QPushButton(self.layoutWidget2)
        self.value2_open_button.setObjectName(u"value2_open_button")

        self.horizontalLayout_8.addWidget(self.value2_open_button)

        self.value2_stop_button = QPushButton(self.layoutWidget2)
        self.value2_stop_button.setObjectName(u"value2_stop_button")

        self.horizontalLayout_8.addWidget(self.value2_stop_button)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pressure_time_label = QLabel(self.layoutWidget2)
        self.pressure_time_label.setObjectName(u"pressure_time_label")

        self.horizontalLayout_14.addWidget(self.pressure_time_label)

        self.pressure_time = QLineEdit(self.layoutWidget2)
        self.pressure_time.setObjectName(u"pressure_time")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pressure_time.sizePolicy().hasHeightForWidth())
        self.pressure_time.setSizePolicy(sizePolicy1)

        self.horizontalLayout_14.addWidget(self.pressure_time)

        self.pressure_start = QPushButton(self.layoutWidget2)
        self.pressure_start.setObjectName(u"pressure_start")

        self.horizontalLayout_14.addWidget(self.pressure_start)

        self.horizontalLayout_14.setStretch(0, 4)
        self.horizontalLayout_14.setStretch(1, 9)
        self.horizontalLayout_14.setStretch(2, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setSizeConstraint(QLayout.SetFixedSize)
        self.file_name_label = QLabel(self.layoutWidget2)
        self.file_name_label.setObjectName(u"file_name_label")

        self.horizontalLayout_15.addWidget(self.file_name_label)

        self.file_name = QLineEdit(self.layoutWidget2)
        self.file_name.setObjectName(u"file_name")
        sizePolicy1.setHeightForWidth(self.file_name.sizePolicy().hasHeightForWidth())
        self.file_name.setSizePolicy(sizePolicy1)

        self.horizontalLayout_15.addWidget(self.file_name)

        self.pressure_display = QPushButton(self.layoutWidget2)
        self.pressure_display.setObjectName(u"pressure_display")

        self.horizontalLayout_15.addWidget(self.pressure_display)

        self.horizontalLayout_15.setStretch(0, 4)
        self.horizontalLayout_15.setStretch(1, 9)
        self.horizontalLayout_15.setStretch(2, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_15)

        self.layoutWidget_2 = QWidget(self.page_6)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 250, 200, 102))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.value2_label_2 = QLabel(self.layoutWidget_2)
        self.value2_label_2.setObjectName(u"value2_label_2")

        self.horizontalLayout_2.addWidget(self.value2_label_2)

        self.valeu2_passage_label = QLabel(self.layoutWidget_2)
        self.valeu2_passage_label.setObjectName(u"valeu2_passage_label")

        self.horizontalLayout_2.addWidget(self.valeu2_passage_label)

        self.value2_dial = QDial(self.layoutWidget_2)
        self.value2_dial.setObjectName(u"value2_dial")
        self.value2_dial.setMinimum(1)
        self.value2_dial.setMaximum(6)
        self.value2_dial.setNotchesVisible(True)

        self.horizontalLayout_2.addWidget(self.value2_dial)

        self.layoutWidget3 = QWidget(self.page_6)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 150, 200, 102))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.value1_label_2 = QLabel(self.layoutWidget3)
        self.value1_label_2.setObjectName(u"value1_label_2")

        self.horizontalLayout.addWidget(self.value1_label_2)

        self.value1_passage_label = QLabel(self.layoutWidget3)
        self.value1_passage_label.setObjectName(u"value1_passage_label")

        self.horizontalLayout.addWidget(self.value1_passage_label)

        self.value1_dial = QDial(self.layoutWidget3)
        self.value1_dial.setObjectName(u"value1_dial")
        self.value1_dial.setMinimum(1)
        self.value1_dial.setMaximum(6)
        self.value1_dial.setNotchesVisible(True)

        self.horizontalLayout.addWidget(self.value1_dial)

        self.toolBox.addItem(self.page_6, u"value")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.page_7.setGeometry(QRect(0, 0, 399, 359))
        self.layoutWidget_3 = QWidget(self.page_7)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(5, 20, 351, 311))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tepro_vol_label = QLabel(self.layoutWidget_3)
        self.tepro_vol_label.setObjectName(u"tepro_vol_label")

        self.horizontalLayout_6.addWidget(self.tepro_vol_label)

        self.horizontalSpacer_8 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.tepro_vol_spinBox = QSpinBox(self.layoutWidget_3)
        self.tepro_vol_spinBox.setObjectName(u"tepro_vol_spinBox")
        self.tepro_vol_spinBox.setSingleStep(1)
        self.tepro_vol_spinBox.setValue(10)

        self.horizontalLayout_6.addWidget(self.tepro_vol_spinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.couple_vol_label = QLabel(self.layoutWidget_3)
        self.couple_vol_label.setObjectName(u"couple_vol_label")

        self.horizontalLayout_4.addWidget(self.couple_vol_label)

        self.horizontalSpacer_4 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.couple_vol_spinBox = QSpinBox(self.layoutWidget_3)
        self.couple_vol_spinBox.setObjectName(u"couple_vol_spinBox")
        self.couple_vol_spinBox.setValue(10)

        self.horizontalLayout_4.addWidget(self.couple_vol_spinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tepro_time_label = QLabel(self.layoutWidget_3)
        self.tepro_time_label.setObjectName(u"tepro_time_label")

        self.horizontalLayout_3.addWidget(self.tepro_time_label)

        self.horizontalSpacer_5 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.tepro_time_spinBox = QSpinBox(self.layoutWidget_3)
        self.tepro_time_spinBox.setObjectName(u"tepro_time_spinBox")
        self.tepro_time_spinBox.setValue(2)

        self.horizontalLayout_3.addWidget(self.tepro_time_spinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.couple_time_label = QLabel(self.layoutWidget_3)
        self.couple_time_label.setObjectName(u"couple_time_label")

        self.horizontalLayout_10.addWidget(self.couple_time_label)

        self.horizontalSpacer_6 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.couple_time_spinBox = QSpinBox(self.layoutWidget_3)
        self.couple_time_spinBox.setObjectName(u"couple_time_spinBox")
        self.couple_time_spinBox.setValue(6)

        self.horizontalLayout_10.addWidget(self.couple_time_spinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.wash_label = QLabel(self.layoutWidget_3)
        self.wash_label.setObjectName(u"wash_label")

        self.horizontalLayout_11.addWidget(self.wash_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.wash_frequence_spinBox = QSpinBox(self.layoutWidget_3)
        self.wash_frequence_spinBox.setObjectName(u"wash_frequence_spinBox")
        self.wash_frequence_spinBox.setValue(5)

        self.horizontalLayout_11.addWidget(self.wash_frequence_spinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.start_pushButton = QPushButton(self.layoutWidget_3)
        self.start_pushButton.setObjectName(u"start_pushButton")

        self.horizontalLayout_13.addWidget(self.start_pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)

        self.stop_pushButton = QPushButton(self.layoutWidget_3)
        self.stop_pushButton.setObjectName(u"stop_pushButton")

        self.horizontalLayout_13.addWidget(self.stop_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.toolBox.addItem(self.page_7, u"\u5f00\u59cb\u9875\u9762")

        self.verticalLayout_7.addWidget(self.toolBox)


        self.horizontalLayout_9.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(400, 500))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.output_label = QLabel(self.frame_2)
        self.output_label.setObjectName(u"output_label")

        self.horizontalLayout_16.addWidget(self.output_label)

        self.clear_button = QPushButton(self.frame_2)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setLayoutDirection(Qt.LeftToRight)
        self.clear_button.setAutoFillBackground(False)
        self.clear_button.setFlat(False)

        self.horizontalLayout_16.addWidget(self.clear_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.display_text = QTextBrowser(self.frame_2)
        self.display_text.setObjectName(u"display_text")
        self.display_text.setMinimumSize(QSize(198, 0))
        self.display_text.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.verticalLayout_5.addWidget(self.display_text)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")

        self.verticalLayout_11.addWidget(self.groupBox)


        self.verticalLayout_5.addLayout(self.verticalLayout_11)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 10)
        self.verticalLayout_5.setStretch(2, 10)

        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_9.addLayout(self.verticalLayout_6)


        self.horizontalLayout_9.addWidget(self.frame_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)


        self.retranslateUi(Form)

        self.toolBox.setCurrentIndex(6)
        self.clear_button.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Kamor\u6cf5\u7684\u63a7\u5236", None))
#if QT_CONFIG(tooltip)
        self.toolBox.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pump3_label.setText(QCoreApplication.translate("Form", u"pump3:", None))
        self.pump3_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump3_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump3_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.pump4_label.setText(QCoreApplication.translate("Form", u"pump4:", None))
        self.pump4_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump4_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump4_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.pump5_label.setText(QCoreApplication.translate("Form", u"pump5:", None))
        self.pump5_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump5_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump5_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.unit1_wash.setText(QCoreApplication.translate("Form", u"wash:", None))
        self.unit1_wash_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.unit1_wahs_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.unit1_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.unit1_waste_label.setText(QCoreApplication.translate("Form", u"waste:", None))
        self.unit1_waste_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.unit1_waste_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.unit1_waste_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.unit1_depro_label.setText(QCoreApplication.translate("Form", u"\u8131\u4fdd\u62a4\uff1a", None))
        self.unit1_depro_start_button.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.unit1_depro_stop_button.setText(QCoreApplication.translate("Form", u"\u6682\u505c", None))
        self.unit1_couple_label.setText(QCoreApplication.translate("Form", u"\u7f29\u5408\uff1a", None))
        self.unit1_couple_start_button.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.unit1_couple__stop_button.setText(QCoreApplication.translate("Form", u"\u6682\u505c", None))
        self.unit1_wash_label.setText(QCoreApplication.translate("Form", u"\u6e05\u6d17\uff1a", None))
        self.unit1_wash_start_button.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Form", u"unit 1", None))
        self.pump6_label.setText(QCoreApplication.translate("Form", u"pump6:", None))
        self.pump6_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump6_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump6_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.pump7_label.setText(QCoreApplication.translate("Form", u"pump7:", None))
        self.pump7_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump7_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump7_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.pump8_label.setText(QCoreApplication.translate("Form", u"pump8:", None))
        self.pump8_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump8_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump8_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.unit2_wash.setText(QCoreApplication.translate("Form", u"wash:", None))
        self.unit2_wash_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.unit2_wahs_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.unit2_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.unit2_waste_label.setText(QCoreApplication.translate("Form", u"waste:", None))
        self.unit2_waste_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.unit2_waste_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.unit2_waste_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.unit2_depro_label.setText(QCoreApplication.translate("Form", u"\u8131\u4fdd\u62a4\uff1a", None))
        self.unit2_depro_start_button.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.unit2_depro_stop_button.setText(QCoreApplication.translate("Form", u"\u6682\u505c", None))
        self.unit2_couple_label.setText(QCoreApplication.translate("Form", u"\u7f29\u5408\uff1a", None))
        self.unit2_couple_start_button.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.unit2_couple__stop_button.setText(QCoreApplication.translate("Form", u"\u6682\u505c", None))
        self.unit2_wash_label.setText(QCoreApplication.translate("Form", u"\u6e05\u6d17\uff1a", None))
        self.unit2_wash_start_button.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Form", u"unit 2", None))
        self.pump9_label.setText(QCoreApplication.translate("Form", u"pump9:", None))
        self.pump9_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump9_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump9_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.pump10_label.setText(QCoreApplication.translate("Form", u"pump10:", None))
        self.pump10_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump10_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump10_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.pump11_label.setText(QCoreApplication.translate("Form", u"pump11:", None))
        self.pump11_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump11_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump11_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.unit3_wash.setText(QCoreApplication.translate("Form", u"wash:", None))
        self.unit3_wash_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.unit3_wahs_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.unit3_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.unit3_waste_label.setText(QCoreApplication.translate("Form", u"waste:", None))
        self.unit3_waste_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.unit3_waste_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.unit3_waste_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.unit3_depro_label.setText(QCoreApplication.translate("Form", u"\u8131\u4fdd\u62a4\uff1a", None))
        self.unit3_depro_start_button.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.unit3_depro_stop_button.setText(QCoreApplication.translate("Form", u"\u6682\u505c", None))
        self.unit3_couple_label.setText(QCoreApplication.translate("Form", u"\u7f29\u5408\uff1a", None))
        self.unit3_couple_start_button.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.unit3_couple__stop_button.setText(QCoreApplication.translate("Form", u"\u6682\u505c", None))
        self.unit3_wash_label.setText(QCoreApplication.translate("Form", u"\u6e05\u6d17\uff1a", None))
        self.unit3_start_wash_button.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("Form", u"unit 3", None))
        self.pump12_label.setText(QCoreApplication.translate("Form", u"pump12:", None))
        self.pump12_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump12_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump12_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.pump13_label.setText(QCoreApplication.translate("Form", u"pump13:", None))
        self.pump13_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump13_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump13_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.pump14_label.setText(QCoreApplication.translate("Form", u"pump14:", None))
        self.pump14_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump14_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump14_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.unit4_wash.setText(QCoreApplication.translate("Form", u"wash:", None))
        self.unit4_wash_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.unit4_wahs_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.unit4_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.unit4_waste_label.setText(QCoreApplication.translate("Form", u"waste:", None))
        self.unit4_waste_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.unit4_waste_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.unit4_waste_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.unit4_depro_label.setText(QCoreApplication.translate("Form", u"\u8131\u4fdd\u62a4\uff1a", None))
        self.unit4_depro_start_button.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.unit4_depro_stop_button.setText(QCoreApplication.translate("Form", u"\u6682\u505c", None))
        self.unit4_couple_label.setText(QCoreApplication.translate("Form", u"\u7f29\u5408\uff1a", None))
        self.unit4_couple_start_button.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.unit4_couple__stop_button.setText(QCoreApplication.translate("Form", u"\u6682\u505c", None))
        self.unit4_wash_label.setText(QCoreApplication.translate("Form", u"\u6e05\u6d17\uff1a", None))
        self.unit4_start_wash_button.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("Form", u"unit 4", None))
        self.pump15_label.setText(QCoreApplication.translate("Form", u"pump15:", None))
        self.pump15_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump15_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump15_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.pump16_label.setText(QCoreApplication.translate("Form", u"pump16:", None))
        self.pump16_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump16_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump16_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.pump17_label.setText(QCoreApplication.translate("Form", u"pump17:", None))
        self.pump17_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pump17_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pump17_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.unit5_wash.setText(QCoreApplication.translate("Form", u"wash:", None))
        self.unit5_wash_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.unit5_wahs_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.unit5_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.unit5_waste_label.setText(QCoreApplication.translate("Form", u"waste:", None))
        self.unit5_waste_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.unit5_waste_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.unit5_waste_reverse.setText(QCoreApplication.translate("Form", u"reverse", None))
        self.unit5_depro_label.setText(QCoreApplication.translate("Form", u"\u8131\u4fdd\u62a4\uff1a", None))
        self.unit5_depro_start_button.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.unit5_depro_stop_button.setText(QCoreApplication.translate("Form", u"\u6682\u505c", None))
        self.unit5_couple_label.setText(QCoreApplication.translate("Form", u"\u7f29\u5408\uff1a", None))
        self.unit5_couple_start_button.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.unit5_couple__stop_button.setText(QCoreApplication.translate("Form", u"\u6682\u505c", None))
        self.unit5_wash_label.setText(QCoreApplication.translate("Form", u"\u6e05\u6d17\uff1a", None))
        self.unit5_wash_start_button.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("Form", u"unit5", None))
        self.value1_label.setText(QCoreApplication.translate("Form", u"value1", None))
        self.value1_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.value1_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.value2_label.setText(QCoreApplication.translate("Form", u"value2", None))
        self.value2_open_button.setText(QCoreApplication.translate("Form", u"Open", None))
        self.value2_stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pressure_time_label.setText(QCoreApplication.translate("Form", u"\u538b\u529b\u6d4b\u91cf\u65f6\u95f4\uff1a", None))
        self.pressure_start.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u538b\u529b\u6d4b\u91cf", None))
        self.file_name_label.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u540d\uff1a", None))
        self.pressure_display.setText(QCoreApplication.translate("Form", u"\u538b\u529b\u663e\u793a", None))
        self.value2_label_2.setText(QCoreApplication.translate("Form", u"\u591a\u901a\u96002\u901a\u9053\uff1a", None))
        self.valeu2_passage_label.setText(QCoreApplication.translate("Form", u"1", None))
        self.value1_label_2.setText(QCoreApplication.translate("Form", u"\u591a\u901a\u96001\u901a\u9053\uff1a", None))
        self.value1_passage_label.setText(QCoreApplication.translate("Form", u"1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), QCoreApplication.translate("Form", u"value", None))
        self.tepro_vol_label.setText(QCoreApplication.translate("Form", u"\u6258\u4fdd\u62a4\u6db2\u7528\u91cf\uff1a", None))
        self.couple_vol_label.setText(QCoreApplication.translate("Form", u"\u5076\u8054\u6db2\u7528\u91cf\uff1a", None))
        self.tepro_time_label.setText(QCoreApplication.translate("Form", u"\u8131\u4fdd\u62a4\u65f6\u95f4\uff1a", None))
        self.couple_time_label.setText(QCoreApplication.translate("Form", u"\u5076\u8054\u65f6\u95f4\uff1a", None))
        self.wash_label.setText(QCoreApplication.translate("Form", u"\u6d17\u6da4\u6b21\u6570\uff1a", None))
        self.start_pushButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u6309\u94ae", None))
        self.stop_pushButton.setText(QCoreApplication.translate("Form", u"\u7ed3\u675f\u6309\u94ae", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_7), QCoreApplication.translate("Form", u"\u5f00\u59cb\u9875\u9762", None))
        self.output_label.setText(QCoreApplication.translate("Form", u"Output & Result", None))
        self.clear_button.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
    # retranslateUi

