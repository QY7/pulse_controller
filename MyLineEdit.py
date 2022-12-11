from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor
from ConmmunicationInterface import com
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
class MyLineEdit(QtWidgets.QLineEdit):
    def focusInEvent(self, event):
        shadow = QGraphicsDropShadowEffect()
  
        # setting blur radius
        shadow.setColor(QColor(41,121,255))
        shadow.setBlurRadius(10)
        shadow.setOffset(0,0)
        # shadow.s
    
        # adding shadow to the label
        self.setGraphicsEffect(shadow)

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.setGraphicsEffect(None)
        try:
            num_modified = float(self.text())
            # com.local_configuration[self.objectName()] = num_modified
            com.send_data(self.objectName(), num_modified)
             
        except ValueError:
            print("[ERROR] Invalid Input")
        except AssertionError:
            print("[ERROR] Value must be larger thant 0")
        except TypeError:
            pass
        except AttributeError:
            print('[ERROR] Port not open')