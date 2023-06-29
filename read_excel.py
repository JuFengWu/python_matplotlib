import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
data = pd.read_excel('R生物科技公司_人員資料.xlsx')

xPoint = data['月收入(MonthlyIncome)']

plt.plot(xPoint)

plt.show()
