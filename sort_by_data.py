
def sort_which_element(x):
    return x[2]

salary = [50000, 60000, 75000, 100000, 90000]
age = [28, 35, 22, 45, 40]
exp = [4,5,3,8,10]

combined_list = list(zip(salary, age,exp))

sorted_list = sorted(combined_list, key=sort_which_element)

print(sorted_list)

sorted_list = sorted(combined_list, key=sort_which_element,reverse=True)

print(sorted_list)
