from re import sub
from tracemalloc import stop
import PyQt5
from PyQt5.QtGui import QColor, QPalette, qRed
from sqlalchemy import except_all
from ui import Ui_MainWindow
from ui_sub import Ui_Form
from PyQt5 import QtWidgets
import sys
from ConmmunicationInterface import CommunicationInterface
import os
import serial.tools.list_ports
import _thread
from ConmmunicationInterface import com
from PyQt5 import QtCore
from PyQt5.QtMultimedia import *
import time
from math import floor
import threading
import json
import serial
import pyqtgraph as pg
from random import randint
from custom_setting import  *

import logging
logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='new.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
# logging.debug('debug 信息')
# logging.info('info 信息')
# logging.warning('warning 信息')
# logging.error('error 信息')
# logging.critical('critial 信息')

pg.setConfigOptions(foreground=QColor(0,0,0),antialias=True)
pg.setConfigOptions(background=QColor(255,255,255),antialias=True)



class Controller_ui(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Controller_ui,self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer1 = QtCore.QTimer(self)
        self.timer1.timeout.connect(self.update_time)

        self.graphWidget = pg.PlotWidget()
        self.ui.verticalLayout.addWidget(self.graphWidget)
        # self.setCentralWidget(self.ui.graphWidget)

        # self.x = list(range(100))  # 100 time points
        # self.y = [randint(0,100) for _ in range(100)]  # 100 data points

        pen = pg.mkPen(color=(255, 0, 0),width=2)
        # self.graphWidget.setXRange(0,100)
        self.graphWidget.setYRange(-5000,5000)
        self.data_line =  self.graphWidget.plot(data_index, data_received, pen=pen)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        logging.info('Timer start!')
        self.timer.start()
        # self.playlist = QMediaPlaylist()
        # self.player = QMediaPlayer()
        # self.player.setVideoOutput(self.ui.player_w)                 # 视频播放输出的widget，就是上面定义的
        # url = QtCore.QUrl.fromLocalFile('D:\\Documents\\KeyShot 7\\Animations\\Drone_control.30\\Drone_control.30.mp4')
        # self.playlist.addMedia(QMediaContent(url))
        # self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        # self.player.setPlaylist(self.playlist)
        # self.player.play()
        # self.ui.player_w.show()
        logging.info('Turnning on UI')
        self.show()
    def update_plot_data(self):
        logging.info('Update data in the graph')
        self.data_line.setData(data_index, data_received)  # Update the data.

    def update_time(self):
        if(self.total_second is not 0):
            self.total_second-=1
            second_left = int((self.total_second)%60)
            minute_left = int((self.total_second-second_left)/60)
            self.ui.minute_timer.setText(str(minute_left))
            self.ui.second_timer.setText(str(second_left))
            # time.sleep(1)
            logging.info('Update counting down time')
        else:
            com.stop_pwm()
            self.timer1.stop()
            self.ui.start_btn.setStyleSheet('')
            self.ui.stop_btn.setStyleSheet('')
            self.ui.stop_btn_2.setStyleSheet('')
            self.ui.minute_timer.setText('0')
            self.ui.second_timer.setText('0')
            logging.info("Timer stopped")

    def set_params(self):
        if(com.ser == None):
            logging.error('Connected unestablished')
            QtWidgets.QMessageBox.warning(self,"Error","请先连接串口")
        else:
            if(os.path.exists('./password.txt')):
                with open('./password.txt','r')as f:
                    passwd = f.readlines()[0]
            else:
                logging.error('No password config file')
                return
            text,ok = QtWidgets.QInputDialog().getText(QtWidgets.QWidget(),"Password","请输入密码")
            if(ok):
                if(text == passwd):
                    logging.info('Password checked')
                    sub_menu.show()
                else:
                    QtWidgets.QMessageBox.warning(self,"Error","密码错误")

    def start_pulse(self):
        """开启pwm输出
        """
        try:
            
            com.start_pwm()
            self.timer1.start(1000)
            minute_tmp = int(self.ui.minute.text())
            second_tmp = int(self.ui.second.text())
            self.ui.second_timer.setText(str(second_tmp))
            self.ui.minute_timer.setText(str(minute_tmp))
            self.total_second = minute_tmp*60+second_tmp
            self.ui.start_btn.setStyleSheet(f'QPushButton {{background-color: red;}}')
            self.ui.stop_btn.setStyleSheet(f'QPushButton {{background-color: red;}}')
            self.ui.stop_btn_2.setStyleSheet(f'QPushButton {{background-color: red;}}')
            # for i in range(second_total):
            logging.debug('Into start')
        except AttributeError:
            QtWidgets.QMessageBox.warning(self,"Error","请确保串口已打开")
            logging.debug('Connection unestablished')
            
    def stop_pulse(self):
        '''
        @TODO 关闭PWM输出
        '''
        try:
            com.stop_pwm()
            self.ui.start_btn.setStyleSheet('')
            self.ui.stop_btn.setStyleSheet('')
            self.ui.stop_btn_2.setStyleSheet('')
            self.timer1.stop()
            self.ui.minute_timer.setText('0')
            self.ui.second_timer.setText('0')
            logging.debug('into stop_pulse')
        except AttributeError:
            QtWidgets.QMessageBox.warning(self,"Error","请确保串口已打开")
            logging.debug('Connection unestablished')
    def take_over(self):
        if(com.com_valid()):
            start_cmd = bytes()
            start_cmd += bytes([0xEE,0xB1,0x11])
            start_cmd += bytes([0x00,0x00])
            start_cmd += bytes([0x00,0x68])
            start_cmd += bytes([0x00,0xFF,0xFC,0xFF,0xFF])
            start_cmd += '\n'.encode()
            com.ser.write(start_cmd)
            logging.debug('into take_over')
        else:
            QtWidgets.QMessageBox.warning(self,"Error","请确保串口已打开")
    def change_com(self,value):
        value = value.split(' ')[0]
        com.set_com(value)
        print(f"{value} selected")
        logging.debug('into change_com')

    def disconnect_serial(self):
        try:
            stop_cmd = bytes()
            stop_cmd += bytes([0xEE,0xB1,0x11])
            stop_cmd += bytes([0x00,0x00])
            stop_cmd += bytes([0x00,0x69])
            stop_cmd += bytes([0x00,0xFF,0xFC,0xFF,0xFF])
            stop_cmd += '\n'.encode()
            com.ser.write(stop_cmd)
            time.sleep(0.5)
            com.stop_com()
            self.ui.connect_info.setText("已断开")
            self.ui.connect_info.setAutoFillBackground(False)
            logging.debug('into disconnect_serial')
        except AttributeError:
            print("[ERROR] Port has already been stopped")
        except serial.serialutil.PortNotOpenError:
            print("[ERROR] Port has been closed")

    def connect_serial(self):
        try:
            com.start_com()
            self.ui.connect_info.setText("已连接")
            self.ui.connect_info.setAutoFillBackground(True)
            palette = QPalette()
            palette.setColor(QPalette.Window, QtCore.Qt.green)
            self.ui.connect_info.setPalette(palette)
            logging.debug('into connect_serial')
        except serial.serialutil.SerialException:
            start_cmd = bytes()
            start_cmd += bytes([0xEE,0xB1,0x11])
            start_cmd += bytes([0x00,0x00])
            start_cmd += bytes([0x00,0x68])
            start_cmd += bytes([0x00,0xFF,0xFC,0xFF,0xFF])
            start_cmd += '\n'.encode()
            com.ser.write(start_cmd)
            logging.error('Port used')

    def set_to_internal(self):
        com.change_pulse_index("internal")


    def set_to_external(self):
        com.change_pulse_index("external")


class SubMenu(QtWidgets.QWidget):
    def __init__(self,parent = None):
        super(SubMenu,self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def set_to_index1(self):
        com.change_index(0)
        print("Index1 selected")

    def set_to_index2(self):
        com.change_index(1)
        print("Index2 selected")

    def set_to_index3(self):
        com.change_index(2)
        print("Index3 selected")

def init_configuration(ui,configs):
    # print(ui.getChildren())
    for key in configs.keys():
        try:
            # 以key为类的属性，然后遍历赋值
            ui.__getattribute__(key).setText(str(configs[key]))
        except AttributeError:
            print("[ERROR] No such attribute yet "+str(key))

@DeprecationWarning
def change_ui_params(name,value):
    # 获取实例，设置参数
    getattr(ui,name).setText(value)
@DeprecationWarning
def change_ui_to_preset(name):
    print(f"[INFO] {name} change")
    getattr(ui,name).click()

@DeprecationWarning
# 不需要从串口读数据了，因为PC是绝对的接管
def change_ui_to_pulse_source(name):
    if(name == 'internal' and not getattr(ui,name).isChecked()):
        ui.internal.click()
    if(name == 'external' and not getattr(ui,name).isChecked()):
        ui.external.click()
    logging.debug('into change_ui_to_pulse_source')


def get_data_from_serial():
    global data_received
    global data_index
    stop_flag = 0
    cnt = 0
    while(True):
        try:
            time.sleep(0.00001)
            if(not com.ser):
                continue
            data_count = com.ser.inWaiting()
            # print(data_count)
            if(data_count!=0):
                datas = com.ser.read(com.ser.inWaiting())
                # com.ser.flushInput()
                for i in range(len(datas)-7):
                    if(datas[i] == 0x3a and datas[i+1]==0xbf and datas[i+2]==0x33):
                        # print(datas[i:])
                        voltage_recv = (int(datas[i+3:i+7])-SAMPLE_BIAS)*SAMPLE_GAIN
                        print(voltage_recv)
                        if(voltage_recv>TRIG_LEVEL):
                            cnt +=1
                            if(cnt==TRIG_HOLD_CNT):
                                stop_flag = 1
                        if(stop_flag == 1):
                            continue
                        data_received = data_received[1:]
                        data_received.append(voltage_recv)
                        # print(int(datas[i+1:i+5]))
                        data_index = data_index[1:]  # Remove the first y element.
                        data_index.append(data_index[-1] + 1)  # Add a new value 1 higher than the last.
                        # data_hex = ['0x%x'%i for i in data_received]
                
                    # print(f"received {','.join(data_hex)}")
                    # print(data_received[-1])
        except serial.serialutil.SerialException:
            continue
        except:
            continue

local_index = 0
local_pulse_source = 0

if __name__ == '__main__':
    data_received = [0]*1000
    data_index = list(range(1000))  # 100 time points
    # 创建ap
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Controller_ui()

    # 初始化子菜单
    sub_menu = SubMenu()
    port_list = list(serial.tools.list_ports.comports())

    # 增加互斥选择，不然button会同时都能选中
    ui.ui.bg1 = QtWidgets.QButtonGroup(MainWindow)
    ui.ui.bg1.addButton(ui.ui.internal,0)
    ui.ui.bg1.addButton(ui.ui.external,1)
    sub_menu.ui.bg2 = QtWidgets.QButtonGroup(MainWindow)
    sub_menu.ui.bg2.addButton(sub_menu.ui.preset0,2)
    sub_menu.ui.bg2.addButton(sub_menu.ui.preset1,3)
    sub_menu.ui.bg2.addButton(sub_menu.ui.preset2,4)

    # 装载文件中的初始设置
    f = open("./configs.json")
    configs = json.load(f)
    init_configuration(ui.ui,configs['1'])
    init_configuration(sub_menu.ui,configs['2'])

    # 初始化串口的选项
    ui.ui.COM.addItem('')
    for i in range(0,len(port_list)):
        ui.ui.COM.addItem(str(port_list[i]))
    thread = threading.Thread(target=get_data_from_serial)
    thread.setDaemon(True)
    thread.start()
    
    sys.exit(app.exec_())
