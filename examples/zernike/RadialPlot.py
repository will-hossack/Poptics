"""
    Make plots of the Radial(n,m,r) function
"""

from poptics.zernike import radial
import matplotlib.pyplot as plt
from poptics.tio import getInt
import numpy as np


def main():

    #       Get mex value
    n = getInt("n value",4,0)
    rData = np.linspace(0.0,1.0,100)     #  rdata is rage 0 > 1.0

    #      Plot out for polynomial for the legal range on m
    for m in range(n%2,n + 1,2):
        plt.plot(rData,radial(n,m,rData),label = "m : {0:d}".format(m))

    #     Make a standard plot.
    plt.title("Plot of Radial({0:d},m)".format(n))
    plt.legend(loc = "upper left", fontsize = "small")
    plt.xlim([0,1])
    plt.ylim([-1,1.2])
    plt.xlabel("Radius")
    plt.ylabel("Value")
    plt.show()

if __name__ == "__main__":
    main()

