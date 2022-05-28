# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\workspace\Qtdesigner\pulse_generator_control_old.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(982, 510)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QLineEdit { border-radius:4px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font:bold large  \"Microsoft Yahei\";\n"
"    padding:10px;\n"
"}\n"
"QRadioButton{\n"
"    padding:10px\n"
"}\n"
"#label_12{\n"
"    color:\"\"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_12 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.minute = MyLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.minute.setFont(font)
        self.minute.setAlignment(QtCore.Qt.AlignCenter)
        self.minute.setObjectName("minute")
        self.horizontalLayout_7.addWidget(self.minute)
        self.label_14 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.second = MyLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.second.setFont(font)
        self.second.setAlignment(QtCore.Qt.AlignCenter)
        self.second.setObjectName("second")
        self.horizontalLayout_7.addWidget(self.second)
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.label_15)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.label_13 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.COM = QtWidgets.QComboBox(self.frame)
        self.COM.setMinimumSize(QtCore.QSize(150, 0))
        self.COM.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.COM.setFont(font)
        self.COM.setObjectName("COM")
        self.horizontalLayout_4.addWidget(self.COM)
        self.connect_info = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.connect_info.setFont(font)
        self.connect_info.setObjectName("connect_info")
        self.horizontalLayout_4.addWidget(self.connect_info)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.Tw = MyLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.Tw.setFont(font)
        self.Tw.setAlignment(QtCore.Qt.AlignCenter)
        self.Tw.setObjectName("Tw")
        self.horizontalLayout_6.addWidget(self.Tw)
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_6.addWidget(self.label_21)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLineWidth(4)
        self.label_4.setMidLineWidth(4)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.Tc = MyLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.Tc.setFont(font)
        self.Tc.setAlignment(QtCore.Qt.AlignCenter)
        self.Tc.setObjectName("Tc")
        self.horizontalLayout_5.addWidget(self.Tc)
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_5.addWidget(self.label_20)
        self.voltage_max = MyLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.voltage_max.setFont(font)
        self.voltage_max.setAlignment(QtCore.Qt.AlignCenter)
        self.voltage_max.setObjectName("voltage_max")
        self.horizontalLayout_5.addWidget(self.voltage_max)
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_5.addWidget(self.label_22)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.minute_timer = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.minute_timer.setFont(font)
        self.minute_timer.setObjectName("minute_timer")
        self.horizontalLayout_3.addWidget(self.minute_timer)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.second_timer = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.second_timer.setFont(font)
        self.second_timer.setObjectName("second_timer")
        self.horizontalLayout_3.addWidget(self.second_timer)
        self.label_7 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.start_btn = QtWidgets.QPushButton(self.frame)
        self.start_btn.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.start_btn.setFont(font)
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout_2.addWidget(self.start_btn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.stop_btn = QtWidgets.QPushButton(self.frame)
        self.stop_btn.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stop_btn.setFont(font)
        self.stop_btn.setObjectName("stop_btn")
        self.horizontalLayout_2.addWidget(self.stop_btn)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.stop_btn_2 = QtWidgets.QPushButton(self.frame)
        self.stop_btn_2.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stop_btn_2.setFont(font)
        self.stop_btn_2.setObjectName("stop_btn_2")
        self.horizontalLayout_2.addWidget(self.stop_btn_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.internal = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.internal.setFont(font)
        self.internal.setChecked(True)
        self.internal.setAutoExclusive(False)
        self.internal.setObjectName("internal")
        self.horizontalLayout_8.addWidget(self.internal)
        self.external = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.external.setFont(font)
        self.external.setAutoExclusive(False)
        self.external.setObjectName("external")
        self.horizontalLayout_8.addWidget(self.external)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_test = QtWidgets.QLabel(self.frame_2)
        self.label_test.setMinimumSize(QtCore.QSize(500, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_test.setFont(font)
        self.label_test.setAlignment(QtCore.Qt.AlignCenter)
        self.label_test.setObjectName("label_test")
        self.verticalLayout_3.addWidget(self.label_test)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stop_btn.clicked.connect(MainWindow.stop_pulse)
        self.start_btn.clicked.connect(MainWindow.start_pulse)
        self.internal.clicked.connect(MainWindow.set_to_internal)
        self.external.clicked.connect(MainWindow.set_to_external)
        self.stop_btn_2.clicked.connect(MainWindow.set_params)
        self.pushButton_3.clicked.connect(MainWindow.connect_serial)
        self.pushButton_2.clicked.connect(MainWindow.disconnect_serial)
        self.COM.textActivated['QString'].connect(MainWindow.change_com)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_12.setText(_translate("MainWindow", "脉冲控制"))
        self.label_6.setText(_translate("MainWindow", "时间设置"))
        self.minute.setText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", "分"))
        self.second.setText(_translate("MainWindow", "20"))
        self.label_15.setText(_translate("MainWindow", "秒"))
        self.pushButton_3.setText(_translate("MainWindow", "连接"))
        self.pushButton_2.setText(_translate("MainWindow", "断开"))
        self.label_13.setText(_translate("MainWindow", "端口号"))
        self.connect_info.setText(_translate("MainWindow", "已断开"))
        self.label_5.setText(_translate("MainWindow", "周期"))
        self.Tw.setText(_translate("MainWindow", "1"))
        self.label_21.setText(_translate("MainWindow", "秒"))
        self.label_4.setText(_translate("MainWindow", "充电"))
        self.Tc.setText(_translate("MainWindow", "100"))
        self.label_20.setText(_translate("MainWindow", "毫秒"))
        self.voltage_max.setText(_translate("MainWindow", "5"))
        self.label_22.setText(_translate("MainWindow", "千伏"))
        self.minute_timer.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "分"))
        self.second_timer.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "秒"))
        self.start_btn.setText(_translate("MainWindow", "开始"))
        self.stop_btn.setText(_translate("MainWindow", "停止"))
        self.stop_btn_2.setText(_translate("MainWindow", "参数修改"))
        self.internal.setText(_translate("MainWindow", "内部"))
        self.external.setText(_translate("MainWindow", "外部"))
        self.label_test.setText(_translate("MainWindow", "采样数据曲线"))
from MyLineEdit import MyLineEdit
import src_rc