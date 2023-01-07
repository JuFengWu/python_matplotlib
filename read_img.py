import matplotlib.pyplot as plt
import matplotlib.image as img

image = img.imread('Lenna.jpg')                       # 讀取圖片
plt.subplot(1, 2, 1)
plt.imshow(image)                                    # 在圖表中繪製圖片


image = img.imread('gem.png')                       # 讀取圖片
plt.subplot(1, 2, 2)
plt.imshow(image)                                    # 在圖表中繪製圖片
plt.show()                 