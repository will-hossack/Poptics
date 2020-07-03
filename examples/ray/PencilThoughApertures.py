
"""
        Example of of simple collimated RayPencil with two apertures.
"""

from poptics.ray import RayPencil, RayPath, Disc
from poptics.surface import CircularAperture, IrisAperture
from poptics.vector import Unit3d
import matplotlib.pyplot as plt

def main():

    #        Form a disc and two apertures both 20mm with Iris closed to 0.5 ratio
    disc = Disc(20,20)
    ca = CircularAperture(50,20)
    iris = IrisAperture(80,20,0.5)
    #        Forma an angle for the pencil at 10deg up nore "10" specified in degrees.
    u = Unit3d().parseAngle("10")
    #        Form a pencil is the circular aperture as specified angle of 0.45 microns
    #        and add a RayPath to ech ray
    pencil = RayPencil().addBeam(disc,u,wavelength = 0.59).addMonitor(RayPath())

    #        Propgate throgh the iris aperture and another 30 mm to make it visible
    pencil *= ca
    pencil *= iris
    pencil += 30

    #               Make a diagram
    disc.draw()
    ca.draw()
    iris.draw()
    pencil.draw()
    plt.axis("equal")
    plt.show()


main()


