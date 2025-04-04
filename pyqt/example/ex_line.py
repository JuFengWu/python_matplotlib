import csv

# 讀取 CSV 檔案並轉換成 dictionary
csv_filename = "financial_data.csv"  # 替換成你的檔案路徑

data_list = []
with open(csv_filename, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)  # 自動使用第一行當作 key
    for row in reader:
        data_list.append(dict(row))  # 轉換成 dictionary

cost = []
revenue = []

for data in data_list:
    cost.append(int(data["費用"]))  # 提取 cost 欄位的值 並轉換為整數!!
    revenue.append(int(data["營收"]))  # 提取 revenue 欄位的值 並轉換為整數!!
# 顯示結果
print(data_list)
import matplotlib.pyplot as plt
import numpy as np

print(cost)

plt.plot(cost,   label="cost")
plt.plot(revenue, label="revenue")
plt.title("A company's cost")
plt.xlabel("time")
plt.ylabel("USD")
plt.legend()
plt.grid(True)
plt.show()