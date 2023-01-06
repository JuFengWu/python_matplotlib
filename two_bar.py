import matplotlib.pyplot as plt
import numpy as np

xPoint1 = np.array(["A", "B", "C", "D", "E"])
yPoint1 = np.array([1,30,26,45,18])
plt.subplot(2, 1, 1) #兩行，一列，第一個圖表 
plt.bar(xPoint1,yPoint1)

xPoint1 = np.array(["F", "G", "H", "I", "J"])
yPoint1 = np.array([12,36,22,43,19])
plt.subplot(2, 1, 2) #兩行，一列，第二個圖表 
plt.bar(xPoint1,yPoint1,width = 0.2,color = 'r')
plt.show()