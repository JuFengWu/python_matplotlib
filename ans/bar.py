import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
data = pd.read_excel('Fake_data.xlsx')

xPoint = data['MonthlyIncome']

overTime = data['OverTime']

counter = 0
overTimePeople = []
for i in overTime:
    if i == "Yes":
        overTimePeople.append(xPoint[counter])
    counter+=1

plt.plot(overTimePeople)

plt.show()
