import matplotlib.pyplot as plt
import numpy as np

yPoint = np.array([0,30,26,45,18])



plt.plot(yPoint,  marker = 'H', label="example")
plt.title("example - Matplotlib")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.grid(True)
plt.show()