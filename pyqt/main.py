
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from graph import Ui_Form
import time
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MyPlt(FigureCanvas):   # 繼承FigureCanvas，成為PyQt5的Qwidget，同時也是matplotlib的FigureCanvas
    def __init__(self, parent=None):
        fig = Figure(dpi=80)  # matplotlib下的figure

        FigureCanvas.__init__(self, fig) # 初始化FigureCanvas
        self.setParent(parent)
        self.axes = fig.add_subplot(111) # 用figure下面的add_subplot方法

    def draw1(self):
        self.axes.clear()
        x = [0, 3, 4, 6, 8]
        y = [0,30,26,45,18]
        self.axes.plot(x, y)
        self.draw()
        
    def draw2(self):
        self.axes.clear()
        x = [0, 5, 7, 11, 13]
        y = [0,34,17,57,16]
        self.axes.plot(x, y)
        self.draw()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton1.clicked.connect(self.push_button1_click)
        self.ui.pushButton2.clicked.connect(self.push_button2_click)
        self.create_graph()
        
    def create_graph(self):
        self.myPlt = MyPlt()
        graphicview = QtWidgets.QGraphicsView()# 產生graph view
        graphicscene = QtWidgets.QGraphicsScene()# 產生graph scene
        graphicscene.addWidget(self.myPlt)
        graphicview.setScene(graphicscene)
        self.ui.stackedWidget.addWidget(graphicview)
        graphicview.show()
        
    def push_button1_click(self):
        self.myPlt.draw1()
        
    def push_button2_click(self):
        self.myPlt.draw2()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
