from serial import Serial
import _thread

import serial
import time
class CommunicationInterface:
    def __init__(self,com):
        self.ser = None
        self.com_name = ''
        self.id_mapping = {
            # 格式为[Screen id, component id]
            "minute":[0x00,0x01],
            'second':[0x00,0x02],
            'Tw':[0x00,0x07],
            'Tc':[0x00,0x15],
            "voltage_max":[0x00,0x26],
            'width1_us_0':[0x01,0x4],
            'width1_us_1':[0x01,0x7],
            'width1_us_2':[0x01,0x3B],
            'width2_us_0':[0x01,0x05],
            'width2_us_1':[0x01,0x08],
            'width2_us_2':[0x01,0x0B],
            'phase_us_0':[0x01,0x06],
            'phase_us_1':[0x01,0x09],
            'phase_us_2':[0x01,0x0C],
            'D1':[0x01,0x16],
            'D2':[0x01,0x17],
            'phase2':[0x01,0x18],
            'M':[0x01,0x1E],
            'index':[0x01,0x0D],
            'pulse_source_index':[0x00,0x12],
            'frequency_0':[0x01,0x1A],
            'frequency_1':[0x01,0x1B],
            'frequency_2':[0x01,0x1C],
            'internal':[0x00,0x7A],
            'external':[0x00,0x7B],
            'preset0':[0x01,0x7C],
            'preset1':[0x01,0x7D],
            'preset2':[0x01,0x7E]
        }


    def set_com(self,com_name):
        self.com_name = com_name
        print(f"[INFO] Change to {com_name}")

    def start_com(self):
        try:
            self.ser.close()
        except:
            pass
        if(self.ser is None):
            self.ser=Serial(self.com_name,115200,timeout=0.5)
        else:
            self.ser.open()
        # self.ser.open()
        print("[INFO] serial connected")

    def com_valid(self):
        return self.ser is not None

    def stop_com(self):
        start_cmd = bytes()
        start_cmd += bytes([0xEE,0xB1,0x11])
        start_cmd += bytes([0x00,0x00])
        start_cmd += bytes([0x00,0x69])
        start_cmd += bytes([0x00,0xFF,0xFC,0xFF,0xFF])
        start_cmd += '\n'.encode()
        self.ser.write(start_cmd)
        time.sleep(1)
        self.ser.close()
        print("[INFO] serial disconnected")
        

    def format_data(self,name,value):
        # 转换数据的格式，生成数据帧
        format_result = bytes()
        format_result += bytes([0xEE,0xB1,0x11])
        if(name=='voltage_max'):
            value*=1000
        try:
            format_result += bytes([0x00,self.id_mapping[name][0]])
            format_result += bytes([0x00,self.id_mapping[name][1],0x11])
            format_result += str(value).encode()
        except KeyError:
            print('[ERROR] Variable does not exist, please check it!')
        format_result += bytes([0x00,0xFF,0xFC,0xFF,0xFF])
        format_result += '\n'.encode()

        return format_result

    def start_pwm(self):
        start_cmd = bytes()
        start_cmd += bytes([0xEE,0xB1,0x11])
        start_cmd += bytes([0x00,0x00])
        start_cmd += bytes([0x00,0x08])
        start_cmd += bytes([0x00,0xFF,0xFC,0xFF,0xFF])
        start_cmd += '\n'.encode()
        try:
            self.ser.write(start_cmd)
            print("[INFO] PWM has started")
        except serial.serialutil.PortNotOpenError:
            print("[ERROR] Port has been closed")
            raise AttributeError

    def stop_pwm(self):
        start_cmd = bytes()
        start_cmd += bytes([0xEE,0xB1,0x11])
        start_cmd += bytes([0x00,0x00])
        start_cmd += bytes([0x00,0x09])
        start_cmd += bytes([0x00,0xFF,0xFC,0xFF,0xFF])
        start_cmd += '\n'.encode()
        try:
            self.ser.write(start_cmd)
            print("[INFO] PWM has stopped")
        except serial.serialutil.PortNotOpenError:
            print("[ERROR] Port has been closed")
            raise AttributeError
    def send_data(self,name,value):
        # 将数据格式转化
        try:
            formatted_data = self.format_data(name, value)
            # # 转换为可以人能看的十六进制的数据
            # str_hex = ":".join("{:02x}".format(ord(c)) for c in formatted_data)
            # 打印
            # print(f"Send data {str_hex}")
            # 输出到串口
            self.ser.write(formatted_data)
            print("[INFO] %s has been changed to %s"%(name.capitalize(),value))
        except serial.serialutil.PortNotOpenError:
            print("[ERROR] Port has been closed")
            # raise AttributeError
    def send_number(self,name,value):
        format_result = bytes()
        format_result += bytes([0xEE,0xB1,0x11])
        try:
            format_result += bytes([0x00,self.id_mapping[name][0]])
            format_result += bytes([0x00,self.id_mapping[name][1],0x11])
            format_result += bytes([value])
        except KeyError:
            print('[ERROR] Variable does not exist, please check it!')
        format_result += bytes([0x00,0xFF,0xFC,0xFF,0xFF])
        format_result += '\n'.encode()
        print(format_result)
        self.ser.write(format_result)

    # change trigger mode index
    def change_pulse_index(self,trigger_mode):
        """修改PWM的触发模式

        Args:
            trigger_mode (str): internal或者external
        """
        if(trigger_mode == 'internal'):
            self.send_number("pulse_source_index",0x00)
            print("[INFO] Index change to internal")
        else:
            self.send_number("pulse_source_index",0x01)
            print("[INFO] Index change to external")

    # change preset index
    def change_index(self,index):
        self.send_number("index",0x00+index)
        print(f"[INFO] Pulse Index: {index}")

    @DeprecationWarning
    def change_port(self,value):
        com_name = value.split(' ')[0]
        print(com_name)
        self.set_com(com_name)
        # _thread.start_new_thread(self.get_data_from_serial, (com,))

com = CommunicationInterface("")