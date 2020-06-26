
"""
    Check SphericalImagePlane
"""

from poptics.analysis import SphericalOpticalImage
import numpy as np
import matplotlib.pyplot as plt

def main():


    radius = 12.0
    curve = 1.0/50
    sp = SphericalOpticalImage(100,curve,xsize = 12.0,ysize = 12.0)
    sp.addTestGrid(8,8)

    radius = sp.maxRadius
    ydata = np.linspace(0.0,radius,10)
    zdata = np.zeros(ydata.size)

    for i,y in enumerate(ydata):
        pt = sp.getSourcePoint(0.0,y)
        zdata[i]= pt.z

    ydata = []
    zdata = []

    for j in range(0,sp.ypixel):
        pt = sp.getPixelSourcePoint(sp.xpixel//2,j)
        print(str(pt))
        ydata.append(pt.y)
        zdata.append(pt.z)

    sp.draw()
    plt.plot(zdata,ydata,"x")
    plt.axis("equal")



    plt.show()

main()