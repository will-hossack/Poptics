"""
        Plot the specified opticalZernike along the x,y, and diagonals

"""

import numpy as np
import math
from optics.zernike import opticalZernike, opticalZernikeName
from poptics.tio import getInt
import matplotlib.pyplot as plt

def main():

        #      Get the component
        op = getInt("Component",3)

        #      make data arrays
        rData = np.linspace(-1.0,1.0,100)
        xData = np.empty(rData.size)
        yData = np.empty(rData.size)
        pDiag = np.empty(rData.size)
        nDiag = np.empty(rData.size)

        #          Fill up the arrays

        for i,r in enumerate(rData):
            xData[i] = opticalZernike(1.0,op,r,0.0)   # X
            yData[i] = opticalZernike(1.0,op,0.0,r)   # Y
            rc = r/math.sqrt(2.0)
            pDiag[i] = opticalZernike(1.0,op,rc,rc)   # Pos diagonal
            nDiag[i] = opticalZernike(1.0,op,-rc,-rc) # Neg diagonal

        #     Make the plot
        plt.plot(rData,xData,label = "Horizontal")
        plt.plot(rData,yData,label = "Vertical")
        plt.plot(rData,pDiag,label = "Positive Diagonal")
        plt.plot(rData,nDiag,label = "Negative Diagonal")

        plt.xlim([-1,1])
        plt.ylim([-1,1])
        plt.legend(loc="lower left",fontsize="xx-small")
        plt.title("X/Y plot of " + opticalZernikeName(op))
        plt.show()

if __name__ == "__main__":
    main()

