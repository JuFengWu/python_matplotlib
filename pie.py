import matplotlib.pyplot as plt

import numpy as np

y = np.array([12, 38, 150, 35])
mylabels = ["A", "B", "C", "D"]

plt.pie(y, labels = mylabels)

plt.show()