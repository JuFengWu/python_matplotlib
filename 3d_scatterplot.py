import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
 
plt.rcParams['font.family'] = 'Meiryo'
 
fig = plt.figure()
ax = Axes3D(fig)

ax.set_xlabel("x軸",color="black")
ax.set_ylabel("y軸",color="black")
ax.set_zlabel("z軸",color="black")

x = np.random.rand(200,1) 
y = np.random.rand(200,1)
z = np.random.rand(200,1)
 
ax.scatter(x,y,z)

plt.show()