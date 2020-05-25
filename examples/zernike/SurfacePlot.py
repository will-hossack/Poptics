
"""
Plot Optical Zernikes in 3d

@author: wjh
"""
import math
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
from optics.zernike import opticalZernike

def main():
    xscan = np.linspace(-1.0, 1.0, 50)
    yscan = np.linspace(-1.0, 1.0, 50)
    z = np.zeros((xscan.size,yscan.size))
    #xx, yy = np.meshgrid(x, y, sparse=True)
    for j,y in enumerate(yscan):
        for i,x in enumerate(xscan):
            if x*x + y*y <= 1.0:
                z[i,j] = opticalZernike(1.0,8,x,y)
    
    
    #z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
    
    X,Y = np.meshgrid(xscan,yscan)
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    surf = ax.plot_surface(X, Y, z, 
                       linewidth=1, antialiased=False)
    #cmap=cm.coolwarm,
    # Customize the z axis.
    ax.set_zlim(-2.01, 2.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()
    
main()