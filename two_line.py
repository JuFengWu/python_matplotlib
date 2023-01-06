import matplotlib.pyplot as plt
import numpy as np

xPoint1 = np.array([0, 3, 4, 6, 8])

yPoint1 = np.array([0,30,26,45,18])

xPoint2 = np.array([0, 5, 7, 11, 13])

yPoint2 = np.array([0,34,17,57,16])

plt.plot(xPoint1,yPoint1,'o:r',xPoint2,yPoint2,'o:b')

plt.show()