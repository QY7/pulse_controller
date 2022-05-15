import os
import serial.tools.list_ports

port_list = list(serial.tools.list_ports.comports())
# print(port_list)#if there is no serial ports,here wil show '[]'. array mode
if len(port_list) == 0:
   print('No serial ports.')
else:
    for i in range(0,len(port_list)):
        print(port_list[i])

os.system("pause")