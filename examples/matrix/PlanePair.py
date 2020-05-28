"""
Example code to take a system of two thick singlet lenses the first on art 50 mm
and plot the  focal length of as the second lens is moved from 60 to 100 mm.

"""
from poptics.matrix import ParaxialThickLens
from poptics.ray import RayPencil, RayPath
import matplotlib.pyplot as plt

def main():

    lens = ParaxialThickLens(30,0.025,1.61,10.0,-0.035,5.0)
    lens.setFocalLength(50)     # Scale to 50 mm focal length
    print(repr(lens))


    mag = -0.3
    obj,ima = lens.planePair(50,mag)     #  Make pair of planes
    print("Object Plane : " + str(repr(obj)))
    print("New Image Plane : " + str(repr(ima)))

    #        Make paraxial pencil from a point on object plane
    pencil = RayPencil().addSourceParaxialBeam(lens,-0.5*obj.getHeight(), obj)
    pencil.addMonitor(RayPath())

    pencil *= lens
    pencil *= ima


    # Draw diagram
    lens.draw(True)
    obj.draw()
    ima.draw()
    pencil.draw()
    plt.axis("equal")
    plt.show()
main()
