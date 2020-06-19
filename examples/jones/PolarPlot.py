"""
    Example program to form a ciccular polasised beam, pass through
    linear polarsier and do a polar plot of the output intensity.
"""


import poptics.jones as j
import matplotlib.pyplot as plt
from poptics.tio import getFloat
import math

def main():

    theta = math.radians(getFloat("Polariser angle",30.0))

    #       Make right circular beam
    beam = j.RightCircularPolarisedBeam()
    print(repr(beam))

    #       Make linear polarsier as specified angle
    polar = j.LinearPolariser(theta)

    #       Pass beam through polarsied and do a polarplot
    beam *= polar
    print(repr(beam))
    beam.polarPlot()

    plt.show()

main()
