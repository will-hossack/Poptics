"""
   Example Programme for SpotAnimation


"""

from poptics.lens import DataBaseLens
from poptics.psf import Psf,SpotAnimation
from poptics.vector import Unit3d,Angle
from poptics.ray import RayPencil
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

    bf = lens.backFocalPlane()

    #            Propagate through lens to back focal plane
    pencil *= lens
    pencil *= bf

    #            Get optimal area psf and create a SpotDiagram
    psf = Psf().optimalArea(pencil,bf)
    sd = SpotAnimation(pencil)

    #             Go round loop plotting the sopt diagram as various zplane positions

    sd.run(psf.z,1.0,0.1,400)
    #plt.show()


main()
