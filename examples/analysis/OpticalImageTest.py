"""
    Example to for a test grid and image through simple singlet with default
    parameters.
"""

import matplotlib.pyplot as plt
from poptics.analysis import OpticalImage
from poptics.lens import SimpleSinglet
from poptics.tio import tprint

def main():

    #     Make a test image of 100 x 100 pixels and size 300 x 300 mm
    oi = OpticalImage(0,100,100,300,300)
    oi.addTestGrid(8,8)           # Add a 8 x 8 test grid

    #     Make plot area and plot target on the left
    plt.subplot(1,2,1)
    oi.draw()

    #     Simple singlet of focal length 80mm, radius 10 mm at location 200mm
    lens = SimpleSinglet(200,80,10)

    #      Get a system image with a -0.2 magnification
    im = oi.getSystemImage(lens,-0.2)

    tprint(repr(oi))
    tprint(repr(im))

    #     Plot output image on right.
    plt.subplot(1,2,2)
    im.draw()

    plt.show()


main()
