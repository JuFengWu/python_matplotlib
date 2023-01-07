import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['font.family'] = 'Meiryo'
# (x, y, z)
x = [1, 2, 3, 4, 5]
y = [1, 2.2, 2.3, 4.9, 5]
z = [1, 2, 3, 4, 5]

# 3D plot
fig = plt.figure()
ax = Axes3D(fig)
ax.plot3D(x, y, z)
ax.set_xlabel("x軸")
ax.set_ylabel("y軸")
ax.set_zlabel("z軸")
plt.show()

