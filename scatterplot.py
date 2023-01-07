import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [11,8,26,16,9,17,23,4,14,10]

plt.scatter(x, y, c=y, cmap='PiYG')  # 繪製散布圖，顏色使用 PiYG 的 colormap
plt.colorbar()   # 加入 colorbar
plt.show()