import sys

import time
from PyQt5 import QtWidgets, QtCore




from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
import matplotlib

import numpy as np

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 解决坐标轴中文显示问题
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号不显示的问题


class Figure_Canvas(FigureCanvas):
    """
    创建画板类
    """

    def __init__(self, width=3, height=5):
        self.fig = Figure(figsize=(width, height), dpi=100)
        super(Figure_Canvas, self).__init__(self.fig)
        self.ax = self.fig.add_subplot(111)  # 111表示1行1列，第一张曲线图

    def add_line(self, x_data, y_data, y2_data=None):
        self.line = Line2D(x_data, y_data)  # 绘制2D折线图

        # ------------------调整折线图基本样式---------------------#

        # self.line.set_ls('--')  # 设置连线
        # self.line.set_marker('*') # 设置每个点
        # self.line.set_color('red')  # 设置线条颜色

        self.ax.grid(True)  # 添加网格
        self.ax.set_title('采样波形')  # 设置标题

        # 设置xy轴最大最小值,找到x_data, y_data最大最小值
        self.ax.set_xlim(0, 500)
        self.ax.set_ylim(-5000,5000)  # y轴稍微多一点，会好看一点

        # self.ax.set_xlabel('x坐标')  # 设置坐标名称
        # self.ax.set_ylabel('y坐标')

        # 在曲线下方填充颜色
        # self.ax.fill_between(x_data, y_data, color='g', alpha=0.1)

        # self.ax.legend([self.line], ['sinx'])  # 添加图例

        # ------------------------------------------------------#
        self.ax.add_line(self.line)
        self.line.set_linewidth(2)
        self.line.set_color('r')

        # # 绘制第二条曲线
        # self.line2 = Line2D(x_data, y2_data)
        # self.ax.add_line(self.line2)
        # self.line2.set_color('red')  # 设置线条颜色
        # self.ax.legend([self.line, self.line2], ['sinx', 'cosx'])  # 添加图例

        # self.ax2 = self.ax.twinx()
        # self.ax2.set_ylabel('y2坐标')