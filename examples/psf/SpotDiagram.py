"""
   Example Programme to for a Spot Diagram


"""

from poptics.lens import DataBaseLens
from poptics.psf import Psf,SpotDiagram
from poptics.vector import Unit3d,Angle
from poptics.ray import RayPencil,RayPath
from poptics.surface import OpticalPlane
from poptics.wavelength import Default
from poptics.tio import getFloat
import matplotlib.pyplot as plt

def main():

    #      Get lens from database
    lens = DataBaseLens()

    #           Get angle of beam and wavelnegth
    angle = getFloat("Angle in degrees",0.0,0.0,15.0)
    u = Unit3d(Angle().setDegrees(angle))     # Angle as unit vectr
    w = getFloat("Wavelength",Default)

    #    Make two ray pencils, one for spot diagram and one for display (vertical only)
    pencil = RayPencil().addBeam(lens,u,"array",wavelength=w)
    vpencil = RayPencil().addBeam(lens,u,"vl",wavelength=w).addMonitor(RayPath())
    bf = lens.backFocalPlane()

    #            Propagate through lens to back focal plane
    pencil *= lens

    vpencil *=lens
    vpencil *=bf

    #            Get optimal area psf and create a SpotDiagram
    sd = SpotDiagram(pencil)

    #             Go round loop plotting the sopt diagram as various zplane positions

    while True:
        zp = getFloat("Zplane",bf.getPoint().z)
        plane = OpticalPlane(zp)
        plt.subplot(2,1,1)
        lens.draw()
        vpencil.draw()
        plt.axis("equal")
        plt.title("Lens " + lens.title)

        plt.subplot(2,1,2)
        sd.draw(plane,True)
        plt.title("Spot diagram")
        plt.show(block = True)


main()
