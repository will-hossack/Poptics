"""
       Three dimensional plot of specfied Optical Zernike.

"""
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
from optics.zernike import opticalZernike, opticalZernikeName
from poptics.tio import getInt

def main():

    #       Get the component to plot
    op = getInt("Component",3)

    #        Make x/y ranges
    xscan = np.linspace(-1.0, 1.0, 50)
    yscan = np.linspace(-1.0, 1.0, 50)
    z = np.zeros((xscan.size,yscan.size))

    # Fill z array of values
    for j,y in enumerate(yscan):
        for i,x in enumerate(xscan):
            if x*x + y*y <= 1.0:
                z[i,j] = opticalZernike(1.0,op,x,y)

    #    Make mesh for 3d plot
    X,Y = np.meshgrid(xscan,yscan)

    fig = plt.figure()
    ax = fig.gca(projection='3d')     # Set projection

    surf = ax.plot_surface(X, Y, z, linewidth=1, antialiased=False)
                       #cmap=cm.coolwarm)

    ax.set_zlim(-1.1, 1.1)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.title("Plot of " + opticalZernikeName(op))
    plt.show()

if __name__ == "__main__":
    main()