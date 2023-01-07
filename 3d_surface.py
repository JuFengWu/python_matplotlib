import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
 
plt.rcParams['font.family'] = 'Meiryo'
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

data = np.linspace(-3*np.pi,3*np.pi,50) #等差數列

x, y = np.meshgrid(data,data)

z = np.cos(x/np.pi)*np.sin(y/np.pi)
#z = np.zeros((50,50))
ax.plot_surface(x,y,z,cmap="winter")
plt.show()