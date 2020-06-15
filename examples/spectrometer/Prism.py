"""
         Example program create a prism with three colout input beam
         with the output beam straightened and put through a vieweing lens

"""
import math
from poptics.spectrometer import Prism
from poptics.wavelength import Red,Green,Blue
from poptics.ray import Disc,RayPencil,RayPath
import matplotlib.pyplot as plt


def main():

    #      Make a 40m high prism of F4 glass at the origin
    prism = Prism(0,height = 40, index = "F4")
    prism.setTilt(math.radians(5))
    #      Calcuate min deviation angle a
    minDev = prism.minDeviation(Green)
    print("Min deviation at Green: {0:6.4f}".format(math.degrees(minDev)))

    # Form a pencil and add in three beams of R,G,B along the optical axis
    # Start of beeams given by 10mm diameter disc at -50mm before prism
    disc = Disc(-50.0 ,8.0)
    pencil = RayPencil()               # Make blank pencil
    pencil.addBeam(disc,0.0,wavelength = Green)  # Add the three coloured beams.
    pencil.addBeam(disc,0.0,wavelength = Blue)   # default of 21 rays in vertical line
    pencil.addBeam(disc,0.0,wavelength = Red)
    angle = minDev/2                       # Angle of beam at half min deviation
    pencil.rotateAboutX(angle,prism.getInputPoint()) # retate beam about inpout point
    print("Numnber of rays : " + str(len(pencil)))
    pencil.addMonitor(RayPath())           # Add a monitor to allow plotting

    pencil *= prism                        # propagate beam through prism
    pencil += 50.0



    #       Generate the diagram
    prism.draw()
    pencil.draw()
    plt.axis("equal")
    plt.grid()
    plt.xlabel("mm along optical axis")
    plt.show()



main()
