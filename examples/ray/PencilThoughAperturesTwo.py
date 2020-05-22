"""
        Example of of simple souce RayPencil with two apertures.
"""

from poptics.ray import RayPencil, RayPath, SourcePoint
from poptics.surface import CircularAperture, IrisAperture
from poptics.vector import Vector3d
import matplotlib.pyplot as plt

def main():
    
    #        Form two apertures both 20mm with Iris closed to 0.5 ratio
    ca = CircularAperture(50,20)
    iris = IrisAperture(80,20,0.5)
    #        source for the rays at (0,10,-50) in global coordinates
    source = SourcePoint(Vector3d(0.0,10,-50))
    #        Form a pencil is the circular aperture as specified angle of 0.45 microns
    #        and add a RayPath to ech ray
    pencil = RayPencil().addBeam(ca,source,wavelength = 0.65).addMonitor(RayPath())
    
    #        Propgate throgh the the both aperture and another 30 mm to make it visible
    pencil *= ca
    pencil *= iris
    pencil += 30
    
    #               Make a diagram
    ca.draw()
    iris.draw()
    pencil.draw()
    plt.axis("equal")
    plt.show()
    
    
main()
