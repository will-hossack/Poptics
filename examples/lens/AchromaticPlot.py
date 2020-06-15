"""
    Example program to form a wide aperture AchromaticDoublet and trace three
    colours of ray pencil at angle of 5 degrees

"""


from poptics.ray import RayPencil,RayPath
from poptics.lens import AchromaticDoublet
from poptics.vector import Unit3d
from poptics.wavelength import Red,Green,Blue
import poptics.tio as t
import matplotlib.pyplot as plt

def main():

    doublet = AchromaticDoublet(0.0,120,20.0,ct=10)   # 120mm, 20mm radius
    t.tprint("Focal length is :",doublet.backFocalLength())
    u = Unit3d().parseAngle("5")                      # trace at 5 degrees

    #           Make ray pencil of three coloured rays
    pencil = RayPencil().addBeam(doublet,u,nrays = 5 , wavelength = Red)
    pencil.addBeam(doublet,u,nrays = 5, wavelength = Green)
    pencil.addBeam(doublet,u,nrays = 5, wavelength = Blue)
    pencil.addMonitor(RayPath())        # Add monitor to all rays to allow plotting

    ip = doublet.backFocalPlane()       # Back focal plane
    pencil *= doublet                   # Propagte through lens to back focal plane
    pencil *= ip

    #      Draw the diagram
    doublet.draw(True,True)
    ip.draw()
    pencil.draw()
    plt.axis("equal")
    plt.grid()
    plt.title(repr(doublet))
    plt.show()


if __name__ == "__main__":
    main()


