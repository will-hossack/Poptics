"""
View an display lens in MatPlotLib with a typical ray pencil.

Author: Will Hossack, The University of Edinburgh
"""
from poptics.lens import DataBaseLens
from poptics.ray import RayPencil,RayPath
from poptics.tio import tprint,getFloat
import matplotlib.pyplot as plt
import math


def main():

    #
    #      Read lens in from database
    #
    lens = DataBaseLens()
    lens.setIris(0.7)           # Set iris to 0.7 of max
    #
    #       Make collimated pencil and add ray monitor to each ray
    angle = getFloat("Angle",2.0)
    pencil = RayPencil().addBeam(lens,math.radians(angle),"vl").addMonitor(RayPath())
    #
    tprint("Focal length is : ",lens.backFocalLength())
    tprint("Petzal sum is : ",lens.petzvalSum())
    #
    #        Set the output plane (being the back focal plane)
    op = lens.backFocalPlane()

    #         Propagate pencil through lens and one to back plane
    pencil *= lens       # Through lens
    pencil *= op         # To plane
    #
    #                    Draw the diagram

    plt.axis('equal')
    lens.draw(planes = True, legend = True)
    op.draw()
    pencil.draw()
    #                    Add decorations.
    plt.grid()
    plt.xlabel("Optical Axis")
    plt.ylabel("Height")
    plt.title("Diagram of lens " + lens.title)
    plt.show()

main()










