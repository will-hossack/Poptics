"""
    Test program to cac laulte the relation between focal length and
    the accomodation parameter
"""

from poptics.lens import Eye
import poptics.wavelength as wl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit



def fit(x,a,b,c,d):
    """
    the fit function for accomodation against focal length
    """
    return a*x**3 + b*x**2 + c*x + d

def main():


    #     Mahe default eye
    eye = Eye(0.0)
    print("Original Focalength : " + str(eye.backFocalLength()))

    #      Make a range of accomodation parameters, Note 1.0 is no accomodatiomn
    acc = np.linspace(1.0,1.5,50)
    focal = np.zeros(acc.size)

    #      Go round loops finding focal length for each accomodation value
    for i,a in enumerate(acc):
        eye.accommodation(a)
        focal[i] = eye.backFocalLength(wl.PhotopicPeak)

    #     Do a fit
    popt,pvar = curve_fit(fit,focal,acc)
    print(str(popt))           # print out fite values

    #     No a plot to make sure it is sensible.
    plt.plot(focal,acc)
    plt.plot(focal,fit(focal,*popt),"x")
    plt.show()



main()