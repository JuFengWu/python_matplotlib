import matplotlib.pyplot as plt
import numpy as np

xPoint1 = np.array(["A", "B", "C", "D", "E"])

yPoint1 = np.array([1,30,26,45,18])


plt.bar(xPoint1,yPoint1,width = 0.2,color = 'r')

plt.show()