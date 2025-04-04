import matplotlib.pyplot as plt
import numpy as np

# 設定中文字型，避免顯示亂碼
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  #（微軟正黑體）
plt.rcParams['axes.unicode_minus'] = False  # 避免負號變成亂碼

xPoint = np.array([0,6,8,13])

yPoint = np.array([0,30,20 ,45])

plt.plot(xPoint,yPoint, label="線條")
plt.title("example - Matplotlib")
plt.xlabel("X 軸")
plt.ylabel("Y axis")
plt.legend()
plt.grid(True)
plt.show()