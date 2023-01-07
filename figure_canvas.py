from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
import matplotlib
from custom_setting import *
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
        self.ax.grid(True)  # 添加网格
        self.ax.set_title('采样波形')  # 设置标题

        # 设置xy轴最大最小值,找到x_data, y_data最大最小值
        self.ax.set_xlim(0, WINDOW_SIZE)
        self.ax.set_ylabel("电压(V)")
        self.ax.set_ylim(-5000,5000)  # y轴稍微多一点，会好看一点
        self.ax.set_xticklabels(["0","0.1s","0.2s","0.3s","0.4s","0.5s"])
        self.ax.set_xticks([0,WINDOW_SIZE/5,2*WINDOW_SIZE/5,3*WINDOW_SIZE/5,4*WINDOW_SIZE/5,WINDOW_SIZE])
        self.ax.add_line(self.line)
        self.line.set_linewidth(2)
        self.line.set_color('r')
        plt.tight_layout()