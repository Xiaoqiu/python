import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#plot a line
# x = np.linspace(0,10,100)
# plt.plot(x,np.sin(x))
# plt.show();

#scatter-plot points
# x = np.random.normal(size=500)
# y = np.random.normal(size=500)
# plt.scatter(x,y)
# plt.show()

#showing image
# x = np.linspace(1,12,100)
# y = x[:,np.newaxis]
# im = y * np.sin(x) * np.cos(y)
# print(im)
# # imshow - note that origin is at the top-left by default!
# #plt.imshow(im)
# # Contour plot - note that origin here is at the bottom-left by default!
# plt.contour(im)
# plt.show()

#3D plotting
ax = plt.axes(projection='3d')
xgrid,ygrid = np.meshgrid(x,y.ravel())
