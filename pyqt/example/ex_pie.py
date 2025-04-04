import matplotlib.pyplot as plt
import csv

# 讀取 CSV 檔案並轉換成 dictionary
csv_filename = "sample_data.csv"  # 替換成你的檔案路徑

data_list = []
with open(csv_filename, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)  # 自動使用第一行當作 key
    for row in reader:
        data_list.append(dict(row))  # 轉換成 dictionary
male = 0
female = 0
for i in data_list:
    if i["gender"] == "Male":
        male+=1
    else:
        female+=1
y = [male,female]
mylabels = ["male", "female"]
plt.pie(y, labels = mylabels)
plt.show()