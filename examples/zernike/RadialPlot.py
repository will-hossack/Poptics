"""
    Make plots of the radial(n,m,r) function.
"""

from poptics.zernike import radial
import matplotlib.pyplot as plt
from poptics.tio import getInt
import numpy as np


def main():
    
    #       Get mex value
    n = getInt("n value",4,0)
    

    rData = np.linspace(0.0,1.0,100)     #  rdata is rage 0 > 1.0

    #      Plot out for the range om m
    for m in range(n%2,n + 1,2):
        plt.plot(rData,radial(n,m,rData),label = "m : {0:d}".format(m))

    plt.title("Plot of radial({0:d},m)".format(n))
    plt.legend(loc = "upper left", fontsize = "small")
    plt.xlabel("Radius")
    plt.ylabel("Value")
    plt.show()
    
main()
             
