"""
  Example plot of a TriColour spectrum 
"""

from poptics.wavelength import TriColourSpectrum
from poptics.tio import getFloat
import matplotlib.pyplot as plt

def main() :

    #      Get the red, green, blue relative peak values
    red = getFloat("Red Intensity ",1.0)
    green = getFloat("Greeen Intensity",1.0)
    blue = getFloat("Blue Intensity",1.0)
    
    #       Get spectrum with specified values and default brightness and peak width.
    s = TriColourSpectrum(red, green, blue)
    print(repr(s))
    
    #        Default plot
    s.draw()
    plt.title(repr(s))
    plt.show()
    




main()
