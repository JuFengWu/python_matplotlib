import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button

subPlt = plt.figure(figsize = (5,5)).add_subplot(111)

def value_2_button_click(event):
    print("value_2_button_click")
    subPlt.cla()
    xPoint = np.array([0, 3, 4, 6, 8])
    yPoint = np.array([0,30,26,45,18])
    subPlt.plot(xPoint,yPoint,'o:r')
    plt.draw()

def value_1_button_click(event):
    print("value_1_button_click")
    subPlt.cla()
    xPoint = np.array([0, 5, 7, 11, 13])
    yPoint = np.array([0,34,17,57,16])
    subPlt.plot(xPoint,yPoint,'o:r')
    plt.draw()

xPoint = np.array([0, 3, 4, 6, 8])
yPoint = np.array([0,30,26,45,18])

subPlt.plot(xPoint,yPoint,'o:r')

ax1 = plt.axes([0.7, 0.01, 0.1, 0.05]) # 左、下、寬、高
# 左邊70%的位置, 和下緣5%, 寬為圖像的10％, 高為圖像的7.5%
ax2 = plt.axes([0.81, 0.01, 0.1, 0.05])
value2Button = Button(ax1, 'value2')
value2Button.on_clicked(value_2_button_click)
value1Button = Button(ax2, 'value1')
value1Button.on_clicked(value_1_button_click)

plt.show()
