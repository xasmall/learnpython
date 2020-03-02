import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

x,y = np.mgrid[-4:4:80j,-4:4:40j]
z = 50*np.sin(x+y)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_surface(x,y,z,rstride=2,cstride=1,color='red',)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

