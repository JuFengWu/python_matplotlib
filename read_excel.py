import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
data = pd.read_excel('Fake_data.xlsx')

xPoint = data['MonthlyIncome']

print(xPoint)
