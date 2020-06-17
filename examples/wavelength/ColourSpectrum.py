"""
    Display WavelengthColour sptedrum as an image
"""

from poptics.wavelength import WavelengthColour
import numpy as np
import matplotlib.pyplot as plt

def main():

    xsize = 500
    ysize = 200
    minwave = 0.35      # Min wavelength
    maxwave = 0.75      # Max wavelength
    dw = (maxwave - minwave)/xsize

    #        Make np array to hold colours
    image = np.empty((xsize,ysize,3))

    #        Loop over array filling it up
    for i in range(0,xsize):
        wave = minwave + i*dw
        colour = WavelengthColour(wave)
        for j in range(0,ysize):
            image[i,j] = colour

    plt.imshow(image,aspect = "equal")
    plt.show()

main()
