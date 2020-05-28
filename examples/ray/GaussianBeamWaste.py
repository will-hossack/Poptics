
"""
       Example to plot the beam radius over a range of distances
"""
from poptics.ray import GaussianBeam
import numpy as np
from poptics.wavelength import HeNeRed, WavelengthColour
import matplotlib.pyplot as plt


def main():


    waist = 0.1                    # Initial waist
    wavelength = HeNeRed           # Wavelength
    beam = GaussianBeam(0.0,waist,wavelength = wavelength)

    zData = np.linspace(0.0,500,100)    # the z range
    rData = np.zeros(zData.size)        # the radius data

    for i,z in enumerate(zData):        # scan down the range
        beam.propagateTo(z)             # propagate to position z
        rData[i] = beam.getRadius()     # get tbe radius

    #      Do the plot
    colour = WavelengthColour(wavelength)
    plt.plot(zData,rData,c = colour)
    plt.plot(zData,-rData,c = colour)
    plt.show()

main()
