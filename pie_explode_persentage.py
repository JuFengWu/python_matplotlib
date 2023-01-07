import matplotlib.pyplot as plt

import numpy as np

y = np.array([12, 38, 150, 35])
mylabels = ["A", "B", "C", "D"]
myexplode = [0, 0.3, 0, 0]
plt.pie(y, labels = mylabels, explode = myexplode,autopct='%1.3f%%')

plt.show()