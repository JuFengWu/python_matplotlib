import matplotlib.pyplot as plt

import numpy as np

plt.rcParams['font.family'] = 'Meiryo'
#plot 1:
x = np.array([0, 3, 4, 6, 8])
y = np.array([0,30,26,45,18])
plt.subplot(2, 1, 1) #一行，兩列，第一個圖表
plt.title("你好")
plt.plot(x,y)

#plot 2:
x = np.array([0, 5, 7, 11, 13])
y = np.array([0,34,17,57,16])
plt.subplot(2, 1, 2) #一行，兩列，第二個圖表
plt.title("標題")
plt.plot(x,y)
plt.subplots_adjust(wspace =0, hspace =0.6)

plt.show()