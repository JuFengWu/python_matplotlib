import matplotlib.pyplot as plt
import matplotlib.image as img

image = img.imread('depth.png')                       

plt.matshow(image, cmap='PiYG')  # 繪製散布圖，顏色使用 PiYG 的 colormap
plt.colorbar()   # 加入 colorbar
plt.show()