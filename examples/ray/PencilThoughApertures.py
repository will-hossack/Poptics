
"""
        Example of of simple RayPencil with two apertures.
"""

from poptics.ray import RayPencil, RayPath
from poptics.surface import CircularAperture, IrisAperture
from poptics.vector import Angle
import matplotlib.pyplot as plt

def main():
    
    #        Form two apertures both 20mm with Iris closed to 0.5 ratio
    ca = CircularAperture(50,20)
    iris = IrisAperture(80,20,0.5)
    #        Forma an angle for the pencil at 10deg up
    angle = Angle().setDegrees(10,0)
    #        Form a pencil is the circular aperture as specified angle of 0.45 microns
    #        and add a RayPath to ech ray
    pencil = RayPencil().addBeam(ca,angle,wavelength = 0.45).addMonitor(RayPath())
    
    #        Propgate throgh the iris aperture and another 30 mm to make it visible
    pencil *= iris
    pencil += 30
    
    #               Make a diagram
    ca.draw()
    iris.draw()
    pencil.draw()
    plt.axis("equal")
    plt.show()
    
    
main()


