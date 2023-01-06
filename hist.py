import matplotlib.pyplot as plt

import numpy as np

scores=[22, 73, 46, 68, 92, 34, 65, 29, 88, 31,
        66, 94, 77, 85, 29, 59, 11, 85, 79, 84,
        69, 83, 96, 45, 73, 85, 69, 86, 0, 9]           #成績
binsList=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]   #分布區域 (組距)
n, bins, patches=plt.hist(scores, bins=binsList,  edgecolor='black',
         label='Students')        #繪製直方圖

print(n)                              #輸出次數分配
print(bins)                           #輸出分布區間
for p in patches:                     #輸出 Patch 物件內容
    print(p)
plt.legend()      
plt.title('Score Distribution')       #設定圖形標題
plt.ylabel('Scores')                  #設定 Y 軸標籤
plt.xlabel('Students')                #設定 X 軸標籤
plt.show()
