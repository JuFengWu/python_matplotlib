import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
data = pd.read_excel('Fake_data.xlsx')

salary = data['MonthlyIncome']

age = data['Age']

def sort_which_element(x):
    return x[1]


combined_list = list(zip(salary, age))

sorted_list = sorted(combined_list, key=sort_which_element)

sortSalary = []
sortAge = []
for i in  sorted_list:
    sortSalary.append(i[0])
for i in  sorted_list:
    sortAge.append(i[1])

plt.plot(sortSalary)

plt.show()

plt.plot(sortAge)

plt.show()

counter = 0
currentAge = 0
currentAgePeople = 0
totalAgeSalary = 0
zipData = []
for i in  sorted_list:
    if counter == 0:
        currentAge = sorted_list[counter][1]
    if counter!=0 and sorted_list[counter][1]!=currentAge:
        zipData.append( (totalAgeSalary/currentAgePeople,currentAge))
        currentAge = sorted_list[counter][1]
        currentAgePeople = 0
        totalAgeSalary = 0
    totalAgeSalary+=sortSalary[counter]
    currentAgePeople+=1
    counter+=1

print(zipData)

ageData = []
averageAgeSalary = []
for i in zipData:
    ageData.append(i[1])
    averageAgeSalary.append(i[0])
    
plt.plot(ageData,averageAgeSalary)

plt.show()    
    

        
        
